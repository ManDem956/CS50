from camel import convert
import pytest


@pytest.mark.parametrize("input, expected",
                         [
                             ("name", "name"),
                             ("firstName", "first_name"),
                             ("preferredFirstName", "preferred_first_name"),
                         ])
def test_get_convert(input, expected):
    assert convert(input) == expected
