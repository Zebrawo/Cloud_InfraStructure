# Flask Authomatic DNS Management Application

This is a simple Flask application that allows users to manage DNS records on a local DNS server via a web interface. Users can log in using OAuth2 authentication with their Google account and add, edit, or delete DNS records for the specified domain.

## Installation

To run this application, you need to have Python 3.x and Flask installed on your machine. You can install Flask using pip:
```bash
pip install flask
```
you also need to install Authomatic and pymong libraries
```bash
pip install authomatic pymongo
```
## Usage

To use the application, simply run the "main.py" file:
```bash
python main.py
```
Then navigate to https://<IP-Address>.nip.io:5000 in your web browser to access the application. Note that the application is using an "nip.io" in the link. nip.io is just deadsimple a wildcard dns.

Once logged in with your Google Account or Amazon, you can add, edit or delete DNS records for the specified domain.

## Dependencies

This application relies on the following Python libraries

- Flask
- Authomatic
- pymongo
- dnspython

## Files

- main.py: The main application file containing the Flask routes for login and DNS management.
- config.py: Configuration file containing the OAuth2 authentication settings for Google
- mongo_functions.py: File containing MongoDB functions for logging DNS management actions & adding users
- dnszone.py: File containing classes for handling DNS zone file manipulation
- templates/: Folder containing HTML templates for the application

## Routes

- /: Home page of the application. Displays the logo and the login options
- /login/<provider_name>/: OAuth2 login page for the specified provider (in this case, google).
- /login/<provider_name>/add_a_record/: Route for adding a DNS A record.
- /login/<provider_name>/edit_a_record/: Route for editing a DNS A record.
- /login/<provider_name>/delete_a_record/: Route for deleting a DNS A record.
