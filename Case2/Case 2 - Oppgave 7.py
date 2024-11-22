"""

Basert på informasjonen om en bil som finnes i car_register-dictionarien,
lag en klasse som skal kunne holde på informasjonen om en bil isteden.

Legg også til metode-definisjonene (ikke implementasjon) for de funksjonene som er definert i
del 3 av eksamen,som du mener kunne passe inn i denne klassen isteden. Begrunn kort hvorfor.

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

    car_year = car["year"]
    car_month = car["month"]
    car_name = car["brand"] + " " + car["model"]

    if car_month < 10:
        car_month = "0"+str(car_month)

    while car_year < date.today().year:
        car_year += 2

    return f"Next EU-control for the {car_name} is {str(car_year) + "-" + str(car_month) + "-01"}"

# -------------------------------------------------------------------------------------------------------------------- #


# Case 2 - Oppgave 5

def rent_car_monthly_price(car):
    monthly_price = car["price"]*RENT_CAR_PERCENTAGE/12
    if car["new"]:
        monthly_price += 1000
    return round(monthly_price,2)

# -------------------------------------------------------------------------------------------------------------------- #


# Case 2 - Oppgave 6

def calculate_total_price(car):
    totalprice = car["price"]
    print(totalprice)
    if car["new"]:
        totalprice += 10783
    else:
        if date.today().year - car["year"] <= 3:
            totalprice += 6681
        elif date.today().year - car["year"] <= 11:
            totalprice += 4034
        elif date.today().year - car["year"] <= 29:
            totalprice += 1729
    return totalprice

# -------------------------------------------------------------------------------------------------------------------- #


# Case 2 - Oppgave 7

class Car:
    def __init__(self, brand, model, price, year, month, new=True, km=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.month = month
        self.new = new
        self.km = km

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