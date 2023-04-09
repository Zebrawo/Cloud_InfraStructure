from flask import Flask, render_template, request, make_response, session, flash
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
import authomatic
from dnszone import *
from mongo_functions import *
from config import CONFIG
import os

#bindserver_ip = os.environ.get('BINDSERVER_IP')

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)

#Kubernetes containers krijgen dynamisch ip altijd.


dnsmang = DnsZone("cli.test","10.224.0.113")
app = Flask(__name__, template_folder='templates')
app.secret_key = "21341r23232"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    # We hebben een response object nodig voor Werkzeugner
    response = make_response()
    # Log de gebruiker in, geef hem de adapter en de providernaam door.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    # Als er geen LoginResult-object is, is de aanmeldingsprocedure nog in behandeling.
    if result:
        if result.user:
            # We moeten de gebruiker update voor meer informatie
            result.user.update()
            # Voeg de gebruiker toe aan de MongoDB
            add_user(result.user.name,result.user.email,result.user.id)
            
            #Zet gegevens vast in Session zodat we deze herkunnen gebruiken
            session['email'] = result.user.email
            session['result'] = {
            'provider_name': result.provider.name,
            'user_id': result.user.id,
            'user_email': result.user.email,
            'user_name': result.user.name,
            'error': None
        }

        # De rest gebeurd in de template
        return render_template('login.html', result=result)

    # Vergeet niet het antwoord terug te sturen
    return response

#Route voor het toevoegen van een A Record
@app.route('/login/google/add_a_record/', methods=['post'])
def add_a_record():
    # variable maken met input van de form van de website met behulp van post
    dnsname = request.form['fqdn'] + ".cli.test"
    ip = request.form['ipv4']
    # Toevoegen van de A record met de bijhorende gegevens
    dnsmang.add_address(fqdn=dnsname,ipv4=ip)
    # Toevoegen door wie de wijziging is gebeurd aan MongoDB.
    email = session.get('email')
    time_change_FQDN(dnsname, ip, email)
    # Sessie binnenhalen
    result = session.get('result')
    # Weergeven op de website dat de A record is toegevoegd
    flash(f"record voor {dnsname} met IP-adres {ip} is toegevoegd")

    return render_template('login.html', result=result)

# Route voor het aanpassen van de A Record
@app.route('/login/google/edit_a_record/', methods=['post'])
def edit_a_record():
    # variable maken met input van de form van de website met behulp van post
    dnsname = request.form['fqdn'] + ".cli.test"
    ip = request.form['ipv4']
    # Het aanpassen van de A record met de bijbehorende gegevens
    dnsmang.update_address(fqdn=dnsname,ipv4=ip)
    # Sessie data binnenhalen zodat we de pagina statisch kunnen houden
    email = session.get('email')
    # Opslaan van de wijziging in MongoDB
    time_change_FQDN(dnsname, ip, email)
    # Sessie binnenhalen
    result = session.get('result')
    # Weergeven op de website dat de A record is aangepast
    flash(f"record voor {dnsname} met IP-adres {ip} is aangepast")

    return render_template('login.html', result=result)

# Route voor het verwijderen van een A Record
@app.route('/login/google/delete_a_record/', methods=['post'])
def delete_a_record():
    # Variable aanmaken met input vanuit de website met behulp van post
    dnsname = request.form['fqdn'] + ".cli.test"
    dnsmang.clear_address(fqdn=dnsname)
    # Sessie data binnen halen
    email = session.get('email')
    # Wijziging opslaan in database
    change_action_delete(dnsname, email)
    # Sessie binnenhalen
    result = session.get('result')
    # Weergeven op de website dat de A record is verwijderd
    flash(f"record voor {dnsname} is verwijderd")

    return render_template('login.html', result=result)

# Run the app on port 5000 on all interfaces, accepting only HTTPS connections
if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc', host='0.0.0.0', port=5000)
