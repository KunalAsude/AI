def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)

print("Sorted array:", arr)

# userinput = input("Enter a list of numbers separated by spaces: ")
# userinput = user-input.split()   
# userinput = [int(i) for i in userinput]
# selection_sort(userinput)
# print("Sorted user input:", userinput)