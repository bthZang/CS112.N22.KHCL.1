import pytest
from src.checkTriangle import checkTriangle
from unittest.mock import patch


# @pytest.fixture
# def mockIsLeapYear(mocker, isLeapYear):
#     mocker.patch("src.findNextDate.isLeapYear", return_value=isLeapYear)


# @pytest.fixture
# def mockGetMonthLength(mocker, monthLength):
#     mocker.patch("src.findNextDate.getMonthLength", return_value=monthLength)






# @pytest.mark.usefixtures("mockIsLeapYear")
# def test_get_month_length(month, year, isLeapYear, monthLength):
#     assert getMonthLength(month, year) == monthLength


# a	 b	c	T	F
# 3	 2	1	0	1
# 1	 2	3	0	1
# 1	 3	2	0	1
# 4	 2	5	1	0


@pytest.mark.parametrize(
    "input,output",
    [
        ((3, 2, 1), False),
        ((1, 2, 3), False),
        ((1, 3, 2), False),
        ((4, 2, 5), True),
    ],
)

def test_check_triangle(input, output):
    assert checkTriangle(*input) == output



