def sorter(arr):

    #Range from 1 cus we have to go back, this is insertion sort so we check the current\n
    #value with all of it's previous values.
    for x in range(1, len(arr)):

        # Position decreases after every iteration to compare the current value with its previous values.
        pos = x
        cur = arr[x]

        while pos > 0 and arr[pos - 1] > cur:
            arr[pos] = arr[pos - 1]
            pos -= 1
        
        # Current value had to be saved to replace the lesser values previous to it

        arr[pos] = cur


array = ["Sam", "Zeeke", "Abby", "Aarnie"]

print(f"\nHere is your unsorted array: {array} \n")

sorter(array)

print(f"Here is your sorted array: {array} \n", )

        