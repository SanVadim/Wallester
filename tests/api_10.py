import pytest
from conftest import api_endpoints, post_request
from utilities import check_response, check_message_response, random_string
import json

# API 10: POST To Verify Login with invalid details
def test_post_to_verify_login_with_invalid_data(post_request, api_endpoints):
    data = { 'email': random_string(20),
             'password': random_string(10)
    }
    response = post_request(api_endpoints['verify_login_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 404, 'User not found!')

#def test_create(post_request, api_endpoints):
#    new_user = create_user(post_request, api_endpoints)
#    save_user_data(new_user)

with open('test_data\\invalid_user_data.json') as json_file:
    invalid_user_data = json.load(json_file)

# API 10.1: POST Login with correct email but incorrect password
@pytest.mark.parametrize('data', invalid_user_data)
def test_post_to_verify_login_with_invalid_data_1(post_request, api_endpoints, data):
    response = post_request(api_endpoints['verify_login_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 404, 'User not found!')

# API 10.2: POST Login with valid email parameter, but don't enter password parameter
@pytest.mark.parametrize('data', invalid_user_data)
def test_post_to_verify_login_with_invalid_data_2(post_request, api_endpoints, data):
    response = post_request(api_endpoints['verify_login_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 404, 'User not found!')