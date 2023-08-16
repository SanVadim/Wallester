from conftest import api_endpoints, post_request, get_request, put_request
from utilities import check_response, check_message_response, random_string, get_user
import random
import json

with open('test_data\\user_data.json') as json_file:
    user_data = json.load(json_file)

# API 13: PUT METHOD To Update User Account
def test_put_to_update_user(put_request, post_request, get_request, api_endpoints):
    user = random.choice(user_data)
    original_user = user.copy()
    print(user)

    user['city'] = random_string(15)
    user['zipcode'] = str(random.randint(10000000, 99999999))

    response = put_request(api_endpoints['update_account_path'], user)
    check_response(response, 200)
    check_message_response(response.json(), 200, 'User updated!')

    response = get_user(get_request, api_endpoints, original_user)
    updated_user = response['user']
    print(updated_user)
    assert updated_user['city'] == user['city']
    assert updated_user['zipcode'] == user['zipcode']
    assert updated_user['birth_day'] == user['birth_date']
    assert updated_user['first_name'] == user['firstname']
    assert updated_user['last_name'] == user['lastname']

    for key in original_user:
        if key not in ['city', 'zipcode', 'password', 'mobile_number', 'birth_day', 'birth_date','firstname', 'lastname']:
            assert original_user[key] == updated_user[key]

# API 13.1: PUT When updating your account, enter an unregistered email (all other fields are filled)
def test_put_to_update_unrigistered_user(put_request, post_request, get_request, api_endpoints):
    user = random.choice(user_data)
    user['email'] = random_string(15) + '@test.com'
    response = put_request(api_endpoints['update_account_path'], user)
    check_response(response, 200)
    check_message_response(response.json(), 404, 'Account not found!')

# API 13.2: PUT When updating your account, enter an existing email, but enter the wrong password (all other fields are filled)
def test_put_to_update_user_wrong_password_(put_request, post_request, get_request, api_endpoints):
    user = random.choice(user_data)
    user['password'] = random_string(10)
    response = put_request(api_endpoints['update_account_path'], user)
    check_response(response, 200)
    check_message_response(response.json(), 404, 'Account not found!')