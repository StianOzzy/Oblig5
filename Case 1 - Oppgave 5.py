'''

Skriv en funksjon som legger til en vare med et gitt antall i en "handlevogn" i form av en dictionary.
Ta utgangspunkt i at handlevogn-dictionarien er/skal være på følgende format:

{

<varenøkkel 1>: <antall av vare i handlevognen>,

<varenøkkel 2>: <antall av vare i handlevognen>,

etc.
}

Det skal kontrolleres at antallet av den gitte varen som forsøkes å legges til i handlevognen
faktisk er på lager. Hvis det fulle antallet ikke er tilgjengelig, men varen ellers er på lager,
skal det tilgjengelige antallet på lager legges til.

Lag fornuftige utskrifter der du mener det kan være nyttig for brukeren å få informasjon om hva som skjer.

Denne funksjonen skal hete add_number_or_ware_to_shopping_cart() og skal ta minst fire parametere:

'''

def add_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware):

    if ware["number_in_stock"] >= number_of_ware:
        shopping_cart[ware_key] = number_of_ware
        return f"{number_of_ware} instance(s) of {ware_key} were added to shopping cart\n"

    elif ware["number_in_stock"] == 0:
        return f"{ware_key} is not in stock, and could not be added to the shopping cart.\n"

    else:
        shopping_cart[ware_key] = ware["number_in_stock"]
        return (f"Only {ware["number_in_stock"]} instance(s) of {ware_key} are in stock."
                f"These were added to the shopping cart.\n")

# -------------------------------------------------------------------------------------------------------------------- #

all_wares = {
"amd_processor": {
"name": "AMD Ryzen 9 5900X Processor",
"price": 5590.0,
"number_in_stock": 50,
"ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
"description": "All the cores and threads you'll need!",
},
"playstation_5": {
"name": "PlayStation 5",
"price": 5999.0,
"number_in_stock": 0,
"ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
"description": "Next generation console, never in stock!",
},
"hdmi_cable": {
"name": "Belkin Ultra High Speed HDMI Cable - 2m",
"price": 349.0,
"number_in_stock": 3,
"ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
"description": "A high speed overprices HDMI cable!",
}
}

# TEST
my_cart = {}
print(add_ware_to_shopping_cart(all_wares["amd_processor"]["name"], all_wares["amd_processor"], my_cart, 1))
print(add_ware_to_shopping_cart(all_wares["playstation_5"]["name"], all_wares["playstation_5"], my_cart, 1))
print(add_ware_to_shopping_cart(all_wares["hdmi_cable"]["name"], all_wares["hdmi_cable"], my_cart, 4))
print(f"The current shopping cart is: {my_cart}")