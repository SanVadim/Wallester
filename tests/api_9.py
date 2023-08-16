from conftest import api_endpoints, delete_request
from utilities import check_response, check_message_response

# API 9: DELETE To Verify Login
def test_delete_to_verify_login(delete_request, api_endpoints):
    response = delete_request(api_endpoints['verify_login_path'])
    check_response(response, 200)
    check_message_response(response.json(), 405, 'This request method is not supported.')