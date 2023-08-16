import requests
import pytest

@pytest.fixture
def url():
    return 'https://automationexercise.com'

@pytest.fixture
def api_endpoints(url):
    return {
        'product_list_path': url + "/api/productsList",
        'search_product_path': url + "/api/searchProduct",
        'brands_list_path': url + "/api/brandsList",
        'verify_login_path': url + "/api/verifyLogin",
        'create_account_path': url + "/api/createAccount",
        'delete_account_path': url + "/api/deleteAccount",
        'update_account_path': url + "/api/updateAccount",
        'get_user_by_email_path': url + "/api/getUserDetailByEmail"
    }

@pytest.fixture
def get_request():
    def _get_request(url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params)
        return response
    return _get_request

@pytest.fixture
def post_request():
    def _post_request(url, data=None):
        response = requests.post(url, data=data)
        return response
    return _post_request

@pytest.fixture
def delete_request():
    def _delete_request(url, data=None):
        response = requests.delete(url, data=data)
        return response
    return _delete_request

@pytest.fixture
def put_request():
    def _put_request(url, data=None):
        response = requests.put(url, data=data)
        return response
    return _put_request