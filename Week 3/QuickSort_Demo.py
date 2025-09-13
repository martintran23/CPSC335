def quick_sort(arr):
    
    def partition(low, high):
        pivot = arr [(low + high) // 2]
        i = low
        j = high
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return i, j
    
    def sort(low, high):
        if low < high:
            i, j = partition(low, high)
            sort(low, j)
            sort(i, high)
    sort(0, len(arr) - 1)
    return arr
            
#test with demo
if __name__ == "__main__":
    data = [13, 12, 11, 5, 6]
    print("Unsorted Data: ", data)
    sorted_data = quick_sort(data)
    print("Sorted Data: ", sorted_data)