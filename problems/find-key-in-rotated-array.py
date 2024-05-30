"""
An e-commerce organisation's network uses data encryption to ensure the security
of sales data during transmission. While encrypting a sequence of sales data of 
N hours, a key is generated. The generated key is added to every element of the 
sequence and the sequence is rotated. The rotated sequence and the key are transmitted. 
During transmission, the key is disrupted. The network algorithm has both
the original sequence and the rotated sequence and must be enhanced with a feature 
to recover the key.
Write an algorithm to find the key.

Input
The first line of the input consists of an integer - datalist size, representing
the number of hours for which data is present in the sequence (N).
The next line consists of N space-separated integers - dataList[0], dataList[1].
....... dataList[N-1], representing the data in the sequence.
The third line consists of an integer - rotateDataList_size, representing the number 
of hours of data in the rotated sequence (rotateDataList_size(M) is always equal to datalist size (N)).
The next line consists of M space-separated integers - rotateDataList[0]. rotate
DataList[1]...... rotateDataList[N-1], representing the data in the rotated sequence.

Output
Print an integer representing the key which is added to every element of the original sequence.

Example
input
5
22 5 4 7 15
5
14 17 25 32 15

output
10
"""

from collections import deque
from operator import sub

"""
Time complexity: O(n^2)
Space complexity: O(n)
"""
def find_key(original_arr: list[int], rotated_arr: list[int]):
    for i in range(len(original_arr)):
        dq = deque(original_arr)
        dq.rotate(i)
        rotated_temp_arr = list(dq)

        diff = list(map(sub, rotated_arr, rotated_temp_arr))
        if len(set(diff)) == 1:
            return diff[0]
    
    return None

original_arr_size = int(input())
original_arr = list(map(int, input().split()))
rotated_arr_size = int(input())
rotated_arr = list(map(int, input().split()))

key = find_key(original_arr, rotated_arr)
print("The key which was added to the array before rotation is", key)
