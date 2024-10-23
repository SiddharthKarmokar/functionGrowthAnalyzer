from function_plotter import plot_functions
import sympy as sp


def test_plot_functions():
    n = sp.Symbol('n')

    test_functions = [n ** 2, sp.log(n), 2 ** n]

    try:
        plot_functions(test_functions)
        print("test_plot_functions passed! No errors during plotting.")
    except Exception as e:
        print(f"test_plot_functions failed: {e}")

def test_special_case_functions():
    n = sp.Symbol('n')

    special_functions = [1, n ** 0, sp.Heaviside(n)]

    try:
        plot_functions(special_functions)
        print("test_special_case_functions passed! No errors with special functions.")
    except Exception as e:
        print(f"test_special_case_functions failed: {e}")


test_plot_functions()
test_special_case_functions()

