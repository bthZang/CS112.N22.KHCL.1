import pytest
from src.checkPrime import checkPrime
from unittest.mock import patch

@pytest.mark.parametrize(
    "input, output",
    [
        (1 , False),
        (2, True),
        (3, True),
        (4, False),
    ],
)


def test_checkPrime(input, output):
    assert checkPrime(input) == output

