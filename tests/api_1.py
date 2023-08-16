from conftest import get_request, api_endpoints
from utilities import check_response, check_products_json

# API 1: Get All Products List
def test_get_all_product_list(get_request, api_endpoints):
    response = get_request(api_endpoints['product_list_path'])
    check_response(response, 200)
    response_data = response.json()
    check_products_json(response_data)