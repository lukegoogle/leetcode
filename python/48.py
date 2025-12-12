def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for i in range(n):
        matrix[i].reverse()

# Example Output
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix1)
print(f"Output for [[1, 2, 3], [4, 5, 6], [7, 8, 9]]: {matrix1}")

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(matrix2)
print(f"Output for 4x4 matrix: {matrix2}")