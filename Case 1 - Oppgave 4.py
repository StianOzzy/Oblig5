'''

Skriv en funksjon som returnerer en Boolean-verdi som representerer om et
spesifisert antall av en gitt vare finnes på lager.

Denne funksjonen skal hete is_number_of_ware_in_stock() og skal minst ta to parametere:

'''

def is_number_of_ware_in_stock(ware, number_of_ware):
    if ware["number_in_stock"] == number_of_ware:
        return True
    else:
        return False

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

if is_number_of_ware_in_stock(all_wares["amd_processor"], 50):
    print("Code works")