

def transpose_matrix(m):
    response = []
    once = True

    for i in range(len(m)):
        for j in range(len(m[0])):
            if once:
                response.append([])
            col = [_ for _ in m[i]]
            response[j].append(col[j])
        once = False

    return response


def get_matrix_minor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def get_matrix_deternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*get_matrix_deternminant(get_matrix_minor(m,0,c))
    return determinant


def get_matrix_inverse(m):
    determinant = get_matrix_deternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * get_matrix_deternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose_matrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


class Matrix:
    def __init__(self, mat: list):
        self.matrix = mat
        self.lin = len(mat)
        self.col = len(mat[0])

    def get_linha(self, n: int):
        return [_ for _ in self.matrix[n]]

    def get_coluna(self, n: int):
        return [i[n] for i in self.matrix]

    def __mul__(self, mat2):
        response = []

        for i in range(self.lin):
            response.append([])

            for j in range(mat2.col):
                auxiliar_list = [x*y for x, y in zip(self.get_linha(i), mat2.get_coluna(j))]
                response[i].append(sum(auxiliar_list))

        return Matrix(response)

    def transposed(self):
        return Matrix(transpose_matrix(self.matrix))

    def determinant(self):
        return get_matrix_deternminant(self.matrix)

    def inverse(self):
        return Matrix(get_matrix_inverse(self.matrix))
