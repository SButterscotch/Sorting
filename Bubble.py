def sorter(arr):

    
    for x in range(0, len(arr) - 1):

        for y in range(0, len(arr) - 1):

            if arr[y] > arr[y + 1]:
                temp = arr[y]
                arr[y] = arr[y + 1]
                arr[y + 1] = temp



array = ["Sam", "Zeeke", "Abby", "Aarnie"]

print(f"\nHere is your unsorted array: {array} \n")

sorter(array)

print(f"Here is your sorted array: {array} \n", )