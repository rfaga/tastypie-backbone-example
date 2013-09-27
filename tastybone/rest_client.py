#!/usr/bin/env python

#
# install tastypie_client lib with PIP, with this command on Linux:
# pip install -e git+https://github.com/rfaga/tastypie-client#egg=tastypie_client
#

from tastypie_client import Api

BASE_URL = 'http://localhost:8000/api/'

# username, password
AUTH = ('teste', 'teste')

### Starting the code
operation_api = Api(BASE_URL + 'operation', auth=AUTH)
operations = operation_api.get_endpoints()

print operations['objects']
