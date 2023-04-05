# Import required modules
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from dnszone import *
import uuid

# Initialize the Flask application
app = Flask(__name__)
# Initialize the Flask-RESTful API
api = Api(app)

# Dictionary to store the tokens
tokens = {}

# Function to generate a token
def generate_token():
    return str(uuid.uuid4())

# Function to verify if a token is valid
def verify_token(token):
    return tokens.get(token) is not None

# Class to handle DNS API requests
class DnsAPI(Resource):
    def __init__(self, dns_zone):
        self.dns_zone = dns_zone

    def get(self, fqdn):
        # Verify the token in the request header
        if not verify_token(request.headers.get('Authorization')):
            return {'error': 'Invalid token'}, 401

        result = self.dns_zone.check_address(fqdn)
        if 'error' in result:
            return result, result.get('error_text', 500)
        return result, 200

    def put(self, fqdn):
        # Verify the token in the request header
        if not verify_token(request.headers.get('Authorization')):
            return {'error': 'Invalid token'}, 401

        parser = reqparse.RequestParser()
        parser.add_argument('ipv4', type=str, required=True, help='IP address is required')
        args = parser.parse_args()

        result = self.dns_zone.update_address(fqdn, args['ipv4'])
        if 'error' in result:
            return result, result.get('error_text', 500)
        return result, 200

    def delete(self, fqdn):
        # Verify the token in the request header
        if not verify_token(request.headers.get('Authorization')):
            return {'error': 'Invalid token'}, 401

        result = self.dns_zone.clear_address(fqdn)
        if 'error' in result:
            return result, result.get('error_text', 500)
        return result, 200

# Class to handle token API requests
class TokenAPI(Resource):
    def post(self):
        token = generate_token()
        tokens[token] = True
        return {'token': token}, 200

# Initialize the DNS zone
dns_zone = DnsZone("cli.test", "192.168.37.132")

# Add the DNS API resource to the API
api.add_resource(DnsAPI, '/dns/<string:fqdn>', resource_class_kwargs={'dns_zone': dns_zone})
# Add the Token API resource to the API
api.add_resource(TokenAPI, '/token')

# Start the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
