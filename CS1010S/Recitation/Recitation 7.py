#Question 1
def matrix(seq):
    mat = []
    for row in seq:
        mat.append(list(row)) # Create brand new list so that there is no reference to the old seq.
    return mat

# Question 1b
def rows(m):
    return len(m)

def cols(m):
    return len(m[0])

def get(m, x, y):
    return m[x][y]

def sets(mat, x, y, val):
    get(mat, x, y) = val
    return mat

def transpose(m):
    n = len(m)
    final_list = []
    for i in range(n):
        for j in range(len(m[i])):
            if len(result) <= j:
                result.append([m[i][j]])
            else:
                result[j].append(m[i][j])
    m.clear()
    m.extend(new_mat)
    return m

def print_matrix(mat):
    for rows in mat:
        print(rows)

#Question 2
def make_matrix(seq):
    data = []
    for i in range(len(seq)):
        for j in range(len(seq[0])):
            if seq[i][j] != 0:
                data.append([i,j,seq[i][j]])
            #[num_rows, num_cols, data]
            #data: list of x and y < 0.
    return [len(seq), len(seq[0]), data]

# Question 2a
def rows2(m):
    return m[0]

def col2(m):
    return m[1]

def get2(m, x, y):
    for ele in m[2]:
        if ele[0] == x and ele[1] == y:
            return ele[2]
    return 0

def sets2(mat, x, y, val):
    for ele in mat[2]:
        if ele[0] == x and ele[1] == y:
            if val == 0:
                m[2].remove(item)
            else:
                item[2] = val
            return mat
        
    m[2].append([x, y, val])
    return mat

def transpose2(m):
    for ele in m[2]:
        ele[0], ele[1] = ele[1], ele[0]
    m[1], m[2] = m[2], m[1]
    return m

def print_mat(matrix):
    # create a dense matrix full of 0s
    dense_mat = []
    r = num_rows(m)
    c = col_rows(m)
    for i in range(r):
        dense_mat.append([0] * c)

    # populate dense matrix with data
    for i, j, val in matrix[2]:
        dense_mat[i][j] = val

    for row in dense_mat:
        print(row)
    
        

