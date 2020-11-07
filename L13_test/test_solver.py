# from unittest import TestCase
from pytest import mark, raises
from solver import Solver, mul, sub, SUB_ERROR_TEXT

@mark.parametrize(
    "values, expected_result",
    [
        ((3,5), 15), # не упадет, как в случае с циклом
        ((1,10), 10),
        # ((1,0), 1),
        ((1,0), 0),
        ((4,8), 32),
    ]
)
def test_mul(values, expected_result):
    res = mul(*values)
    assert res == expected_result

def test_sub_raises():
    with raises(TypeError) as exc_info:
        sub(1, "")
    assert str(exc_info.value) == SUB_ERROR_TEXT


# # for running tests in folder: python -m unittest
# class TestSolver(TestCase):
#     def test_add(self): # все тесты должны быть инстансами (self)
#         res = Solver.add(1,2)
#         self.assertEqual(res, 3)
#         res = Solver.add(4,5)
#         self.assertEqual(res, 9)
#
#     def test_2(self):
#         pass

