from extensions import get_ext
import pytest


@pytest.mark.parametrize("input,expected",
                         [
                             ("happy.jpg", "image/jpeg"),
                             ("document.pdf", "application/pdf"),
                             ("exporer.exe", "application/octet-stream"),
                         ])
def test_get_ext(input, expected):
    assert get_ext(input) == expected
