2 - Programmeringsoppgaver

 
Case 1 - Vareregister, nettbutikk

Kontekst

Denne delen består av 8 oppgaver basert på et felles tema som går ut på et tiltenkt vareregister for en nettbutikk. Koden du skal skrive vil håndtere forskjellig backend-funksjonalitet tilnærmet konseptene vi har vært gjennom i kurset. Vareregisteret er basert på en nestet dictionary hvor hver vare har en varenøkkel og tilhørende informasjon slik som navnet på varen, prisen, antall på lager, beskrivelse og brukeranmeldelser (ratings). Mer om dette i “Hvordan løse oppgavene”-paragrafen, lenger ned. 

Kodefunksjonaliteten du skal skrive tar utgangspunkt i tre kodefiler; webshop.py, wallet.py og webshop_frontend.py. Innholdet av disse filene er inkludert i denne PDF-filen: Oblig 5 - Case 1 - Predefinert kode.pdf

Download Oblig 5 - Case 1 - Predefinert kode.pdf

Av disse, er webshop.py den viktigste og inneholder funksjonsdefinisjoner du skal fylle ut i de forskjellige oppgavene, samt et par forhåndsdefinerte funksjoner du står fritt til å benytte i kodeløsningene dine. 

Filen wallet.py inneholder klassen Wallet, som simulerer en lommebok. Enkelte av oppgavene du skal løse simulerer varekjøp. I disse tilfellene skal du ta utgangspunkt i objekter av denne klassen for “pengehåndtering”.   

Filen webshop_frontend.py demonstrerer et scenario basert på et eksempel-vareregister (all_wares-variabelen) og funksjonene du skal implementere i webshop.py.  Benytt denne filen for å danne et bilde av hvordan funksjonene du skal skrive skal brukes og henger sammen.   

Hvordan løse oppgavene 

Når du løser oppgavene, ta utgangspunkt i at vareregisteret du skal skrive funksjonalitet rundt følger samme struktur som all_wares-variabelen i webshop_frontend.py.  Ta også utgangspunkt i at "ware"-parameteren, som er satt opp i en del av funksjonene i webshop.py, er en direkte referense til en gitt vare. Altså en av de indre dictionary-elementene i all_wares. Et eksempel på dette kan være:

{

    "name": "AMD Ryzen 9 5900X Processor",

    "price": 5590.0,

    "number_in_stock": 50,

    "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],

    "description": "All the cores and threads you'll need!"

}


Som nevnt tidligere, er oppgavene basert på å fylle ut en rekke funksjonsdefinisjoner som det finnes en oversikt over i webshop.py. Angående disse funksjonene, har mange av disse ferdigdefinerte parametere som du skal ta utgangspunkt i. Du kan likevel modifisere disse parameterne og/eller legge til flere. Du kan også anta at verdiene som blir sendt inn med disse parameterne samsvarer med det som er å forvente. For eksempel, hvis en parameter skal ta et heltall for å representere et antall varer, kan du anta at denne verdien alltid vil være et heltall og aldri negativt.

webshop.py inneholder et par forhåndsdefinerte funksjoner. Du står fritt til å benytte disse der du føler det naturlig. Det er lov, og oppfordres til, å benytte funksjoner du har skrevet i tidligere oppgaver av Del 3. Hver oppgave er likevel uavhengig av hvordan du har løst tidligere oppgaver. Med andre ord, kan du benytte tidligere funksjoner, selv om du ikke har løst de relevante tidligere oppgavene. Du trenger heller ikke å definere disse funksjonene på nytt. Det holder med å kalle funksjonen. 

Du står fritt til å utvide koden med egne funksjoner om du ser et behov for det, men dette er ikke et krav. I motsetning til funksjoner fra tidligere oppgaver; hvis du velger å utvide med egne funksjoner, skal du inkludere definisjonene av disse i alle oppgaver du benytter dem. 

 

Case 1 - Oppgave 1

Skriv en funksjon som printer ut informasjon om en vare på følgende format:

Name: Example Ware
Price: 3999,-
Number in stock: 30
Description: A non-existent ware used only for this example.

Funksjonen skal hete print_ware_information() og skal ta én parameter:

    ware - En varereferanse - dictionary

 

Case 1 - Oppgave 2

Skriv en funksjon som returnerer den gjennomsnittlige ratingen (en float verdi med én desimal) for en gitt vare. Det vil si summen av alle ratingene for denne varen delt på antallet ratinger. Bemerk at hvis listen er tom, vil denne utregningen føre til en ZeroDivisionError.

Funksjonen skal hete calculate_average_ware_rating() og skal ta minst én parameter: 

    ware - En varereferanse - dictionary

 

Case 1 - Oppgave 3

Skriv en funksjon som returnerer en dictionary med alle varer som er på lager. Den returnerte dictionarien skal følge samme format som vareregisteret i webshop_frontent.py (all_wares-variabelen).

Funksjonen skal hete get_all_wares_in_stock() og skal ta minst én parameter: 

    all_wares - Et vareregister – dictionary 

 

Case 1 - Oppgave 4

Skriv en funksjon som returnerer en Boolean-verdi som representerer om et spesifisert antall av en gitt vare finnes på lager. 

Denne funksjonen skal hete is_number_of_ware_in_stock() og skal minst ta to parametere: 

    ware - En varereferanse - dictionary

    number_of_ware - Antallet av denne varen - int  

 

Case 1 - Oppgave 5

Skriv en funksjon som legger til en vare med et gitt antall i en "handlevogn" i form av en dictionary. Ta utgangspunkt i at handlevogn-dictionarien er/skal være på følgende format: 

{

    <varenøkkel 1>: <antall av vare i handlevognen>, 

    <varenøkkel 2>: <antall av vare i handlevognen>,

    etc.

} 

Det skal kontrolleres at antallet av den gitte varen som forsøkes å legges til i handlevognen faktisk er på lager. Hvis det fulle antallet ikke er tilgjengelig, men varen ellers er på lager, skal det tilgjengelige antallet på lager legges til.

Lag fornuftige utskrifter der du mener det kan være nyttig for brukeren å få informasjon om hva som skjer.

Denne funksjonen skal hete add_number_or_ware_to_shopping_cart() og skal ta minst fire parametere: 

    ware_key - En varenøkkel - string
    ware - En varereferanse - dictionary
    shopping_cart - En handlevogn - dictionary
    number_of_ware - Antallet av varen - int (standardverdi skal være 1)

 

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

 

Case 1 - Oppgave 7 (Bonusoppgave)

Skriv en funksjon som sjekker om det er nok penger i en gitt lommebok for å kjøpe en gitt handlevogn. 

Funksjonen skal hete can_afford_shopping_cart(), skal returnere en Boolean verdi, og skal minst ta to parametere: 

    price - Prisen på en handlevogn - float 

    wallet - En lommebok - Wallet-objekt 

 

Case 1 - Oppgave 8 (Bonusoppgave)

Skriv en funksjon som kan benyttes til å kjøpe varene i en handlevogn.  

Funksjonen skal hete buy_shopping_cart() men du kan selv velge hvilke og hvor mange parametere funksjonen skal ta. Hint: Funksjonene i de to tidligere oppgavene er gode indikasjoner.  

Krav: 

    Selv om add_number_of_ware_to_shopping_cart()-funksjonen fra en tidligere oppgave satt et krav på at antallet varer lagt til i handlekurven skal stemme overens med det som er tilgjengelig på lager, er det likevel en mulighet for at andre personer i mellomtiden har kjøpt av disse varene. Varene i handlevognen skal derfor bare kjøpes så langt de er på lager. Handlevognen skal oppdateres ved forsøkt kjøp slik at antallet av hver varetype ikke overstrider det som er tilgjengelig på lageret, samt en varetype skal fjernes fra handlevognen hvis det ikke finnes noen av denne på lager. 

    Transaksjonen skal bare gjelde hvis det er nok penger i lommeboken til å kjøpe hele den oppdaterte handlevognen. Skriv ut en passende melding basert på resultatet av kjøpsforsøket, oppdater antallet på lager av de kjøpte varene i vareregisteret og tøm eventuelt handlevognen. 

    Ha med passende utskrifter der du mener det er naturlig.

 

Case 1 - oppgave 9 (bonusoppgave)

Lag et passende GUI der du forsøker å presentere funksjonaliteten du har laget for nettbutikken i de foregående oppgavene.

 

 
Case 2 - Bilsalg og -utleie

Vi utvikler et system for en oppdragsgiver, BilligBil A/S. Vi har nettopp begynt utviklingen og vi jobber med å få på plass kjernefunksjonalitet. Det skal selges og leies brukte og nye biler, og du skal implementere noen av funksjonene det vil bli behov for å ha.

Relevant for oppgavene er innholdet av denne PDF-filen: Oblig 5 - Case 2 - Predefinert kode.pdf

Download Oblig 5 - Case 2 - Predefinert kode.pdf

    car_dealership.py - inneholder:
        funksjonsdefinisjonene og annen kode du skal ta utgangspunkt i
        Implementasjon av main som illustrerer bruken av funksjonene du skal implementere
    car_dealership output - gir outputen du ville fått ved kjøring av main-metoden
    date dokumentasjon - utdrag av dokumentasjonen for date-klassen du potensielt vil ha nytte av i noen av funksjonene 
    del 3 - repetert oppgavetekst - denne teksten er repetert i det vedlagte dokumentet

Dette Caset består av 7 oppgaver som er er basert på å fylle ut en rekke funksjonsdefinisjoner. Disse funksjonene har ferdigdefinerte parametere du skal ta utgangspunkt i. Du kan likevel modifisere disse parameterne og/eller legge til flere. Du kan også anta at verdiene som blir sendt inn med disse parameterne samsvarer med det som er å forvente. For eksempel, hvis en parameter skal ta et heltall for å representere kilometerstand, kan du anta at denne verdien alltid vil være et heltall og aldri negativt.

Ta utgangspunkt i at car-parameteren, som er satt opp i en del av funksjonene i car_dealershop.py, er en direkte referense til en gitt bil. Altså en av de indre dictionary-elementene i car_register. Et eksempel på dette kan være:

{

            "brand": "Toyota",

            "model": "Corolla",

            "price": 96_000,

            "year": 2012,

            "month": 8,

            "new": False,

            "km": 163_000

}

Du står fritt til å utvide koden med egne funksjoner om du ser et behov for det. I motsetning til funksjoner fra andre oppgaver; Hvis du velger å utvide med egne funksjoner, skal du inkludere definisjonene av disse i alle oppgaver du benytter dem. 

 

Case 2 - Oppgave 1

Implementer funksjonen print_car_information() som printer ut informasjon om en bil på følgende format:

Brand: Toyota
Model: Corolla
Price. 96000,-
Manufactured: 2012-8
Condition: Used

 

Case 2 - Oppgave 2

Implementer funksjonen create_car() som tar forskjellig informasjon om en bil som parametere. Denne skal lage en dictionary for en bil med korrekte nøkkelverdier slik som beskrevet i Case-beskrivelsen, legger den inn i registeret og returner til slutt bil-dictionaryen.

 

Case 2 - Oppgave 3

Implementer funksjonen get_car_age() som returnerer bilens alder fra inneværende år. F.eks. Hvis bilen er fra 2019, og inneværende år er 2022, er bilen 3 år (vi bryr oss ikke om måned).

 

Case 2 - Oppgave 4

Implementer funksjonen rent_car_monthly_price() som returner månedsprisen for å leie en bil (prisen skal være avrundet til 2 desimaler). Den årlige prisen er 40% av totalprisen av bilen. Hvis bilen er ny, skal det også legges til en påslag på 1000kr i måneden.

 

Case 2 - Oppgave 5

Implementer funksjonen next_eu_control() som returnerer et dato-objekt for neste EU-kontroll. EU-kontrollen skal skje hver 2. år, fra året og måneden bilen ble produsert. Det er OK om man setter den 1. i måneden i dato-objektet man returnerer.

 

Case 2 - Oppgave 6

Implementer funksjonen calculate_total_price() som returnerer totalprisen til bilen. I dette systemet er totalprisen prisen på bilen pluss en avgift. Avgiften for nye biler er 10783kr uavhengig av alder på bilen. Er bilen en bruktbil gis avgiften basert på tabellen under.
Alder på bil 	Avgift i kr
0-3 	6681
4-11 	4034
12-29 	1729
30+ (veteran) 	0

Forsøk å gjøre data fra denne tabellen gjenbrukbar.

 

Case 2 - Oppgave 7

Basert på informasjonen om en bil som finnes i car_register-dictionarien, lag en klasse som skal kunne holde på informasjonen om en bil isteden.

Legg også til metode-definisjonene (ikke implementasjon) for de funksjonene som er definert i del 3 av eksamen, som du mener kunne passe inn i denne klassen isteden. Begrunn kort hvorfor.

 

Case 2 - Oppgave 8 (Bonusoppgave)

Lag et passende GUI der du forsøker å presentere funksjonaliteten du har laget for BilligBil i de foregående oppgavene.
