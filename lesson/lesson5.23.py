def example_func(param1, param2):
    """Example function with types documented in the docstring.
    Args:
        prams1 (int): first param.
        prams2 (str): second param.

    Returns:
        bool: The return value. True for success. False otherwise.
    """
    print(param1)
    print(param2)
    return True

# print(example_func.__doc__)
help(example_func)