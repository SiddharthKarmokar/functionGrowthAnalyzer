from function_input import input_function_from_file
from function_plotter import plot_functions


def main():
    file_path = '../functions.txt'
    functions = input_function_from_file(file_path)

    if functions:
        print("Functions successfully loaded from file:")
        for func in functions:
            print(func)

       
        plot_functions(functions)


if __name__ == "__main__":
    main()
