# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionGetStockPrice(Action):
    def name(self) -> Text:
        return "utter_action_get_stock_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Mocked stock prices
        stock_prices = {
            "AAPL": 150.00,
            "MSFT": 250.50,
            "GOOGL": 1800.75,
            "TSLA": 700.25,
            "AMZN": 3500.00
        }
        
        # Get entities
        entities = tracker.latest_message.get("entities")
        if entities:
            for entity in entities:
                if entity["entity"] == "stock":
                    stock = entity["value"].upper()
                    if stock in stock_prices:
                        price = stock_prices[stock]
                        dispatcher.utter_message(text=f"The current price of {stock} is ${price}.")
                    else:
                        dispatcher.utter_message(text=f"Sorry, I couldn't find the price for {stock}.")
        return []

class ActionPlaceOrder(Action):
    def name(self) -> Text:
        return "utter_action_place_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Mocked response
        orders = [
            "Your order has been placed successfully.",
            "Order confirmed.",
            "Done! Your order has been placed.",
            "Your order has been received.",
            "Order processed successfully."
        ]
        order_response = random.choice(orders)
        
        dispatcher.utter_message(text=order_response)
        return []

class ActionCancelOrder(Action):
    def name(self) -> Text:
        return "utter_action_cancel_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Mocked response
        cancel_responses = [
            "Your order has been canceled successfully.",
            "Order canceled.",
            "Done! Your order has been canceled.",
            "Your order has been successfully removed.",
            "Order cancellation processed."
        ]
        cancel_response = random.choice(cancel_responses)
        
        dispatcher.utter_message(text=cancel_response)
        return []

class ActionManageAccount(Action):
    def name(self) -> Text:
        return "utter_action_manage_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Mocked response
        manage_responses = [
            "Your account has been successfully managed.",
            "Account management completed.",
            "Done! Your account has been updated.",
            "Account details modified successfully.",
            "Account changes applied."
        ]
        manage_response = random.choice(manage_responses)
        
        dispatcher.utter_message(text=manage_response)
        return []

class ActionGetExchangeRate(Action):
    def name(self) -> Text:
        return "action_get_exchange_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        source_currency = tracker.latest_message.get("entities", {}).get("source_currency")
        target_currency = tracker.latest_message.get("entities", {}).get("target_currency")
        
        # Define pre-defined currency exchange rates (example)
        exchange_rates = {
            ("USD", "EUR"): 0.82,
            ("EUR", "USD"): 1.22,
            ("USD", "GBP"): 0.72,
            ("GBP", "USD"): 1.39,
            ("EUR", "GBP"): 0.88,
            ("GBP", "EUR"): 1.14,
            # Add more currency pairs and exchange rates as needed
        }
        
        exchange_rate = exchange_rates.get((source_currency, target_currency))
        
        if exchange_rate:
            dispatcher.utter_message(template="utter_exchange_rate", 
                                     source_currency=source_currency, 
                                     target_currency=target_currency, 
                                     exchange_rate=exchange_rate)
        else:
            dispatcher.utter_message("Sorry, I couldn't find the exchange rate for the specified currency pair.")
        
        return []
    

class ActionGetAccountBalance(Action):
    def name(self) -> Text:
        return "action_get_account_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Call your backend API to fetch the current account balance
        # Replace the following line with code to fetch the actual account balance
        account_balance = 1000  # Example: Replace with actual account balance
        
        dispatcher.utter_message(template="utter_account_balance", balance=account_balance)
        
        return []
class UtterCurrencyNews(Action):
    def name(self) -> Text:
        return "utter_currency_news"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Example currency news
        currency_news = [
            "USD strengthens against EUR amid economic uncertainty.",
            "GBP falls as Brexit negotiations face challenges.",
            "JPY sees gains as investors seek safe-haven assets.",
            "AUD surges on positive economic data from China.",
            "CAD weakens due to declining oil prices."
        ]

        news_text = "\n".join(currency_news)
        dispatcher.utter_message(text=f"Here are the latest currency news updates:\n{news_text}")

        return []
    
class ActionTradingStrategies(Action):
    def name(self) -> Text:
        return "action_trading_strategies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Example trading strategies
        strategies = [
            "Trend following",
            "Momentum trading",
            "Mean reversion",
            "Breakout trading",
            "Counter-trend trading"
        ]

        # Format strategies as a string
        strategies_text = "\n".join(strategies)

        dispatcher.utter_message(text=f"Here are some effective trading strategies:\n{strategies_text}")

        return []



