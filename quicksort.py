#def quicksort(array):
    #   for i in range(len(array)):
    # pivotIndex = 0
    # storeIndex = pivotIndex + 1
    # for i in range(len(array)):
    #     if array[i] < array[pivotIndex]:
    #         array[i], array[storeIndex] = array[storeIndex], array[i]
    #         storeIndex += 1
    # if len(array) > 1:
    #     array[pivotIndex], array[storeIndex - 1] = array[storeIndex - 1], array[pivotIndex]
    #     tmp = storeIndex
    #     storeIndex = pivotIndex
    #     return quicksort(array[:tmp])
    # else:
    #     return array

def partition(array, low ,high):
    i = low
    pivot = array[high]
    for j in range(low,high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i +=1
    array[i], array[high] = array[high], array[i]
    return i

def quicksort(array, low, high):
    if len(array) == 1:
        return array
    elif low<high:
    # getting partition index
        pi = partition(array,low,high)
        quicksort(array,low, pi-1)
        quicksort(array,pi+1,high)
#Driver code
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
n = len(test) - 1
quicksort(test,0,n)
print(test)
