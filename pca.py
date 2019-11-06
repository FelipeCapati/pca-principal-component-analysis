from utilities.matrix import Matrix
import numpy as np
from numpy import linalg as LA
from enum import Enum


class PcaType(Enum):
    Two = 0
    Three = 1


class PCA:
    def __init__(self):
        self.fit_run = False
        self.eigenvalues = None
        self.eigenvectors = None
        self.covariance = None

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

    def __verify_default_error_when_execute_before_fit(self):
        if self.fit_run == False:
            raise Exception("The method fit have to execute before than this method")

    def __subtract_the_mean(self, data: np.array) -> np.array:
        mean = self.__get_mean(data=data)
        for i in range(len(data)):
            data[i] = data[i] - mean[i]
        return data

    def explained_variance_ratio(self) -> np.array:
        self.__verify_default_error_when_execute_before_fit()
        sum_value = np.sum(self.eigenvalues)
        variance_ratio = self.eigenvalues / sum_value
        print("PCA Variance Ratio: %s" %variance_ratio)

        return variance_ratio
    
    def singular_values(self) -> np.array:
        self.__verify_default_error_when_execute_before_fit()
        print("PCA Singular Values: %s" %self.eigenvalues)
        return self.eigenvalues

    
    def get_covariance(self) -> np.array:
        self.__verify_default_error_when_execute_before_fit()
        return self.covariance            
    
    def fit(self, data: np.array, pcaType: PcaType = PcaType.Two):
        data_sub_mean = self.__subtract_the_mean(data=data)
        self.covariance = self.__get_covariance_matrix(data=data_sub_mean)
        [eigenvalues, eigenvectors] = self.__get_eigenvalues_and_eigenvectors(data=self.covariance)

        self.eigenvalues = eigenvalues
        self.eigenvectors = eigenvectors

        print("PCA Values: %s" %self.eigenvalues)
        self.fit_run = True
    
    def transform(self, data: np.array, variables:np.array):
        self.__verify_default_error_when_execute_before_fit()

        variables_length = len(self.eigenvalues)
        response = np.array([])

        if(variables == None):
            variables = np.arange(variables_length)

        for i in range(len(data)):
            for j in range(len(variables)):
                # response = np.append(response, np.sum(self.eigenvectors[j].transpose() * data.transpose(), axis=1), axis=0)
                # print(response)
                response = np.append(response, np.sum(self.eigenvectors[j].transpose() * data.transpose(), axis=1), axis=0)
                print(response)