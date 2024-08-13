import random
import pytest

from professor import generate_integer


@pytest.mark.parametrize(
    "level,expected",
    [
        (1, (6, 6, 0, 4, 8, 7, 6, 4, 7, 5, 9, 3, 8, 2, 4, 2, 1, 9, 4, 8,)),
        (2, (59, 63, 15, 43, 75, 72, 61, 48, 71, 55, 84, 37, 74, 27, 46, 27, 22, 89, 42, 78, )),
        (3, (964, 494, 876, 530, 141, 365, 623, 597, 514, 902, 949, 410, 588, 466, 697, 323, 616, 242, 388, 243, )),
    ]
)
def test_professor_generate_integer(level, expected):
    random.seed(0)
    assert tuple(generate_integer(level) for _ in range(20)) == expected
