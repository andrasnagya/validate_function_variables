# Unit test
# pylint: disable=C0114
import unittest
from typing import Any

from decorators import validate_input


@validate_input([int, str], {"kwarg_a": int, "kwarg_b": str})
def test_func(arg_a: Any, arg_b: Any, kwarg_a: Any = 0, kwarg_b: Any = "") -> bool:
    # pylint: disable=C0116
    # pylint: disable=W0613
    return True


@validate_input([str, int], {"kwarg_1": str, "kwarg_2": int})
def wrong_func(arg_1: Any, arg_2: Any, kwarg_1: Any = 0, kwarg_2: Any = "") -> bool:
    # pylint: disable=C0116
    # pylint: disable=W0613
    return True


# print(test_func(1, "str", kwarg_a=2, kwarg_b="kwarg"))


class TestValidateInput(unittest.TestCase):
    """
    This test case class contains test methods to verify the behavior of the decorated
    functions when provided with correct and incorrect arguments and keyword arguments.

    Test Methods:

    test_correct_args: Tests the decorated function with correct arguments and keyword
    arguments.
    test_incorrect_args: Tests the decorated function with incorrect positional arguments.
    test_incorrect_kwargs: Tests the decorated function with incorrect keyword arguments.
    test_wrong_expected_types: Tests the decorated function with incorrect expected types.

    """

    def test_correct_args(self) -> None:
        # pylint: disable=C0116
        self.assertTrue(test_func(1, "str", kwarg_a=2, kwarg_b="kwarg"))

    def test_incorrect_args(self) -> None:
        # pylint: disable=C0116
        self.assertIsNone(test_func(1, 2, kwarg_a=2, kwarg_b="kwarg"))

    def test_incorrect_kwargs(self) -> None:
        # pylint: disable=C0116
        self.assertIsNone(test_func(1, "str", kwarg_a="kwarg", kwarg_b=2))

    def test_wrong_expected_types(self) -> None:
        # pylint: disable=C0116
        self.assertIsNone(wrong_func(1, "str", kwarg_1=2, kwarg_2="kwarg"))


# Run the tests
if __name__ == "__main__":
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestValidateInput)

    # Run the tests
    unittest.TextTestRunner(verbosity=2).run(suite)
