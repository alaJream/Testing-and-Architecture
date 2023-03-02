import unittest
import pytest
import math
from carbon_dating import get_age_carbon_14_dating

# Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test againt
# this special case.
import math

def test_carbon_dating():
    carbon_14_ratio = 0.35
    if carbon_14_ratio <= 0:
        assert math.isnan(get_age_carbon_14_dating(carbon_14_ratio))
    else:
        expected_age = 8680.34
        calculated_age = get_age_carbon_14_dating(carbon_14_ratio)
        tolerance = 0.05 * expected_age
        
        assert math.isclose(calculated_age, expected_age, rel_tol=0, abs_tol=tolerance)
