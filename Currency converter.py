import requests
import json

class Currency: # Class for all currencies
    def _init_(self, name, code, exchange_rate): # Initializes instances of objects
        self.name = name # Name of Currency, like Dollar (Not really used but important)
        self.code = code # 3 Digit capital lettered code
        self.exchange_rate = exchange_rate # Worth of a dollar (base) wrt a currency (target)

class Converter:
    def __init__(self, base_currency, currencies): # To convert we need a dictionary of currencies and a base currency
        self.base_currency = base_currency # Base currency
        self.currencies = currencies # Dictionary Dictionary

    def convert(self, amount, target_currency): # To convert we need the amount to convert and the target currency
        if self.base_currency not in self.currencies or target_currency not in self.currencies: # Checks if base and target currency are valid
            print("Invalid currency code.")
            return None

        if amount < 0: # Returns error if Amount is Negative
            print("Amount must be a positive number.")
            return None

        base_rate = self.currencies[self.base_currency] # The rate at which base currency is converted to target currency
        target_rate = self.currencies[target_currency] # The rate at which target currency is converted to base currency
        converted_amount = amount * (target_rate / base_rate) # Amount of target currency converted to base
        return converted_amount

class App: # Controls the basic operations of the app like starting
    def __init__(self):
        self.base_currency = "USD" # Default base currency
        self.currencies = self.fetch_exchange_rates()
        #self.currencies = {'USD': 1.00, 'NGN': 767.93, 'EUR': 0.94, 'CAD': 1.35, 'GBP': 0.82, 'INR': 83.06, 'AED': 3.67} #Currency exchange list
        #self.converter = None
        
    def fetch_exchange_rates(self):
        try:
            response = requests.get('https://v6.exchangerate-api.com/v6/d9d8906f62454261760946a5/latest/USD')
            data = response.json()
            return data["conversion_rates"]
        except requests.exceptions.RequestException:
            print("Failed to fetch exchange Rates: ", requests.exceptions.RequestException)
            return {}      
        
    def select_base_currency(self):
        print("Available currencies with their exchange rates:\n")
        for code, rate in self.currencies.items():
            print(f"{code}: {rate}")
        print('\nEnter Q to quit\n')
        base_currency = input("Enter the base currency code: ").upper()
        if base_currency == 'Q':
            return False
        elif base_currency not in self.currencies:
            print("\nInvalid currency code.\n")
            return self.select_base_currency()
        return base_currency

    def app_start(self): # Initializes app
        print("\nCurrency Converter App")
        self.base_currency = self.select_base_currency() # Gets base currency
        if self.base_currency: # if base currency is a valid 3 lettered string
            self.converter = Converter(self.base_currency, self.currencies) #

    def main(self):
        app_running = True  # controls the loop
        while app_running:
            self.app_start()

            if self.base_currency == False:  # Check if base_currency is False indicating 'Q' was entered
                app_running = False  # Set the flag to False to exit the loop
                break

            target_currency = input("\nEnter the target currency code: ").upper()
            if target_currency == 'Q':  # Quits app if target currency is Q
                break

            amount = float(input("Enter the amount to convert: "))
            if amount < 0:
                print("Amount must be a positive number.")  # Checks for positive amount
                continue

            converted_amount = self.converter.convert(amount, target_currency)
            if converted_amount is not None:  # Checks if converted amount is a real number
                print(f"\n{float(amount):.2f} {self.base_currency} is equal to {float(converted_amount):.2f} {target_currency}")
                

if __name__ == '__main__':
    App().main()