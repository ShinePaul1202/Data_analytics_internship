# Problem 3: Given an array of N integers and a number K, the task is to find the number of pairs of integers in the array whose sum is equal to K.


def countSum(arr,k):
    count=0

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):

            if arr[i]+arr[j]==k:
                count+=1

    return count


arr=list(int(x) for x in input("Enter numbers comma separated: ").split(','))

k=int(input("Enter K: "))

print(countSum(arr, k))