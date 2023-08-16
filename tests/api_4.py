from conftest import api_endpoints, post_request
from utilities import check_response, check_message_response

# API 4: PUT To All Brands List
def test_put_to_all_brands_list(post_request, api_endpoints):
    response = post_request(api_endpoints['brands_list_path'])
    check_response(response, 200)
    check_message_response(response.json(), 405, 'This request method is not supported.')
