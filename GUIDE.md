# Guide til brug af den nye Dikutal

Dette er en guide til hvordan man bruger den nye Dikutal.  Guiden er ikke færdig
(for siden er ikke færdig).


## Kalender

I den gamle Dikutal kunne man oprette en begivenhed og så forfremme den til
forsiden.  På den nye Dikutal er det simplere: Man laver altid en artikel, og
hvis den artikel dækker en begivenhed på en bestemt dato, tilføjer man et link i
kalenderen til artiklen.  Kalenderen kan også indeholde links til andet end
artikler på Dikutal hvis det er relevant.

Når man laver en artikel kan man sætte datoer.  Vi kan nok lave noget der
automatisk indsætter det i kalenderen.


## Brugeroprettelse

Man kan ikke selv oprette en bruger på Dikutal.  Det er ikke meningen at særligt
mange mennesker skal oprette brugere.  Kun DIKU-relevante folk der vil oprette
artikler og jobfolk der vil oprette jobs skal have brugere på Dikutal.  Andre
folk der bruger Dikutal skal kun kunne lave kommentarer og behøver ikke brugere.

For at få en bruger sender man en e-mail til dikutal@diku.dk, eller vi tilbyder
folk at give dem brugere.  Når en person har fået en bruger, sender vi
instruktioner til brug af Dikutal.


### Nyt løsen

I instruktionerne skal bl.a. stå at de kan få et nyt løsen hvis de har glemt
deres gamle, ved at gå ind på
[http://dikutal.dk/accounts/password/reset/](). TODO dette skal gøres simplere


## Integration med DIKU Q&A

Der er ingen integration med DIKU Q&A.  Den eneste gode grund til at integrere
med Q&A ville være at folk der har brugere på Q&A kunne lave autentificerede
kommentarer på Dikutal.  Vi prøvede lidt at integrere, men det viste sig at være
for bøvlet.  Desuden har vi set på den gamle Dikutal at folk ikke laver specielt
mange kommentarer, og egentlig ønsker vi også at reel diskussion skal foregå på
Q&A.  At autentificering på kommentarlavning ikke er normalt betyder måske også at
folk der ikke er på Q&A er mere villig til at komme med en relevant kommentar
end hvis registrering var mere normalt.

Hvis nogen på et tidspunkt alligevel får lyst til at prøve at integrere med Q&A,
er følgende oplysninger nok nyttige:

* Dikutal bruger Djangos indbyggede django.contrib.auth til brugerhåndtering.
  OSQA gør vist det samme, men 'auth_*-tabellerne i hver database er nok det
  eneste de har tilfælles, så integrering den vej er nok lidt bøvlet.
* OSQA har nogle klasser i "forum/actions/user.py" hvori man fx kan tilføje kald
  når en bruger oprettes eller brugerinformation ændres.  Dikutal har scriptet
  "bin/import_user.py" der kan tilføje en bruger til Dikutal. Man kunne fx kalde
  dette script fra de ovennævnte klasser.
