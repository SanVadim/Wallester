import pytest
from conftest import get_request, api_endpoints, post_request, delete_request, put_request
import random
import string
import json


def check_headers(headers):
    assert 'Date' in headers
    assert 'Content-Type' in headers
    assert 'Transfer-Encoding' in headers
    assert 'Connection' in headers
    assert 'vary' in headers
    assert 'referrer-policy' in headers
    assert 'x-frame-options' in headers
    assert 'x-content-type-options' in headers
    assert 'allow' in headers
    assert 'x-powered-by' in headers
    assert 'status' in headers
    assert 'CF-Cache-Status' in headers
    assert 'Report-To' in headers
    assert 'NEL' in headers
    assert 'Server' in headers
    assert 'CF-RAY' in headers
    assert 'Content-Encoding' in headers
    assert 'alt-svc' in headers


def check_response(response, expected_code):
    assert response.status_code == expected_code, f"Response code is not {expected_code}"
    check_headers(response.headers)
    assert response.headers['content-type'] == 'text/html; charset=utf-8', "response header 'content-type' is not 'text/html; charset=utf-8'"
    assert response.headers['Server'] == 'cloudflare', "response header 'Server' is not 'cloudflare'"
    assert response.headers['status'] == '200 OK', "response header 'status' is not '200 OK'"
    try:
        assert isinstance(response.json(), dict)
    except ValueError:
        pytest.fail("Response body is not valid JSON")
    assert response.json()

def check_message_response(response_data, expected_code, expected_message):
    assert 'responseCode' in response_data, "No 'responseCode' key in the response"
    assert response_data['responseCode'] == expected_code, f"'responseCode' is not {expected_code}"
    assert 'message' in response_data, "No 'message' key in the response"
    assert response_data['message'] == expected_message, f"'message' is not equal '{expected_message}'"


def check_products_json(response_data):
    assert 'responseCode' in response_data, "No 'responseCode' key in the response"
    assert response_data['responseCode'] == 200, "'responseCode' is not 200"
    assert 'products' in response_data, "No 'products' key in the response"
    assert response_data['products'], "'products' list is empty"
    for product in response_data['products']:
        assert 'id' in product, "No 'id' key in product"
        assert 'name' in product, "No 'name' key in product"
        assert 'price' in product, "No 'price' key in product"
        assert 'brand' in product, "No 'brand' key in product"
        assert 'category' in product, "No 'category' key in product"
        assert 'usertype' in product['category'], "No 'usertype' key in product category"
        assert 'usertype' in product['category']['usertype'], "No 'usertype' key in product category usertype"
        assert 'category' in product['category'], "No 'category' key in product category"

def random_string(size = random.randint(5, 20)):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=size))
    return str(res)

def create_user(post_request, api_endpoints):
    user_num = str(random.randint(123, 4569))
    data = {'name': f'Vadim{user_num}',
            'email': f'Vadim{user_num}@{user_num}.com',
            'password': f'987654321{user_num}',
            'title': 'Mr',
            'birth_date': '15',
            'birth_month': '05',
            'birth_year': '2000',
            'firstname': 'V',
            'lastname': 'S',
            'company': 'Wallester',
            'address1': '3 Vs 123',
            'address2': '',
            'country': 'EST',
            'zipcode': 'L1111',
            'state': 'Harjumaa',
            'city': 'Tallinn',
            'mobile_number': '+37223456789'
    }
    response = post_request(api_endpoints['create_account_path'], data)
    response_data = response.json()
    assert 'responseCode' in response_data, "No 'responseCode' key in the response"
    assert response_data['responseCode'] == 201, "'responseCode' is not 201"
    return data

def save_user_data(user_data, file):
    with open('test_data/user_data_output.json', 'r') as json_file:
        existing_data = json.load(json_file)
    existing_data.append(user_data)
    with open('test_data/user_data_output.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)


def delete_user(delete_request, api_endpoints, user_data):
    data = { 'email': user_data['email'],
             'password': user_data['password']
    }
    response = delete_request(api_endpoints['delete_account_path'], data)
    response_data = response.json()
    assert 'responseCode' in response_data, "No 'responseCode' key in the response"
    assert response_data['responseCode'] == 200, "'responseCode' is not 200"

def get_user(get_request, api_endpoints, user_data):
    data = { 'email': user_data['email']}
    response = get_request(api_endpoints['get_user_by_email_path'], params = data)
    response_data = response.json()
    assert 'responseCode' in response_data, "No 'responseCode' key in the response"
    assert response_data['responseCode'] == 200, "'responseCode' is not 200"
    return response_data