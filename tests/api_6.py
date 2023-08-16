from conftest import api_endpoints, post_request
from utilities import check_response, check_message_response

# API 6: POST To Search Product without search_product parameter
def test_post_to_search_product_without_parameter(post_request, api_endpoints):
    response = post_request(api_endpoints['search_product_path'])
    check_response(response, 200)
    check_message_response(response.json(), 400, "Bad request, search_product parameter is missing in POST request.")