import functools
from typing import List
import numpy as np  

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:

    j = 1 
    for idx, e in enumerate(A):
        if A[j-1] != A[idx]:
            A[j] = A[idx]
            j+=1

    return j

    '''
    #lol
    A = np.unique(A) 
    return len(A)
    '''

