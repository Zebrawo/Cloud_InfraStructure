# DNS API

Dit is een voorbeeldimplementatie van een RESTful api voor het beheren van DNS-records. Het maakt gebruik van de 
Flask-webapplicatie en Flask-RESTful-extensie om de API te definiëren en te implementeren.

## Vereisten

- Python 3.x
- Flask
- FLask-RESTful
- uuid

## Installatie

1. Clonde de repository naar uw lokale machine.
2. Installeer de vereiste afhankelijkheden met behulp van pip: 
```bash
pip install flask flask-restful uuid dnspython
```
3. Voor de toepassing uit met het volgende commando:
```bash
python dns_api.py
```

## API-eindpunten
- 'GET /dns/<string:fqdn>' - Haalt het IP-adres op voor het opgegeven domein.
- 'PUT /dns/<string:fqdn>' - Bij werken van het IP-adres voor het opgegeven domein.
- 'DELETE /dns/<string:fqdn' - Verwijdert het IP-adres voor het opgegeven domein. 

## Authenticatie

Alle-eindpunten vereisen authenticatie met een geldig token dat is verkregen via het 'PUT /token'-eindpunt. het gegenereerde
token moet worden verzonden als een header `Authorization` met de `bearer`-prefix

## Voorbeeld run

Als eerst start je de REST_api applicatie op:
```bash
python dns_api.py
```

Daarna vraag je om een token:
```bash
curl -X POST http://<URL:PORT>/token
```

Als je de token hebt gekregen dan kan je bijvoorbeeld een A Record toevoegen en of aanpassen
```bash
curl -X PUT -H "Authorization: 27a130c3-7ae7-4322-bff1-1c202052db52" -H "Content-Type: application/json" -d '{"ipv4": "192.168.1.100"}' http://192.168.37.132:5000/dns/test4.cli.test
```

Als je een A Record wilt verwijderen:
```bash

```




