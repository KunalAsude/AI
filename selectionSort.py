def selectionSort(arr):
    for i in range (len(arr)):
        min_index=i
        for j in range (i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

        print("The output after pass "+str(i+1)+" is "+str(arr))

inputArr= input("Enter the elemets seperated by spaces = ")
arr=inputArr.split()
arr=[int(i) for i in arr]

selectionSort(arr)