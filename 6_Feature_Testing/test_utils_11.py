import pytest

from test_functions_11 import get_grade


points_parameters = [
    (20, 2),
    (40, 3),
    (80, 4),
    (100, 5),
]


@pytest.mark.parametrize("grade_int, grade_str", points_parameters)
def test_get_grade(grade_int, grade_str):
    assert get_grade(grade_int) == grade_str


points_exceptions = [
    (-1, ValueError),
    (120, ValueError),
    ("1", TypeError),
    (1.0, TypeError)
]


@pytest.mark.parametrize("grade_int, exception", points_exceptions)
def test_get_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        get_grade(grade_int)