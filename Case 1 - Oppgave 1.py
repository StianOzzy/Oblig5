'''

Skriv en funksjon som printer ut informasjon om en vare på følgende format:

Name: Example Ware
Price: 3999,-
Number in stock: 30
Description: A non-existent ware used only for this example.

Funksjonen skal hete print_ware_information() og skal ta én parameter:

1   ware - En varereferanse - dictionary

'''

# Oppgi ware i format: (all_wares["amd_processor"])
def print_ware_information(ware):
    print(f"Name: {ware["name"]}")
    print(f"Price: {ware["price"]},-")
    print(f"Number in stock: {ware["number_in_stock"]}")
    print(f"Description: {ware["description"]}")

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
print_ware_information(all_wares["amd_processor"])