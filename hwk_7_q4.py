from typing import List

def my_sort(A: List[int]) -> List[int]:
    n = len(A)
    Count = [0]*n
    Output = [0]*n

    # Loop through A with i as index
    for i in range(n):
    
        # update a variable counting the entries in A smaller than A[i]
        # Initialize count to 0
        count = 0

        # Count the number of elements in A smaller than A[i]
        # Iterate over each element in A
        for j in A:
            # Check if j is less than A[i]
            if j < A[i]:
                # If so, increment the count
                count += 1

        # End of Loop: append the count variable to Count[i]
        Count[i] = count
        
    for i in range(n):
        Output[Count[i]] = A[i]

    return Output

A = [154, 144, 951, 431, 554, 984, 
    54, 630, 658, 567, 486, 198, 
    584, 108, 415, 320, 725, 563, 
    881, 378, 150, 761, 123, 760]

B = [54, 108, 123, 144, 150, 154,
    198, 320, 378, 415, 431, 486,
    554, 563, 567, 584, 630, 658,
    725, 760, 761, 881, 951, 984]

print(my_sort(A))
print(my_sort(B))
