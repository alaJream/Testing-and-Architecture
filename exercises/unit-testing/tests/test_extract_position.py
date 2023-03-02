import pytest
from extract_position import extract_position

def test_extract_position():
    # Test line with 'error' keyword
    assert extract_position('|error| numerical calculations could not converge.') is None

    # Test line with 'x:' keyword
    assert extract_position('|update| the positron location in the particle accelerator is x:21.432') == '21.432'
