from function_complexity import determine_complexity
import sympy as sp


def test_function_complexity():
    n = sp.Symbol('n')

    # Sample functions and expected complexities
    test_cases = {
        n ** 2: "O(n^2)",
        2 ** n: "O(2^n)",
        n * sp.log(n): "O(n log n)",
        sp.log(n): "O(log n)"
    }

    for func, expected in test_cases.items():
        complexity = determine_complexity(func)
        assert complexity == expected, f"Expected {expected}, but got {complexity} for function {func}"

    print("test_function_complexity passed!")


test_function_complexity()
