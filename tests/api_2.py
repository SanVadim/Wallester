from conftest import get_request, api_endpoints, post_request, delete_request, put_request
from utilities import check_response, check_message_response

# API 2: POST To All Products List
def test_post_to_all_products_list(post_request, api_endpoints):
    response = post_request(api_endpoints['product_list_path'])
    check_response(response, 200)
    check_message_response(response.json(), 405, 'This request method is not supported.')