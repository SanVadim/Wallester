from conftest import get_request, api_endpoints
from utilities import check_response

# API 3: Get All Brands List
def test_get_all_brands_list(get_request, api_endpoints):
    response = get_request(api_endpoints['brands_list_path'])
    check_response(response, 200)
    response_data = response.json()
    assert 'responseCode' in response_data, "No 'responseCode' key in the response"
    assert response_data['responseCode'] == 200, "'responseCode' is not 200"
    assert 'brands' in response_data, "No 'brands' key in the response"
    assert response_data['brands'], "'brands' list is empty"
    for brand in response_data['brands']:
        assert 'id' in brand, "No 'id' key in brand"
        assert 'brand' in brand, "No 'brand' key in brand"