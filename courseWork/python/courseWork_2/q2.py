# Problem 2: Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array without using any additional
# data structure like a hash table, arrays, etc. The order of appearance should be maintained.


def rearrange(n):
    for i in range(len(n)):

        if n[i]>0:
            j=i+1

            while j<len(n):
                if n[j]<0:
                    k=j

                    while k>i:
                        n[k-1],n[k]=n[k],n[k-1]
                        k-=1
                    break
                    
                j+=1


    return n


n = list(int(x) for x in input("Enter numbers comma separated: ").split(','))

print(*rearrange(n))