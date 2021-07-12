## Overview

Integration of Gate.io v4 in Python as a subclass of ccxt.base.exchange's Exchange.  
https://www.gate.io/docs/apiv4/en/index.html#gate-api-v4

The current CCXT implementation only supports v2:  
https://github.com/ccxt/ccxt/blob/master/python/ccxt/gateio.py

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
