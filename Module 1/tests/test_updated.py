from square_example import square
import pytest

def test_positive_numbers() :
    assert square(2) == 4
    assert square(3) == 9

def test_negative_numbers() :
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero() :
    assert square(0) == 0


def test_square_with_string():
    with pytest.raises(TypeError):
        square("cat")