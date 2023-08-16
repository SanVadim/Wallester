import pytest
from conftest import api_endpoints, post_request
from utilities import check_response, check_message_response
import json

with open('test_data\\user_data.json') as json_file:
    user_data = json.load(json_file)

# API 7: POST To Verify Login with valid details
@pytest.mark.parametrize('data', user_data)
def test_post_to_verify_login_with_valid_data(post_request, api_endpoints, data):
    #user_data = create_user(post_request, api_endpoints)
#    data = { 'email': user_data['email'],
#             'password': user_data['password']
#    }
    response = post_request(api_endpoints['verify_login_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 200, 'User exists!')
    #delete_user(delete_request, api_endpoints, user_data)