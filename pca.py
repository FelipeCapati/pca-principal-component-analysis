from utilities.matrix import Matrix
import numpy as np
from numpy import linalg as LA
from enum import Enum


class PcaType(Enum):
    Two = 0
    Three = 1


class PCA:
    def __init__(self):
        pass

    @staticmethod
    def __get_mean(data: np.array) -> np.array:
        num_column = len(data)
        num_line = len(data[0])
        response = np.zeros(num_column)

        for column in range(num_column):
            for line in range(num_line):
                response[column] = response[column] + data[column][line]
            response[column] = response[column] / num_line
        return response

    @staticmethod
    def __get_covariance_matrix(data: np.array) -> np.array:
        return np.cov(data)
    
    @staticmethod
    def __get_eigenvalues_and_eigenvectors(data: np.array) -> np.array:
        eigenvalues, eigenvectors = LA.eig(data)
        return [eigenvalues, eigenvectors]

    def __subtract_the_mean(self, data: np.array) -> np.array:
        mean = self.__get_mean(data=data)
        for i in range(len(data)):
            data[i] = data[i] - mean[i]
        return data
    


    def fit(self, data: np.array, pcaType: PcaType = PcaType.Two):
        print(data)
        data = self.__subtract_the_mean(data=data)
        print(data)
        data = self.__get_covariance_matrix(data=data)
        print(data)
        [eigenvalues, eigenvectors] = self.__get_eigenvalues_and_eigenvectors(data=data)
        print(eigenvalues)
        print(eigenvectors)
