'''

Skriv en funksjon som returnerer en dictionary med alle varer som er på lager.
Den returnerte dictionarien skal følge samme format som vareregisteret i
webshop_frontent.py (all_wares-variabelen).

Funksjonen skal hete get_all_wares_in_stock() og skal ta minst én parameter:

1    all_wares - Et vareregister – dictionary

'''

def get_all_wares_in_stock(warelist):
    wares_in_stock = {}
    for key, amount in warelist.items():
        stock = amount["number_in_stock"]
        if stock > 0:
            wares_in_stock[key] = amount
    return wares_in_stock

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
print(get_all_wares_in_stock(all_wares))
