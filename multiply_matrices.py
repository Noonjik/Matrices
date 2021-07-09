def read_matrix_from_file(name):
    a=[]
    b=[]
    with open(name+'.txt', 'r') as reader:
        for line in reader:
            a.append(line.split())
    
    for i in range(len(a)):
        for j in range (len(a[i])):
            a[i][j] = int(a[i][j])
    return a

def multiply_matrices(first_matrix, second_matrix):
    a = first_matrix
    b = second_matrix
    c = []
    element = 0
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[i])):
            for k in range(len(a)) :
                element += a[i][k]*b[k][j]
            c[i].append(element)
            element = 0
    return c

def write_matrix_to_file (C, filename):
    matrix = []
    for i in range(len(C)):
        matrix.append([])
        for j in range(len((C)[i])):
            matrix[i].append(C[i][j])

    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(lambda x: str(x), row)))
            f.write('\n')

if __name__ == '__main__':
    A_matrix = read_matrix_from_file('A')
    B_matrix = read_matrix_from_file('B')
    C_matrix = multiply_matrices(A_matrix, B_matrix)
    write_matrix_to_file(C_matrix, 'result.txt')
