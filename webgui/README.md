Introductie
Dit is een Flask-applicatie die gebruikt wordt om DNS-records toe te voegen, wijzigen en verwijderen. De applicatie gebruikt Authomatic om gebruikers in te laten loggen via OAuth2.

Gebruik
Voer het bestand app.py uit om de applicatie te starten. De applicatie draait op poort 5000 en gebruikt SSL om veilige verbindingen mogelijk te maken.

De startpagina is te bereiken via https://<ip-adres>:5000/. Hier kan de gebruiker inloggen met behulp van OAuth2 door op de link van de gewenste provider te klikken.

Als de gebruiker is ingelogd, wordt hij doorgestuurd naar de /login/<provider_name>/-route. Hier kan de gebruiker nieuwe DNS-records toevoegen, bestaande wijzigen en/of verwijderen.

Vereisten
De applicatie vereist Python 3.8 of hoger en de volgende modules:

Flask
authomatic
pymongo
Configuratie
De configuratie voor Authomatic staat in het bestand config.py. Hierin moeten de gegevens van de OAuth2-provider(s) worden ingevoerd.

De MongoDB-database wordt gebruikt om wijzigingen in de DNS-records bij te houden. De databasegegevens worden ingevoerd in mongo_functions.py.

De DNS-zone wordt geconfigureerd in het bestand dnszone.py. Hierin moeten de gegevens van de zone worden ingevoerd.
