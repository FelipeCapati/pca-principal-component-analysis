from utilities.matrix import Matrix
from enum import Enum


class LmsType(Enum):
    Linear = 0
    Quadratic = 1


class LMS:
    def __init__(self):
        self.beta = None
        self.type = None

    @staticmethod
    def __append_w_value_on_x_array(x: list, w: list) -> list:
        # If not specify a w on X matrix
        if w is None:
            response = []
            for i in range(len(x)):
                response.append([])
                line = [_ for _ in x[i]]
                response[i].append(1)
                for data in line:
                    response[i].append(data)
        # If value of w was specified on w matrix
        else:
            response = []
            for i in range(len(x)):
                response.append([])
                line = [_ for _ in x[i]]
                response[i].append(w[i][0])
                for data in line:
                    response[i].append(data)

        return response

    @staticmethod
    def __get_beta_array_by_matrix(x: Matrix, y: Matrix):
        return Matrix.inverse(Matrix.transposed(x) * x) * Matrix.transposed(x) * y

    @staticmethod
    def __get_quadratic_variables_by_x_array(x: list) -> list:
        for i in range(len(x)):
            line = [_ for _ in x[i]]
            for j in range(1, len(line)):
                x[i].append(line[j] * line[j])

        return x

    @staticmethod
    def __get_result_by_x_and_beta_array(x: list, beta: list) -> list:
        response = []
        for i in range(len(x)):
            response.append([0.0])
            for j in range(len(beta)):
                response[i][0] += beta[j][0] * x[i][j]

        return response

    def fit(self, x: list, y: list, w: list = None, type: LmsType = LmsType.Linear):
        self.type = type

        lms_x = self.__append_w_value_on_x_array(x=x, w=w)

        response = None
        if type == LmsType.Linear:
            response = self.__get_beta_array_by_matrix(Matrix(lms_x), Matrix(y))

        if type == LmsType.Quadratic:
            x_list = self.__get_quadratic_variables_by_x_array(lms_x)
            response = self.__get_beta_array_by_matrix(Matrix(x_list), Matrix(y))

        self.beta = response.matrix

        return response.matrix

    def predict(self, x: list, w: list = None):
        lms_x = self.__append_w_value_on_x_array(x=x, w=w)

        response = None
        if self.type == LmsType.Linear:
            response = self.__get_result_by_x_and_beta_array(x=lms_x, beta=self.beta)
        if self.type == LmsType.Quadratic:
            x_quadratic = self.__get_quadratic_variables_by_x_array(lms_x)
            response = self.__get_result_by_x_and_beta_array(x=x_quadratic, beta=self.beta)

        return response
