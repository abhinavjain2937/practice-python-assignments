
            




def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  

    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False


Input_matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = int(input('enter your nunber for search : '))
out = search_matrix(Input_matrix,target)
print(out)