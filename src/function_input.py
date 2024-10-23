import sympy as sp


def input_function_from_file(file_path):
    """
    Reads mathematical functions from a file and returns them as sympy expressions.
    Assumes each line in the file contains one mathematical function in terms of 'n'.

    :param file_path: Path to the file containing functions
    :return: List of sympy expressions
    """
    functions = []
    n = sp.Symbol('n')

    try:
        with open(file_path, 'r') as file:
            for line in file:
                function_str = line.strip()
                if function_str:
                    try:
                        func = sp.sympify(function_str)
                        functions.append(func)
                    except sp.SympifyError:
                        print(f"Invalid function in line: {function_str}")
                        continue
        return functions
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
