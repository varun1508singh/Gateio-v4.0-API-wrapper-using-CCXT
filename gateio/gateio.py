# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
import hmac
from time import time
from urllib.parse import urlparse
import json

import requests

from ccxt.base.exchange import Exchange
import hashlib
import math
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidAddress
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import NotSupported
from ccxt.base.errors import DDoSProtection
from ccxt.base.precise import Precise
import hashlib


class gateio(Exchange):

    def describe(self):
        return self.deep_extend(super(gateio, self).describe(), {
            'id': 'gateio',
            'name': 'Gate.io',
            'countries': ['CN'],
            'version': 'v4',
            'rateLimit': 1000,
            'pro': True,
            'has': {
                'createOrder': True,
            },
            'timeframes': {
                '1m': 60,
                '5m': 300,
                '10m': 600,
                '15m': 900,
                '30m': 1800,
                '1h': 3600,
                '2h': 7200,
                '4h': 14400,
                '6h': 21600,
                '12h': 43200,
                '1d': 86400,
                '1w': 604800,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/31784029-0313c702-b509-11e7-9ccc'
                        '-bc0da6a0e435.jpg',
                'api': {
                    'public': 'https://api.gateio.ws/api',
                    'private': 'https://api.gateio.ws/api',
                },
                'www': 'https://gate.io/',
                'doc': 'https://gate.io/api2',
                'fees': [
                    'https://gate.io/fee',
                    'https://support.gate.io/hc/en-us/articles/115003577673',
                ],
                'referral': 'https://www.gate.io/signup/2436035',
            },
            'api': {
                'private': {
                    'post': [
                        '{account}/orders'
                    ],
                    'delete': [
                        '{account}/orders/{id}'
                    ],
                    'get': [
                        '{account}/orders/{id}'
                    ]
                },
            },
            'fees': {
                'trading': {
                    'tierBased': True,
                    'percentage': True,
                    'maker': 0.002,
                    'taker': 0.002,
                },
            },
            'exceptions': {
                'exact': {
                    '4': DDoSProtection,
                    '5': AuthenticationError,
                    # {result: "false", code:  5, message: "Error: invalid key or sign, please re-generate it from
                    # your account"}
                    '6': AuthenticationError,  # {result: 'false', code: 6, message: 'Error: invalid data  '}
                    '7': NotSupported,
                    '8': NotSupported,
                    '9': NotSupported,
                    '15': DDoSProtection,
                    '16': OrderNotFound,
                    '17': OrderNotFound,
                    '20': InvalidOrder,
                    '21': InsufficientFunds,
                },
                # https://gate.io/api2#errCode
                'errorCodeNames': {
                    '1': 'Invalid request',
                    '2': 'Invalid version',
                    '3': 'Invalid request',
                    '4': 'Too many attempts',
                    '5': 'Invalid sign',
                    '6': 'Invalid sign',
                    '7': 'Currency is not supported',
                    '8': 'Currency is not supported',
                    '9': 'Cuxrrency is not supported',
                    '10': 'Verified failed',
                    '11': 'Obtaining address failed',
                    '12': 'Empty params',
                    '13': 'Internal error, please report to administrator',
                    '14': 'Invalid user',
                    '15': 'Cancel order too fast, please wait 1 min and try again',
                    '16': 'Invalid order id or order is already closed',
                    '17': 'Invalid orderid',
                    '18': 'Invalid amount',
                    '19': 'Not permitted or trade is disabled',
                    '20': 'Your order size is too small',
                    '21': 'You don\'t have enough fund',
                },
            },
            'options': {
                'limits': {
                    'cost': {
                        'min': {
                            'BTC': 0.0001,
                            'ETH': 0.0001,
                            'USDT': 1,
                        },
                    },
                },
            },
        })

    def parse_order_status(self, status):
        statuses = {
            'cancelled': 'canceled',
            # 'closed': 'closed',  # these two statuses aren't actually needed
            # 'open': 'open',  # as they are mapped one-to-one
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        id = self.safe_string_2(order, 'orderNumber', 'id')
        symbol = self.safe_string(order, 'currency_pair')
        timestamp = self.safe_timestamp_2(order, 'create_time', 'ctime')
        timeInForce = self.safe_string(order, 'time_in_force')
        status = self.parse_order_status(self.safe_string(order, 'status'))
        side = self.safe_string(order, 'side')
        price = self.safe_number_2(order, 'price', 'rate')
        amount = self.safe_number_2(order, 'initialAmount', 'amount')
        filled = self.safe_number(order, 'filledAmount')
        # In the order status response, self field has a different name.
        remaining = self.safe_number_2(order, 'leftAmount', 'left')
        feeCost = self.safe_number(order, 'fee')
        feeCurrencyCode = self.safe_string(order, 'fee_currency')
        feeRate = self.safe_number(order, 'feePercentage')
        if feeRate is not None:
            feeRate = feeRate / 100
        return self.safe_order({
            'id': id,
            'clientOrderId': None,
            'datetime': self.iso8601(timestamp),
            'timestamp': timestamp,
            'lastTradeTimestamp': None,
            'status': status,
            'symbol': symbol,
            'type': 'limit',
            'timeInForce': timeInForce,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'cost': None,
            'amount': amount,
            'filled': filled,
            'remaining': remaining,
            'average': None,
            'trades': None,
            'fee': {
                'cost': feeCost,
                'currency': feeCurrencyCode,
                'rate': feeRate,
            },
            'info': order,
        })

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        if type == 'market':
            raise ExchangeError(self.id + ' allows limit orders only')
        method = 'privatePost' + 'Account' + self.capitalize("orders")
        request = {
            'currency_pair': symbol,
            'price': price,
            'amount': amount,
            'side': side
        }
        response = getattr(self, method)(self.extend(request, params))
        return self.parse_order(self.extend({
            'status': 'open',
            'type': side,
            'initialAmount': amount,
        }, response))

    def fetch_order(self, id, symbol=None, params={}):
        params['query']['currency_pair'] = symbol
        request = {
            'id': id
        }
        response = self.privateGetAccountOrdersId(self.extend(request, params))
        return self.parse_order(response)

    def cancel_order(self, id, symbol=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' cancelOrder() requires symbol argument')
        params['query']['currency_pair'] = symbol
        request = {
            'id': id
        }
        return self.privateDeleteAccountOrdersId(self.extend(request, params))

    def sign(self, path, api='private', method='GET', params={}, headers=None, body=None, timestamp=None):
        url = self.urls['api'][api] + "/" + self.version + "/" + self.implode_params(path, params)
        if params['query']:
            url += "?" + self.urlencode(params['query'])
            body = ""
            del params['query']
        else:
            del params['query']
            body = self.omit(params, self.extract_params(path))
            body = json.dumps(body) if body else ""
        url = urlparse(url)
        if api == 'public':
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        else:
            self.check_required_credentials()
            timestamp = str(int(time()))
            sig_string = method + "\n" + url.path + "\n" + url.query + "\n" + hashlib.sha512(
                self.encode(body)).hexdigest() + "\n" + timestamp
            signature = hmac.new(self.encode(self.secret), self.encode(sig_string), hashlib.sha512).hexdigest()
            headers = {
                'KEY': self.apiKey,
                'SIGN': signature,
                'Content-Type': 'application/json',
                'Timestamp': timestamp
            }
        return {'url': url.geturl(), 'method': method, 'body': body, 'headers': headers}
