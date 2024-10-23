from function_input import input_function_from_file

def test_input_function():
    # Test case: Create a mock functions.txt file with valid and invalid functions
    test_file = "test_functions.txt"
    with open(test_file, 'w') as f:
        f.write("n**2\n")
        f.write("2**n\n")
        f.write("n*log(n)\n")
        f.write("invalid_function\n")  # Invalid function

    # Call the function to input functions from file
    functions = input_function_from_file(test_file)

    # Expected output should exclude the invalid function
    assert len(functions) == 3, "Should have 3 valid functions"
    assert str(functions[0]) == "n**2", "First function should be n**2"
    assert str(functions[1]) == "2**n", "Second function should be 2**n"
    assert str(functions[2]) == "n*log(n)", "Third function should be n*log(n)"

    print("test_input_function passed!")

def test_invalid_file():
    # Test with a non-existent file
    file_path = "non_existent_file.txt"
    functions = input_function_from_file(file_path)

    assert functions is None, "Expected None when file does not exist"

    print("test_invalid_file passed!")


def test_empty_file():
    # Create an empty file
    empty_file = "empty_functions.txt"
    with open(empty_file, 'w') as f:
        pass

    # Test input function with an empty file
    functions = input_function_from_file(empty_file)

    assert functions == [], "Expected an empty list for an empty file"

    print("test_empty_file passed!")



test_input_function()
test_invalid_file()
test_empty_file()

