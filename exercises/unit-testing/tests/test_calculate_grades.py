import unittest
from unittest import mock
import pytest
import math
from calculate_grades import calculate_stat


class TestCalculateStat(unittest.TestCase):

    def test_calculate_stat(self):
        mean_answer = 77
        sd_answer = 7.95
        grades = [65, 72, 78, 82, 88]
        mean, sd = calculate_stat(grades)
        assert math.isclose(mean, mean_answer, abs_tol=0.05)
        assert math.isclose(sd, sd_answer, abs_tol=0.05)
