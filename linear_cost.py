import numpy as np

def linear_cost(theta,X,y):
    m,n = X.shape
    h = np.matmul(X,theta)
    sq = (y-h) ** 2
    return sq.sum()/(2*m)


def linear_cost_j(theta,X,y):
    m,n = X.shape
    h = np.matmul(X,theta)
    sq = (h-y)*X
    return sq.sum()/m