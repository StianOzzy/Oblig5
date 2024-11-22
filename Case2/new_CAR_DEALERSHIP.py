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
RENT_NEW_CAR_FEE = 1000

# DONE
def print_car_information(car):
   print(f"Brand: {car["brand"]}")
   print(f"Model: {car["model"]}")
   print(f"Price: {car["price"]}")
   print(f"Manufactured: {car["year"]}-{car["month"]}")
   if car["new"]:
       print("Condition: New")
   else:
       print("Condition: Old")

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


def get_car_age(car):
    age = date.today().year - car["year"]
    return age


def next_eu_control(car):

    car_year = car["year"]
    car_month = car["month"]

    if car_month < 10:
        car_month = "0"+str(car_month)

    while car_year < date.today().year:
        car_year += 2

    return str(car_year) + "-" + str(car_month) + "-01"


def rent_car_monthly_price(car):
    monthly_price = car["price"]*RENT_CAR_PERCENTAGE/12
    if car["new"]:
        monthly_price += 1000
    return round(monthly_price,2)


def calculate_total_price(car):
    totalprice = car["price"]
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


def is_new(car):
    return car['new']


if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)

    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)
    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}kr.")

    audi = car_register['audiRS3']
    print_car_information(audi)
    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")
