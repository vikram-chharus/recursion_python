from heapq import merge


arr = [1, 4, 2, 23 ,11, 56, 1, 3, 32]

def merge_sort(arr):
    if len(arr)<2:
        return arr
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    i,j,k, len_left, len_right, new_arr=0, 0, 0, len(left), len(right), []
    while i<len_left and j < len_right:
        if left[i] < right[j]:
            new_arr.append(left[i])
            i+=1
        elif left[i] > right[j]:
            new_arr.append(right[j])
            j+=1
        else:
            new_arr.append(left[i])
            new_arr.append(right[j])
            j+=1
            i+=1
    while i < len_left:
        new_arr.append(left[i])
        i+=1
    while j < len_right:
        new_arr.append(right[j])
        j+=1
    return new_arr

print(merge_sort(arr))