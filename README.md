# bugge
Minimalt webrammeverk for snauweb. For bruk med Common Gateway Interface (CGI), da dette er det enkleste å sette opp på Samfundet sine servere.
Inspirert av Flask, både fordi Flask funker bra, og for å gjøre eventuell migrering til Flask og Web Server Gateway Interface (WSGI) enklere.
Rammeverket eksponerer en API-klasse som gir tilgang på nødvendig funksjonalitet

## Må kunne
* Lese konfigurasjonsfil
* Lese miljøvariabler
* Route
* Lese URL-parameter
* Tolke og sanitere URL-parameter
* Gjøre databaseforespørsler gjennom en wrapper
* Returnere gyldig HTML
* Returnere gyldig JSON
* Returnere feilmeldinger

### Lese konfigurasjonsfil
For å gjøre det enklest mulig å holde passord til database og sånt ute av git-repoet så krever rammeverket at alt av sensitiv informasjon ligger i en konfigurasjonsfil som kan (SKAL!) legges uttafor git-mappa. Konfigurasjonsfila består av nøkkel-verdi-par som igjen er separert med linjeskift. Mellomrom og tabs ignoreres. Linjer som begynner med "#" er kommentarer og ignoreres av parseren
