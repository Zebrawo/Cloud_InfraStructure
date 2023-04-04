# Cloud_InfraStructure Project voor school

Project voor het vak CLI

## Inleiding
Dit is de beschrijving van de eindopdracht van het vak “Cloud Infrastructure and Management”. Als je
alle weekopdrachten hebt gedaan, dan heb je voldoende kennis denken we om al deze kennis te
integreren. Onderschat het niet, dit gaat je veel tijd en energie kosten denken wij dus begin op tijd!
We gaan ervan uit dat je in tweetallen werkt, maar het is mogelijk om alleen te werken, zie hiervoor het
beoordelingsformulier. Het precieze oplevermoment vind je terug bij de opdrachten van Canvas.
Veel Succes toegewenst!
Docententeam “Cloud Infrastructure and Management”

## Case omschrijving
Stel je bedrijf heeft een eigen domein en wil een website hosten vanachter de Ziggo- of KPN-router van
het bedrijf(je) waar je werkt. Je zet port forwarding aan op de router en koppelt www.<jouwdomain>
aan je publieke IP-adres. Daarna kan de hele wereld via de domeinnaam bij de website. Goed geregeld,
toch? Niet helemaal, want het publieke IP-adres kan veranderen en als dat gebeurt moet je de DNS ook
aanpassen, logisch! Dat kan handmatig, maar deze aanpassing kan ook automatisch gerealiseerd
worden middels Dynamic DNS (DDNS). Een voorbeeld van een DDNS-provider is DuckDNS
(https://www.duckdns.org ).

Jouw werkgever heeft stevig last van ‘not invented here syndrome’ en wil geen gebruik maken van een
bestaande DDNS-dienst, maar wil wel over de functionaliteit kunnen beschikken. Dit kan niet op eigen
servers draaien, dus zal er een oplossing gemaakt moeten worden die in de cloud kan worden gezet. In
deze opdracht vragen we jullie hiervoor zelf een mooie cloudoplossing te maken. Echt een CSC-klus dus.
De wens bestaat dat jullie een -eenvoudige-, maar schaalbare website maken in een cloud (public of
private). De website moet worden beveiligd via externe authenticatie. Als je als gebruiker bent ingelogd
kan je vervolgens via deze website een nieuw DNS-record in je domein aanmaken, verwijderen of
vervangen (replace). Dat lijkt heel moeilijk, maar er is een Python module die je daarbij goed kan helpen.
De website is gekoppeld aan een NoSQL-database waarin informatie over jou en/of jouw acties wordt
opgeslagen.

Leuk dat dit kan via een website, maar we willen dit uiteindelijk automatiseren dus hebben we een API
nodig waarmee je ook records kan aanmaken, verwijderen of vervangen. Een beetje vergelijkbaar dus
met: http://www.duckdns.org/

## Directories
- webgui: Folder met behorende python & html files voor het project.
- dnsapi: Folder met behorden python code voor het gebruik van REST api's
