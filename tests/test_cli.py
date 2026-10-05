from unittest.mock import patch
import cli

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

