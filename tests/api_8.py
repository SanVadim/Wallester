from conftest import api_endpoints, post_request
from utilities import check_response, check_message_response, random_string

# API 8: POST To Verify Login without email parameter
def test_post_to_verify_login_without_email(post_request, api_endpoints):
    data = {'password': random_string()}
    response = post_request(api_endpoints['verify_login_path'], data)
    check_response(response, 200)
    check_message_response(response.json(), 400, 'Bad request, email or password parameter is missing in POST request.')