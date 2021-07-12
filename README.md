# Varun Singh

Coding Assessment for Varun Singh.

## Goal

The goal of this assignment is to assess understanding of a third party codebase (CCXT), cleanliness of implementation, and attention to detail; it is not meant to be tricky or difficult.

## Background

We use CCXT (https://github.com/ccxt/ccxt) as a library to help with exchange integrations because it unifies the different exchange responses into a single consistent format which is used throughout the trading system.

However, some exchanges do not have a CCXT implementation, so we need to create our own based on their API documentation.

## Deliverable

Integrate Gate.io v4 in Python as a subclass of ccxt.base.exchange's Exchange.  
https://www.gate.io/docs/apiv4/en/index.html#gate-api-v4

The current CCXT implementation only supports v2 but you can (and should) use it as an example / framework to speed things up and make it easier:  
https://github.com/ccxt/ccxt/blob/master/python/ccxt/gateio.py

The CCXT methods you should implement are as follows:
- `create_order`
- `cancel_order`
- `fetch_order`

Please ensure that the return values for these methods are in the CCXT unified format. Note that you may need to also implement helper methods when necessary (i.e. `sign`, `parse_order`, etc). You should try to use the CCXT implicit methods whenever possible (https://github.com/ccxt/ccxt/wiki/Manual#implicit-api-methods) and also try to handle exchange exceptions as best as possible, mapping them to CCXT exceptions as accurately as you can.

Here are v4 API credentials that you can use (so as to not need to set up your own account):
```
{
    "apiKey":"23b8b4a24e6b093b31f94927d6f0a96e",
    "secretKey":"c558c602ebbb94a917bd04f2f6c830faf9a0b53d4b900af01968e7b61be668d2"
}
```
There is approximately 0.9 ETH in the account so you can place test orders.

## Notes

Even though CCXT is technically written in JavaScript only and then transpiled into Python and PHP, for the purposes of this exercise you only need to write the Python implementation directly; no need to write the JS version and transpile.

You may use any third party libraries you wish as long as you make it easy to install the dependencies.

## Support

You are strongly encouraged to reach out and ask any questions you would like to get clarity and also make things easier if you are stuck or not sure about anything!

Please do not hesitate to contact me (Han) via Whatsapp at +852 5246 7242 with your questions; just assume that I'm a remote colleague and at your service if you need anything. 

## Extra Credit

If you're feeling extra ambitious...  implement client order ID support for `create_order`, `cancel_order`, and `fetch_order`. A client order ID is a unique identifier for a particular order that's specified by the market participant placing the order, and basically helps link the order back with the algo/strategy that placed the order and keeps track of it.

# Gate.io V4

The gateio package uses the ccxt library to create, cancel and fetch orders on Gate.io using Gate.io V4 API.

Ccxt's implicit methods have been used to make the API calls and the return type is as per the return type of Gate.io V2 API. 

## Endpoints

- **CREATE_ORDER**:
  
  The create order end points creates a limit order on the Gate.io exchange. The user can define the type of account that they want to trade with. Following are the parameters that the user needs to pass to create an order:

    * **Symbol (required):** The currency pair that the user wants to trade
    * **Type:** The type of order that the user wants to place
    * **Side (required):** Either buy or sell order
    * **Amount (required):** The amount of coins that the user wants to buy
    * **Price (required):** Order price
    * **Account:** Type of account that the user wants to trade with (spot, margin)

    ```
  import gateio.gateio as gate
  
    api = gate.gateio({
            "apiKey": "YOUR_API_KEY",
            "secret": "YOUR_API_SECRET"
        })
    
    api.create_order("GXS_USDT", "limit", "buy", 1, price=1, params={"account": "spot", "query": {}})
  ```
  **NOTE: IN EVERY ENDPOINT, THE USER NEEDS TO PASS AN EMPTY DICT "query" IN THE "params" PARAMETER AS MENTIONED IN THE CODE SNIPPET**
  

- **FETCH_ORDER**: 
  
  The fetch order function is used to fetch details of an order that has already been placed. Following are the parameters that the user needs to pass to create an order:
  * **Order_ID:** The order ID of the order that the user wants to fetch data for
  * **Symbol (required):** The currency pair of the order
  * **Account:** Type of account that the user wants to trade with (spot, margin)
  
  ```
  import gateio.gateio as gate
  
    api = gate.gateio({
            "apiKey": "YOUR_API_KEY",
            "secret": "YOUR_API_SECRET"
        })
    
    api.fetch_order(create['id'], create['symbol'], params={"account": "spot", "query": {}})
  ```
  **NOTE: IN EVERY ENDPOINT, THE USER NEEDS TO PASS AN EMPTY DICT "query" IN THE "params" PARAMETER AS MENTIONED IN THE CODE SNIPPET**


- **CANCEL_ORDER**: 
  
  The cancel order function is used to cancel an order that has already been placed and is still in progress. Following are the parameters that the user needs to pass to create an order:
  * **Order_ID:** The order ID of the order that the user wants to cancel
  * **Symbol (required):** The currency pair of the order
  * **Account:** Type of account that the user wants to trade with (spot, margin)
  
  ```
  import gateio.gateio as gate
  
    api = gate.gateio({
            "apiKey": "YOUR_API_KEY",
            "secret": "YOUR_API_SECRET"
        })
    
    api.cancel_order(create['id'], create['symbol'], params={"account": "spot", "query": {}})
  ```
  
  **NOTE: IN EVERY ENDPOINT, THE USER NEEDS TO PASS AN EMPTY DICT "query" IN THE "params" PARAMETER AS MENTIONED IN THE CODE SNIPPET**

## Install

Clone it into your project directory using the following command: 
```
git clone https://github.com/parallel-capital/varun-singh.git
```
Go the the project directory and install Requirements:
```
pip install -r requirements.txt
```
Write a python script to call the endpoints, please use the code snippets mentioned above for reference.