import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import math
import numpy as np
import sympy as sym

def euc_dist(pt1,pt2):
    #  return dist of the 2 point sended
    return math.sqrt((pt2[0]-pt1[0])*(pt2[0]-pt1[0])+(pt2[1]-pt1[1])*(pt2[1]-pt1[1]))

def _c(ca,i,j,P,Q):
    # i for P j for Q
    if ca[i,j] > -1:
        return ca[i, j],ca
    elif i == 0 and j == 0:
        ca[i,j] = euc_dist(P[0],Q[0])  # calculate the dist between the last(first) two point of P,Q
    elif i > 0 and j == 0:
        #  first col
        ca[i,j] = max(_c(ca,i-1,0,P,Q)[0],euc_dist(P[i],Q[0]))#take max between:
        # 1.recalculate _c at index i-1,0 (last distance calcu) -  next untreated point
        # 2.calculate the dist between the one point of Q and next untreated point of P
    elif i == 0 and j > 0:
        #  first row
        ca[i,j] = max(_c(ca,0,j-1,P,Q)[0],euc_dist(P[0],Q[j]))
    elif i > 0 and j > 0:
        #  more then one col and row
        # check neighbors best way, and take the max between the best way and the real distance
        # to make shore that the path is feasible
        ca[i,j] = max(min(_c(ca,i-1,j,P,Q)[0],_c(ca,i-1,j-1,P,Q)[0],_c(ca,i,j-1,P,Q)[0]),euc_dist(P[i],Q[j]))
    else:
        #  prob to calculate
        ca[i,j] = float("inf")
    return ca[i,j],ca

""" Computes the discrete frechet distance between two polygonal lines
Algorithm: http://www.kr.tuwien.ac.at/staff/eiter/et-archive/cdtr9464.pdf
P and Q are arrays of 2-element arrays (of points - samples of the function)
"""
def frechetDist(P,Q):
    ca = np.ones((len(P),len(Q)))#a matrix of one size: rows- rows of P, col- rows of Q
    ca = np.multiply(ca,-1)#same matrix all values double minus one
    return _c(ca,len(P)-1,len(Q)-1,P,Q)#send ca and index of the last places at ca with P,Q



def matrixMaker(f,n):
    samples = []
    x = sym.symbols('x')
    for i in np.arange(0,n,0.5):
        samples.append([i,f.subs(x,i)])
    print(samples)
    return samples

def Start(func1,func2,approx):
    P = matrixMaker(func1,approx)#taking samples
    Q = matrixMaker(func2,approx)#taking samples
    frec = frechetDist(P,Q)# frec[0] is the leash lenght frec[1] is the distance matrix
    print(frec[0])#the leash min size
    X = ([P[i][0] for i in range(len(P))])
    Py = ([P[j][1] for j in range(len(P))])
    Qy = ([Q[j][1] for j in range(len(Q))])
    plt.plot(X, Py, 'bo')
    plt.plot(X,Py,'b')
    plt.plot(X, Qy, 'bo')
    plt.plot(X,Qy,'b')

    plt.title(frec[0])
    plt.suptitle('frechet distance=')
    flag = [ [0] * len(frec[1])for _ in range(len(frec[1]))]
    flagp = np.zeros(len(P))
    flagq = np.zeros(len(P))

    # give feasible path but not the best one


    for i in range(len(frec[1])):
        for j in range(len(frec[1])):
            if ((frec[1])[i,j]<=frec[0] and flagp[j]==0):
                plt.plot([P[i][0],Q[j][0]],[P[i][1],Q[j][1]],c='tab:grey')
                flagp[j] = 1
            if ((frec[1])[j,i]<=frec[0] and flagq[i]==0):
                plt.plot([P[i][0],Q[j][0]],[P[i][1],Q[j][1]],c='tab:grey')
                flagq[i] = 1
    plt.show()



