'''

Skriv en funksjon som returnerer den gjennomsnittlige ratingen (en float verdi med én desimal)
for en gitt vare. Det vil si summen av alle ratingene for denne varen delt på antallet ratinger.
Bemerk at hvis listen er tom, vil denne utregningen føre til en ZeroDivisionError.

Funksjonen skal hete calculate_average_ware_rating() og skal ta minst én parameter:

'''


def calculate_average_ware_rating(ware):
    rating = 0
    if len(ware.ratings) > 0:
        for ratings in range(len(ware.rating)):
            rating += ware.rating[ratings]
        return rating/len(ware.rating)
    else: return 0
