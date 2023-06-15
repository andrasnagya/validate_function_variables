# validate_function_variables

This decorator validates the type of arguments and keyword arguments
    provided to a function. It checks if the types of the provided
    arguments and keyword arguments match the expected types. If the types
    match, it calls the function with the arguments and keyword arguments.
    If they do not match, it returns None.

Args:
    ```expected_arg_types (List[Any])```: A list of types that the decorator
    should expect for the arguments of the decorated function. The
    order matters.
 
    ```
    expected_kwarg_types (Dict[str, Any], optional)
    ```  
   
A dictionary mapping keyword argument names to expected types for the decorated
function. If a keyword argument is not in this dictionary or its
type does not match the expected type, the decorated function will
not be called.

Returns:
    ```Callable[[F], F]```: A decorator which can be applied to a function.
    When the decorated function is called, the decorator checks the
    types of the arguments and keyword arguments. If they match the
    expected types, the decorated function is called. Otherwise,
    None is returned.

Example:
```
    @validate_input([int, str], {"kwarg_a": int, "kwarg_b": str})
    def test_func(arg_a: Any, arg_b: Any, kwarg_a: Any = 0, kwarg_b: Any = "") -> bool:
        return True

    @validate_input([str, int], {"kwarg_1": str, "kwarg_2": int})
    def wrong_func(arg_1: Any, arg_2: Any, kwarg_1: Any = 0, kwarg_2: Any = "") -> bool:
        return True
```
