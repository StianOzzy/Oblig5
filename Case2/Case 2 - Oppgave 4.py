"""

Implementer funksjonen next_eu_control() som returnerer et dato-objekt for neste EU-kontroll.
EU-kontrollen skal skje hver 2. år, fra året og måneden bilen ble produsert.
Det er OK om man setter den 1. i måneden i dato-objektet man returnerer.

"""

# -------------------------------------------------------------------------------------------------------------------- #


# Case 2 - Oppgave 1

def print_car_information(car):
   print(f"Brand: {car["brand"]}")
   print(f"Model: {car["model"]}")
   print(f"Price: {car["price"]}")
   print(f"Manufactured: {car["year"]}-{car["month"]}")
   if car["new"] == True:
       print("Condition: New")
   else:
       print("Condition: Old")

# -------------------------------------------------------------------------------------------------------------------- #


# Case 2 - Oppgave 2

def create_car(car_register,brand, model, price, year, month, new=True, km=0):
    car_key = brand.lower()+model.capitalize()
    car_register[car_key] = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km" : km
    }
    return car_key

# -------------------------------------------------------------------------------------------------------------------- #


# Case 2 - Oppgave 3

def get_car_age(car):
    age = date.today().year - car["year"]
    return age

# -------------------------------------------------------------------------------------------------------------------- #


# Case 2 - Oppgave 4

def next_eu_control(car):


# -------------------------------------------------------------------------------------------------------------------- #

# Fra CAR_DEALERSHIP.PY

from datetime import date

car_register = {
"toyotaBZ4X": {
"brand": "Toyota",
"model": "Corolla",
"price": 96_000,
"year": 2012,
"month": 8,
"new": False,
"km": 163_000
},
"pugeot408": {
"brand": "Pugeot",
"model": "408",
"price": 330_000,
"year": 2019,
"month": 1,
"new": False,
"km": 40_000
},
"audiRS3": {
"brand": "Audi",
"model": "RS3",
"price": 473_000,
"year": 2022,
"month": 2,
"new": True,
"km": 0
},
}

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000

# -------------------------------------------------------------------------------------------------------------------- #

# TEST Case 2 - Oppgave 4

toyota = car_register["toyotaBZ4X"]
print(get_car_age(toyota))