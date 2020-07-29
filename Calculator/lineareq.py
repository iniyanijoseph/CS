def linEq(readfile):
    matrix = []
    
    for row in readfile.split(";"):
        matrix.append(row.split(","))
    lenrow = len(matrix) + 1
    lencol = len(matrix)
    for element in range(lencol):
        for num in range(lenrow):
            matrix[element][num] = int(matrix[element][num])


    # Clears Bottom
    for element in range(lencol):
        divisor = matrix[element][element]
        if divisor == 0:
            return [0]
        for num in range(lenrow):
            matrix[element][num] = matrix[element][num] / divisor
        for num in range(element + 1, lencol):
            start = matrix[num][element]
            for n in range(lenrow):
                matrix[num][n] = matrix[num][n] - (matrix[element][n] * start)
    for element in range(lencol):
        if matrix[element][element] == 0:
            return [0]

    # Calculates X and Y values and clears top
    n = lencol - 1
    while n > 0:
        for element in range(n):
            start = matrix[element][n]
            for num in range(lenrow):
                matrix[element][num] = matrix[element][num] - (matrix[n][num] * start)
        n -= 1
    ans = []
    for element in range(lencol):
        ans.append(matrix[element][lencol])
    return ans
    
print(linEq("2, 2, 5, 5; 3, 3, 3, 10"))