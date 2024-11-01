def merge_sort(arr):
    """Sort an array using the merge sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]  # Divide the array elements into 2 halves
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0  # Initialize indices for left_half, right_half, and arr

        # Copy data to temporary arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def example_function(n):
    """Example function demonstrating merge sort with a sample array."""
    # Create a sample array
    arr = [n - i for i in range(n)]  # Example array from n to 1
    merge_sort(arr)  # Sort the array

    return arr

# Example usage:
if __name__ == "__main__":
    n = 10  # Example size
    sorted_array = example_merge_sort(n)
    print(f"Sorted array: {sorted_array}")
