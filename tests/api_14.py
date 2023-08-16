from conftest import api_endpoints, post_request, get_request, put_request
from utilities import check_response, check_message_response, random_string, get_user
import random
import json

with open('test_data\\user_data.json') as json_file:
    user_data = json.load(json_file)

# API 14: GET user account detail by email
def test_get_user_by_email(get_request, api_endpoints):
    user = random.choice(user_data)
    original_user = user.copy()
    response = get_user(get_request, api_endpoints, original_user)
    response_data = response.json()
    print(response_data)
    check_response(response, 200)
    user = response_data['user']
    assert user['birth_day'] == original_user['birth_date']
    assert user['first_name'] == original_user['firstname']
    assert user['last_name'] == original_user['lastname']

    for key in original_user:
        if key not in ['password', 'mobile_number', 'birth_day', 'birth_date','firstname', 'lastname']:
            assert original_user[key] == user[key]