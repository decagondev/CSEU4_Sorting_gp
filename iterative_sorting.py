# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # iterate over a range
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        
        # swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr

# implement the Insertion Sort function below
def insertion_sort( arr ):
  # loop through n-1 elements
  for i in range(1, len(arr)):
    temp = arr[i]
    j = i
    while j > 0 and temp < arr[j - 1]:
      # shift left until correct position found
      arr[j] = arr[j - 1]
      j -= 1
    # insert at correct position
    arr[j] = temp

  return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr