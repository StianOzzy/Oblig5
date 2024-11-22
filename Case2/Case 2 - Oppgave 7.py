"""

Basert på informasjonen om en bil som finnes i car_register-dictionarien,
lag en klasse som skal kunne holde på informasjonen om en bil isteden.

Legg også til metode-definisjonene (ikke implementasjon) for de funksjonene som er definert i
del 3 av eksamen,som du mener kunne passe inn i denne klassen isteden. Begrunn kort hvorfor.

"""

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

    # De valgte funksjonenene mener jeg er direkte relatert til objektet i denne klassen,
    # og derfor mener jeg at disse burde befinne seg her som metoder

    def print_car_information(car):
        # Skrive ut informasjon om objektet er direkte relatert til objektet i klassen
        pass

    def get_car_age(car):
        # Kalkulering av neste objektets alder er direkte relatert til objektet i klassen
        pass

    def next_eu_control(car):
        # Kalkulering av neste EU-kontroll er direkte relatert til objektet i klassen
        pass

    def rent_car_monthly_price(car):
        # Kalkulering av prisen er direkte relatert til objektet i klassen
        pass

    def calculate_total_price(car):
        # Kalkulering av prisen er direkte relatert til objektet i klassen
        pass