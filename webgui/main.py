from flask import Flask, render_template, request, make_response, session, flash
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
import authomatic
import logging
from dnszone import *
from mongo_functions import *
from config import CONFIG


# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)

dnsmang = DnsZone("cli.test","192.168.37.132")
app = Flask(__name__, template_folder='templates')
app.secret_key = "21341r23232"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()
            add_user(result.user.name,result.user.email,result.user.id)

            session['email'] = result.user.email
            session['result'] = {
            'provider_name': result.provider.name,
            'user_id': result.user.id,
            'user_email': result.user.email,
            'user_name': result.user.name,
            'error': None
        }

        # The rest happens inside the template.
        return render_template('login.html', result=result)

    # Don't forget to return the response.
    return response

@app.route('/login/google/add_a_record/', methods=['post'])
def add_a_record():
    #via post krijg je de naam van de machine binnen.
    input_fqdn = request.form['fqdn']
    #Hier wordt de FQDN gemaakt
    dnsname = input_fqdn + ".cli.test"
    #Via post krijg je de IP address binnen
    ip = request.form['ipv4']
    #Toevoegen van de A record met de bijhorende gegevens
    dnsmang.add_address(fqdn=dnsname,ipv4=ip)
    #Toevoegen door wie de wijziging is gebeurd aan MongoDB.
    email = session.get('email')
    time_change_FQDN(dnsname, ip, email)
    #Sessie binnenhalen
    result = session.get('result')
    flash(f"record voor {dnsname} met IP-adres {ip} is toegevoegd")
    
    return render_template('login.html', result=result)

@app.route('/login/google/edit_a_record/', methods=['post'])
def edit_a_record():
    dnsname = request.form['fqdn'] + ".cli.test"
    ip = request.form['ipv4']
    dnsmang.update_address(fqdn=dnsname,ipv4=ip)
    email = session.get('email')
    time_change_FQDN(dnsname, ip, email)
    #Sessie binnenhalen
    result = session.get('result')

    return render_template('login.html', result=result)

@app.route('/login/google/delete_a_record/', methods=['post'])
def delete_a_record():
    dnsname = request.form['fqdn'] + ".cli.test"
    dnsmang.clear_address(fqdn=dnsname)
    email = session.get('email')
    change_action_delete(dnsname, email)
    #Sessie binnenhalen
    result = session.get('result')

    return render_template('login.html', result=result)

# Run the app on port 5000 on all interfaces, accepting only HTTPS connections
if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc', host='192.168.37.132', port=5000)
