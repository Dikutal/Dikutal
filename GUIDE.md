# Guide til den nye Dikutal

Dette er en guide til hvordan man bruger den nye Dikutal, hvordan den hænger
sammen, og hvorfor den er som den er.  Guiden er ikke færdig (for siden er ikke
færdig).


## Integration med DIKU Q&A

Der er ingen integration med DIKU Q&A.  Den eneste rigtig gode grund til at
integrere med Q&A ville være at folk der har brugere på Q&A kunne lave
autentificerede kommentarer på Dikutal.  Vi prøvede lidt at integrere, men det
viste sig at være for bøvlet.

Hvis nogen på et tidspunkt alligevel får lyst til at prøve at integrere med Q&A,
er følgende oplysninger nok nyttige:

* Dikutal bruger Djangos indbyggede django.contrib.auth til brugerhåndtering.
  OSQA gør vist det samme, men 'auth_*-tabellerne i hver database er nok det
  eneste de har tilfælles, så integrering den vej er nok lidt bøvlet.
* OSQA har nogle klasser i "forum/actions/user.py" hvori man fx kan tilføje kald
  når en bruger oprettes eller brugerinformation ændres.  Dikutal har scriptet
  "bin/import_user.py" der kan tilføje en bruger til Dikutal. Man kunne fx kalde
  dette script fra de ovennævnte klasser.
