def binary_search(arr, target):
    """Perform binary search on a sorted array to find the target value."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        # Check if the target is at mid
        if arr[mid] == target:
            return mid  # Target found

        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    return -1  # Target not found

def example_function(n):
    """Example function demonstrating binary search with O(log n) complexity."""
    # Generate a sorted list of integers
    arr = list(range(1, n + 1))  # Sorted array from 1 to n

    # Define a target to search for
    target = n // 2  # For example, searching for the middle value

    # Perform binary search
    index = binary_search(arr, target)

    return index

# Example usage:
if __name__ == "__main__":
    n = 100  # Example size
    result_index = example_function(n)

    if result_index != -1:
        print(f"Target found at index: {result_index}")
    else:
        print("Target not found.")