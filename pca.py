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
        self.array_training = None

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
        eigenvalues, eigenvectors = np.linalg.eig(data)
        return [eigenvalues, eigenvectors]

    def __verify_default_error_when_execute_before_fit(self):
        if self.fit_run == False:
            raise Exception("The method fit have to execute before than this method")

    def __subtract_the_mean(self, data: np.array) -> np.array:
        data_copy = np.copy(data)
        mean = self.__get_mean(data=data_copy)
        for i in range(len(data_copy)):
            data_copy[i] = data_copy[i] - mean[i]
        return data_copy

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
        [self.eigenvalues, self.eigenvectors] = self.__get_eigenvalues_and_eigenvectors(data=self.covariance)

        array_training = [(np.abs(self.eigenvalues[i]),self.eigenvectors[:,i]) for i in range(len(self.eigenvalues))]
        array_training.sort(key=lambda x: x[0], reverse=True)

        self.array_training = array_training

        print("PCA Values: %s" %self.eigenvalues)
        self.fit_run = True
    
    def transform(self, data: np.array, n_components:int):
        for i in range(0,n_components):
            eVector = self.array_training[i][1]
<<<<<<< HEAD
=======
            print(data)
            print(eVector.reshape(-1,1))
>>>>>>> d170f037b08fef7e682fb099a9630fd2334c2808
            pca = np.dot(data.transpose(),eVector).reshape(1,-1)
            if i==0:
                response = pca.T
            else:
                response = np.dstack((response,pca.T))

        return response.reshape(-1,n_components)