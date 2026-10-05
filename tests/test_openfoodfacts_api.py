from unittest.mock import patch, Mock

from services.openfoodfacts import get_product_by_barcode


def test_get_product_by_barcode():
    mock_response = Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "product": {
            "product_name": "Nutella",
            "code": "3017624010701",
            "brands": "Ferrero"
        }
    }

    with patch(
        "services.openfoodfacts.requests.get",
        return_value=mock_response
    ):
        result = get_product_by_barcode("3017624010701")

    assert result == {
        "name": "Nutella",
        "barcode": "3017624010701",
        "brand": "Ferrero"
    }


def test_get_product_by_barcode_not_found():
    mock_response = Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "product": {}
    }

    with patch(
        "services.openfoodfacts.requests.get",
        return_value=mock_response
    ):
        result = get_product_by_barcode("9999999999999")

    assert result is None

def test_get_product_by_barcode_request_failed():
    mock_response = Mock()

    mock_response.status_code = 404

    with patch(
        "services.openfoodfacts.requests.get",
        return_value=mock_response
    ):
        result = get_product_by_barcode("3017624010701")

    assert result is None