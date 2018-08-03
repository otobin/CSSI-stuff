

states = {"California": "CA", "Arizona": "AZ", "Arkansas": "AK"}

for state in states:
    print("State: " + state + " Abbreviation: " + states[state])


store_prices = {"Cereal": 2.00, "Bread": 4.00, "fiber optic": 25.00, "lambo": 30.00 }

print(store_prices["Cereal"] + store_prices["lambo"])


store_inventory = {"Cereal" : 20, "Bread": 30, "fiber optic": 40, "lambo": 2}


price = str(2 * store_prices["Cereal"] + store_prices["lambo"])
print("The price of two boxes of cereal and one lambo is: " + price)

store_inventory["Cereal"] -= 2
store_inventory["lambo"] -= 1

print(store_inventory["Cereal"])
print(store_inventory["lambo"])

for item in store_prices:
    store_prices[item] *= 1.03

for item in store_prices:
    print(store_prices[item])
