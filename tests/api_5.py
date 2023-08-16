import pytest
from conftest import api_endpoints, post_request
from utilities import check_response, check_products_json

# API 5: POST To Search Product
@pytest.mark.parametrize("search_product", ["top", "tshirt", "jean", "dress"])
def test_post_to_search_product(post_request, api_endpoints, search_product):
    data = {"search_product": search_product}
    response = post_request(api_endpoints['search_product_path'], data)
    check_response(response, 200)
    response_data = response.json()
    check_products_json(response_data)
    for product in response_data['products']:
      assert search_product in product['name'].lower() or search_product in product['category']['category'].lower(), f"Product {product['id']} does not contain {search_product} in name or category"