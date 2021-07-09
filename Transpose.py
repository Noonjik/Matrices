def Transpose (Filename):
    shape = [10,10]
    new_line = [] 
    line = str('')
    with open ('Transposed_matric.txt', 'w') as t:
        with open (Filename, 'r') as f:
            for j in range (0, 2*shape[1]):
                for i in range(0, shape[0]):
                    line = f.readline()
                    t.write(line[j])
                    t.write(' ')
                    i += 1
                t.write('\n') 
                f.seek(0)
Transpose("B.txt")