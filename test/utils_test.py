import pytest
import os
import teradatasql
from unittest import mock
from migration.utils import Utility


def test_get_view_list_negative_no_cursor():
    """Tests the `get_view_list()` method in a negative scenario with no cursor."""
    query = "select view_name from user_views"
    with pytest.raises(Exception):
        Utility.get_view_list(None, query)


def test_get_view_ddl_negative_no_cursor():
    """Tests the `get_view_ddl()` method in a negative scenario with no cursor."""
    view = "my_view"
    with pytest.raises(Exception):
        Utility.get_view_ddl(view, None)


def test_list_to_string_positive_empty_list():
    """Tests the `list_to_string()` method in a positive scenario with an empty list."""
    list_input = []
    string_output = Utility.list_to_string(list_input)
    assert string_output == ""


def test_list_to_string_positive_non_empty_list():
    """Tests the `list_to_string()` method in a positive scenario with a non-empty list."""
    list_input = ["my_item", "your_item", "their_item"]
    string_output = Utility.list_to_string(list_input)
    assert string_output == "my_item your_item their_item"


def test_list_to_string_negative_invalid_list():
    """Tests the `list_to_string()` method in a negative scenario with an invalid list."""
    list_input = "invalid_list"
    with pytest.raises(Exception):
        Utility.list_to_string(list_input)


def test_list_to_string_negative_no_list():
    """Tests the `list_to_string()` method in a negative scenario with no list."""
    with pytest.raises(Exception):
        Utility.list_to_string(None)


def test_list_to_string():
    """Tests the `list_to_string()` method."""
    list_input = [1, 2, 3, 4, 5]
    string_output = Utility.list_to_string(list_input)
    assert string_output == "1 2 3 4 5"


def test_replace_cr_by_lf():
    """Tests the `replace_cr_by_lf()` method."""
    query = "select * from my_table\rwhere id = 1"
    query_output = Utility.replace_cr_by_lf(query)
    assert query_output == "select * from my_table\nwhere id = 1"


def test_replace_cr_by_lf_negative_no_query():
    """Tests the `replace_cr_by_lf()` method in a negative scenario with no query."""
    with pytest.raises(Exception):
        Utility.replace_cr_by_lf(None)


def test_list_to_string_negative_not_list():
    """Tests the `list_to_string()` method in a negative scenario with a non-list."""
    list_input = 1234
    with pytest.raises(Exception):
        Utility.list_to_string(list_input)


def test_replace_cr_by_lf_negative_string_query():
    """Tests the `replace_cr_by_lf()` method in a negative scenario with no query."""
    query = "select * from my_table \twhere id = 1"
    query_output = Utility.replace_cr_by_lf(query)
    assert query_output == "select * from my_table \twhere id = 1"


def test_write_string_to_file():
    """Tests the `write_string_to_file()` method."""
    filename = "my_file.txt"
    string = "This is my file content."
    Utility.write_string_to_file(filename, string, "/tmp")
    assert os.path.exists(os.path.join("/tmp", filename))


def test_write_string_to_file_positive():
    """Tests the `write_string_to_file` function with positive scenarios."""
    filename = "test.txt"
    string = "This is a test string."
    tmp_path = "/tmp"

    Utility.write_string_to_file(filename, string, tmp_path)

    with open(os.path.join(tmp_path, filename), "r") as f:
        content = f.read()
    assert content == string

