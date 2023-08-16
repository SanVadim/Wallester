import pytest
from conftest import api_endpoints, delete_request
from utilities import check_response, check_message_response
import json


with open('test_data\\user_data.json') as json_file:
    user_data = json.load(json_file)

# API 12: DELETE METHOD To Delete User Account
@pytest.mark.parametrize('data', user_data)
def test_delete_user(data, delete_request, api_endpoints):
    response = delete_request(api_endpoints['delete_account_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 200, 'Account deleted!')