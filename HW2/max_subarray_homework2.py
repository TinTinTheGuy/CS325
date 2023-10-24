import sys
import time

# Usage when run from the command line: python max_subarray_homework1.py <filename>.
# Example usage:                        python max_subarray_homework1.py num_array_500.txt

file_name = sys.argv[1]

f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

def max_subarray_simplification_delegation(A):
    """
    Computes the value of a maximum subarray of the input array by "simplification and delegation."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """
    x = len(A)
    if x == 1 :
        return A[0]
    else:
        mid = x // 2
        left_half = A[:mid]
        right_half = A[mid:]
        
        half_left = max_subarray_simplification_delegation(left_half)
        half_right = max_subarray_simplification_delegation(right_half)
        
    max_left_half = float("-INF")
    max_right_half = float("-INF")
    i = (x -1) // 2
    sum = 0
    while i >= 0:
        sum += A[i]
        if sum > max_left_half:
            max_left_half = sum
        i -= 1
        
    i = (x -1) // 2 + 1
    sum = 0
    while i < x:
        sum += A[i]
        if sum > max_right_half:
            max_right_half = sum
        i += 1
            
    return max(half_left ,half_right, (half_left + half_right))

def time_alg(alg, A):
    """
    Runs an algorithm for the maximum subarray problem on a test array and times how long it takes.
    
    Parameters:
        alg: An algorithm for the maximum subarray problem.
        A: A list (array) of n >= 1 integers.
    
    Returns:
        A pair consisting of the value of alg(A) and the time needed to execute alg(A) in milliseconds.
    """

    start_time = time.monotonic_ns() // (10 ** 6) # The start time in milliseconds.
    max_subarray_val = alg(A)
    end_time   = time.monotonic_ns() // (10 ** 6) # The end time in milliseconds.
    return max_subarray_val, end_time - start_time

for alg in [max_subarray_simplification_delegation]:
    print(file_name, time_alg(alg, A))
