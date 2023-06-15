"""
This module provides a decorator for type validation of function arguments and keyword
arguments.

Example usage:

@validate_input([int, str], {"kwarg1": int, "kwarg2": str})
def test_func(arg1, arg2, kwarg1=0, kwarg2=""):
# Your function code here

This module is useful in situations where you want to ensure that functions are called with
correctly typed parameters, and automatically prevent or handle cases where they are not.
"""

from typing import Any, Callable, Dict, List, Optional, Sized, TypeVar, cast

from functools import wraps

F = TypeVar("F", bound=Callable[..., Optional[Any]])


def validate_input(
    expected_arg_types: List[Any], expected_kwarg_types: Optional[Dict[str, Any]] = None
) -> Callable[[F], F]:
    """
    This decorator validates the type of arguments and keyword arguments
    provided to a function. It checks if the types of the provided
    arguments and keyword arguments match the expected types. If the types
    match, it calls the function with the arguments and keyword arguments.
    If they do not match, it returns None.

    Args:
        expected_arg_types (List[Any]): A list of types that the decorator
        should expect for the arguments of the decorated function. The
        order matters.

        expected_kwarg_types (Dict[str, Any], optional): A dictionary
        mapping keyword argument names to expected types for the decorated
        function. If a keyword argument is not in this dictionary or its
        type does not match the expected type, the decorated function will
        not be called.

    Returns:
        Callable[[F], F]: A decorator which can be applied to a function.
        When the decorated function is called, the decorator checks the
        types of the arguments and keyword arguments. If they match the
        expected types, the decorated function is called. Otherwise,
        None is returned.

    Example:
        @validate_input([int, str], {"kwarg_a": int, "kwarg_b": str})
        def test_func(arg_a: Any, arg_b: Any, kwarg_a: Any = 0, kwarg_b: Any = "") -> bool:
            return True


        @validate_input([str, int], {"kwarg_1": str, "kwarg_2": int})
        def wrong_func(arg_1: Any, arg_2: Any, kwarg_1: Any = 0, kwarg_2: Any = "") -> bool:
            return True

    """

    if expected_kwarg_types is None:
        expected_kwarg_types = {}  # Set default value here
    expected_kwarg_types = cast(Optional[Dict[str, Any]], expected_kwarg_types)

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
            # pylint: disable=W0511
            # Validate type of positional arguments
            if len(args) != len(expected_arg_types):
                # TODO: You should post your status to a msg queue or a logger from here
                return None
            for arg, expected_type in zip(args, expected_arg_types):
                if not isinstance(arg, expected_type):
                    # if type(arg) is not expected_type:
                    # TODO: You should post your status to a msg queue or a logger from here
                    return None

            # Validate type of keyword arguments
            if not isinstance(expected_kwarg_types, Sized) or len(kwargs) != len(
                expected_kwarg_types
            ):
                # pylint: disable=W0511
                # TODO: You should post your status to a msg queue or a logger from here
                return None

            for kwarg, value in kwargs.items():
                if kwarg not in expected_kwarg_types or not isinstance(
                    value, expected_kwarg_types[kwarg]
                ):
                    return None
            return func(*args, **kwargs)

        return wrapper  # type: ignore

    return decorator
