'''

Skriv en funksjon som returnerer den gjennomsnittlige ratingen (en float verdi med én desimal)
for en gitt vare. Det vil si summen av alle ratingene for denne varen delt på antallet ratinger.
Bemerk at hvis listen er tom, vil denne utregningen føre til en ZeroDivisionError.

Funksjonen skal hete calculate_average_ware_rating() og skal ta minst én parameter:

'''


def calculate_average_ware_rating(ware):
    rating = 0
    if len(ware["ratings"]) > 0:
        for i in range(len(ware["ratings"])):
            rating += ware["ratings"][i]
        return round(rating/len(ware["ratings"]),1)
    else: return 0

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
print(calculate_average_ware_rating(all_wares["amd_processor"]))