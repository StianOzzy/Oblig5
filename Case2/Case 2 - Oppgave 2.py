"""

Implementer funksjonen create_car() som tar forskjellig informasjon om en bil som parametere.
Denne skal lage en dictionary for en bil med korrekte nøkkelverdier slik som beskrevet i Case-beskrivelsen,
legger den inn i registeret og returner til slutt bil-dictionaryen.

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

# TEST Case 2 - Oppgave 2

create_car(car_register,"Volvo", "V90", 850_000, 2021, 12,True,0)

volvo = car_register["volvoV90"]
print_car_information(volvo)
print()
print(f"Current cars in car_register\n{car_register}")