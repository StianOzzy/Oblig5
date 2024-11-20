'''

Case 1 - Oppgave 6

Skriv en funksjon som returnerer prisen (med skatt) av en gitt handlevogn.

Ta fortsatt utgangspunkt i at handlevogn-dictionarien er på følgende format:

{

<varenøkkel 1>: <antall av vare i handlevognen>,

<varenøkkel 2>: <antall av vare i handlevognen>,

etc.
}

Denne funksjonen skal hete calculate_shopping_cart_price() og skal minst ta tre input-parametere:

shopping_cart - En handlevogn - dictionary

all_wares - Et vareregister - dictionary

tax - En skatteprosent - float (standardverdi for skatteprosent skal være 25%) '


'''


def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''

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