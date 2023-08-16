import pytest
from conftest import api_endpoints, post_request
from utilities import check_response, check_message_response
import json

with open('test_data\\user_data.json') as json_file:
    user_data = json.load(json_file)

# API 11: POST To Create/Register User Account
@pytest.mark.parametrize('data', user_data)
def test_post_to_create_user(data, post_request, api_endpoints):
    response = post_request(api_endpoints['create_account_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 201, 'User created!')

with open('test_data\\user_data_negative.json') as json_file:
    user_data_negative = json.load(json_file)

# API 11.1: POST When registering an account, do not enter any requested data
@pytest.mark.parametrize('data', user_data_negative)
def test_post_to_create_user(data, post_request, api_endpoints):
    response = post_request(api_endpoints['create_account_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 400, 'Email already exists!')

    # API 11.2: POST When registering, enter an existing user
@pytest.mark.parametrize('data', user_data_negative)
def test_post_to_create_user(data, post_request, api_endpoints):
    response = post_request(api_endpoints['create_account_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 400, 'Email already exists!')

# API 11.3: POST When registering, specify only email (unregistered email)
@pytest.mark.parametrize('data', user_data_negative)
def test_post_to_create_user(data, post_request, api_endpoints):
    response = post_request(api_endpoints['create_account_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 400, 'Email already exists!')

# API 11.4: POST When registering, specify only password
@pytest.mark.parametrize('data', user_data_negative)
def test_post_to_create_user(data, post_request, api_endpoints):
    response = post_request(api_endpoints['create_account_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 400, 'Email already exists!')