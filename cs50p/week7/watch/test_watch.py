import pytest
from watch import parse


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>',
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',  # noqa: E501
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>',
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',  # noqa: E501
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>',
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe width="560" height="315" src="http://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',  # noqa: E501
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>',
            None,
        ),
    ],
)
def test_parse(input, expected):
    assert parse(input) == expected
