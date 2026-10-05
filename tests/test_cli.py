from unittest.mock import patch
import copy
import cli
import pytest


@pytest.fixture(autouse=True)
def reset_products():
    original_products = [
        {
        "id": 1,
        "name": "Milk",
        "barcode": "123456789012",
        "price": 100,
        "quantity": 20
        },
        {
        "id": 2,
        "name": "Bread",
        "barcode": "987654321098",
        "price": 70,
        "quantity": 15
        },
        {
        "id": 3,
        "name": "Eggs",
        "barcode": "456789012345",
        "price": 50,
        "quantity": 60
        },
        {
        "id": 4,
        "name": "Nutella",
        "barcode": "3017624010701",
        "price": 650,
        "quantity": 10
        }
    ]
    with patch("cli.products", copy.deepcopy(original_products)):
        yield

def test_show_menu(capsys):
    cli.show_menu()

    captured = capsys.readouterr()

    assert "Inventory Management System" in captured.out
    assert "1. List Products" in captured.out
    assert "7. Exit" in captured.out


def test_list_products(capsys):
    cli.list_products()

    captured = capsys.readouterr()

    assert "Milk" in captured.out
    assert "Bread" in captured.out


def test_get_product(capsys):
    with patch("builtins.input", return_value="1"):
        cli.get_product()

    captured = capsys.readouterr()

    assert "Milk" in captured.out


def test_get_product_not_found(capsys):
    with patch("builtins.input", return_value="999"):
        cli.get_product()

    captured = capsys.readouterr()

    assert "Product not found" in captured.out


def test_add_product(capsys):
    with patch(
        "builtins.input",
        side_effect=["Juice", "150", "111222333444", "10"]
    ):
        cli.add_product()

    captured = capsys.readouterr()

    assert "Product added successfully" in captured.out


def test_update_product(capsys):
    with patch(
        "builtins.input",
        side_effect=["1", "Fresh Milk", "120", "25"]
    ):
        cli.update_product()

    captured = capsys.readouterr()

    assert "Product updated successfully" in captured.out


def test_update_product_not_found(capsys):
    with patch("builtins.input", return_value="999"):
        cli.update_product()

    captured = capsys.readouterr()

    assert "Product not found" in captured.out


def test_delete_product(capsys):
    with patch("builtins.input", return_value="2"):
        cli.delete_product()

    captured = capsys.readouterr()

    assert "Product deleted successfully" in captured.out


def test_delete_product_not_found(capsys):
    with patch("builtins.input", return_value="999"):
        cli.delete_product()

    captured = capsys.readouterr()

    assert "Product not found" in captured.out

def test_search_product(capsys):
    mock_product = {
        "name": "Nutella",
        "barcode": "3017624010701",
        "brand": "Ferrero"
    }

    with patch("builtins.input", return_value="3017624010701"):
        with patch(
            "cli.get_product_by_barcode",
            return_value=mock_product
        ):
            cli.search_product_by_barcode()

    captured = capsys.readouterr()

    assert "Nutella" in captured.out
    assert "Ferrero" in captured.out

def test_search_product_not_found(capsys):
    with patch("builtins.input", return_value="9999999999999"):
        with patch(
            "cli.get_product_by_barcode",
            return_value=None
        ):
            cli.search_product_by_barcode()

    captured = capsys.readouterr()

    assert "Product not found!" in captured.out