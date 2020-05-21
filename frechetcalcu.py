import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import math
import numpy as np
import sympy as sym

# This class only computes the discrete frechet distance between two polygonal lines
# Using algorithm: http://www.kr.tuwien.ac.at/staff/eiter/et-archive/cdtr9464.pdf

def euc_dist(pt1,pt2):
    #  return dist of the 2 point sended
    return math.sqrt((pt2[0]-pt1[0])*(pt2[0]-pt1[0])+(pt2[1]-pt1[1])*(pt2[1]-pt1[1]))


# calculate frechet distance
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
        # more then one col and row are filled
        # check neighbors best way, and take the max between the neighbors best way and the real distance
        # explanation why take the max: (same explanation for all conditions use max)
        # if distance is smaller then neighbors take the min neighbors distance - so the leash wont tear for neighbors
        # else if distance is bigger then neighbors take the real distance - so the leash wont tear for current points
        # to make shore that the path is feasible
        ca[i,j] = max(min(_c(ca,i-1,j,P,Q)[0],_c(ca,i-1,j-1,P,Q)[0],_c(ca,i,j-1,P,Q)[0]),euc_dist(P[i],Q[j]))
    else:
        #  error
        ca[i,j] = float("inf")
    return ca[i,j],ca


# P and Q are arrays of 2-element arrays (of points - samples of the function)
def frechetDist(P,Q):
    ca = np.ones((len(P),len(Q)))
    # a matrix of one size: rows- rows of P, col- rows of Q
    ca = np.multiply(ca,-1)
    # same matrix all values double minus one
    return _c(ca,len(P)-1,len(Q)-1,P,Q)
    # send ca and index of the last places at ca with P,Q



