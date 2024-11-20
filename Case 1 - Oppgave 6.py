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
all_wares = {}

def calculate_shopping_cart_price(shopping_cart, all_wares, tax=1.25):
    cart_price = 0
    for item in shopping_cart:
        if item in all_wares:
            cart_price += all_wares[item]["price"] * tax * my_cart[item]
    return cart_price
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

# Fra oppgave 5
def add_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware):
    new_ware = all_wares[ware]
    if new_ware["number_in_stock"] >= number_of_ware:
        shopping_cart[ware] = number_of_ware
        return f"{number_of_ware} instance(s) of {ware_key} were added to shopping cart\n"

    elif new_ware["number_in_stock"] == 0:
        return f"{ware_key} is not in stock, and could not be added to the shopping cart.\n"

    else:
        shopping_cart[ware_key] = new_ware["number_in_stock"]
        return (f"Only {new_ware["number_in_stock"]} instance(s) of {ware_key} are in stock."
                f"These were added to the shopping cart.\n")
my_cart = {}
print(add_ware_to_shopping_cart(all_wares["amd_processor"]["name"], "amd_processor", my_cart, 1))
print(add_ware_to_shopping_cart(all_wares["playstation_5"]["name"], "playstation_5", my_cart, 1))
print(add_ware_to_shopping_cart(all_wares["hdmi_cable"]["name"], "hdmi_cable", my_cart, 3))
print(f"The current shopping cart contains: {my_cart}")

# TEST
print(f"Total price of cart: {calculate_shopping_cart_price(my_cart,all_wares)},- (Tax incl.)")