# Problem 4: Given an array of N integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:
# a. Each student gets one packet.
# b. The difference between the number of chocolates in the packet with the maximum chocolates and the packet with the minimum chocolates given to the students is minimum.


def minDiff(arr,m):
    arr.sort()

    min_diff=float('inf')
    for i in range(len(arr)-(m-1)):
        diff=arr[i+(m-1)]-arr[i]

        if diff<min_diff:
            min_diff=diff
        

    return min_diff

arr=list(int(x) for x in input("Enter numbers comma separated: ").split(","))
m=int(input("enter the no. of student: "))

print(f'Minimum Difference is {minDiff(arr,m)}')


