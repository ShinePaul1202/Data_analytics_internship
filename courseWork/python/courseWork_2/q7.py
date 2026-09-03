# Problem 7: You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


def rotate(matrix):
    n=len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for row in matrix:
        row.reverse()


n=int(input("Enter the size of matrix: "))

matrix=[]

for i in range(n):
    row=list(map(int, input("Enter row: ").split(',')))
    matrix.append(row)

rotate(matrix)

print(matrix)