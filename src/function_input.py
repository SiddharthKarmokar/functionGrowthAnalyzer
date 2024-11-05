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
                print(f"Reading line: '{function_str}'")
                if function_str:
                    try:
                        func = sp.sympify(function_str, locals={'n': n})
                        functions.append(func)
                    except sp.SympifyError:
                        print(f"Invalid function in line: '{function_str}'")  # Handle sympy errors

        return functions
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


# Example usage
if __name__ == "__main__":
    file_path = '../functions.txt'
    functions = input_function_from_file(file_path)

    if functions:
        print("Functions successfully loaded from file:")
    else:
        print("No valid functions found or file not found.")
