'''

Skriv en funksjon som printer ut informasjon om en vare på følgende format:

Name: Example Ware
Price: 3999,-
Number in stock: 30
Description: A non-existent ware used only for this example.

Funksjonen skal hete print_ware_information() og skal ta én parameter:

'''

def print_ware_information(ware):
    print(f"Name: {ware.name}")
    print(f"Price: {ware.price},-")
    print(f"Number in stock: {ware.stock}")
    print(f"Description: {ware.description}")


myProducts = {
  "child1" : {
    "name" : "Emil",
    "price" : 9,
    "stock" : 30,
    "description" : "Shitty ass kid"
  },
  "child2" : {
    "name" : "Tobias",
    "price" : 45,
    "stock" : 30,
    "description" : "Decent kid"
  },
  "child3" : {
    "name" : "Linus",
    "price" : 17,
    "stock" : 30,
    "description" : "mid af"
  }
} 

print_ware_information(child1)