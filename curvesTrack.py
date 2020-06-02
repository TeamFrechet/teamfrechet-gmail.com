import matplotlib.pyplot as plt
import math
import numpy as np
import sympy as sym
import frechetcalcu
import Inputfunction as inputf


##### this function isnt finish yet!!!#####
############## should fix it ##############

# class for calculate and plot the final path

# return [straight line between them, gradient]
def straightLine(point1,point2):
    # input: point1,2 = [x,y]
    x = sym.symbols('x')
    if (point1[0] - point2[0]) == 0:
        # to solve math error
        m = 0
    else:
        m = (point1[1] - point2[1]) / (point1[0] - point2[0])
    f = m * (x - point1[0]) + point1[1]
    return [f,m]

# function to setting pivot axis
def make_pivot(P):# working good
    pivot =[0]
    dist = 0
    for i in range(1,len(P)):
        dist += frechetcalcu.euc_dist(P[i-1],P[i])
        pivot.append(dist)

    return pivot

#function to show pivot grid
def grid_show(X,Y):
    plt.xlim((X[0], X[len(X) - 1]))
    plt.ylim((Y[0], Y[len(Y) - 1]))
    plt.xticks(X)
    plt.yticks(Y)
    plt.grid(True)
    
    
# this function is not finished yet and have some bugs
def free_space_area(P, Q,epsilon):

    X = make_pivot(P)
    Y = make_pivot(Q)
    plt.xlabel('P')
    plt.ylabel('Q')
    grid_show(X,Y)


    # from here i have bugs!!!!!!!
    jump = 0.9
    counter = [P[0][0],Q[0][0]]
    P_lines = []
    Q_lines = []
    good_space = []
    X_couter = X[0]
    Y_couter = Y[0]
    # line array of P and Q

    for i in range(1,len(P)-1):
        mp = straightLine(P[i -1], P[i])[1]
        f = straightLine(P[i - 1], P[i])[0]
        mq = straightLine(Q[i - 1], Q[i])[1]
        g = straightLine(Q[i - 1], Q[i])[0]
        P_lines.append([P[i-1],f,mp])
        Q_lines.append([Q[i-1],g,mq])
    for i in range(1,len(Q)-1):
        while Y[i-1]>=Y_couter:
            for j in range(1,len(P)-1):
                while X[j]>=X_couter:
                    if frechetcalcu.euc_dist([counter[1],Q_lines[i-1][1].subs('x',counter[1])],[counter[0],P_lines[j-1][1].subs('x',counter[0])]) < epsilon:
                        good_space.append([X_couter,Y_couter])
                    if P_lines[j-1][2] > 0:
                        counter[0] += jump
                        X_couter += frechetcalcu.euc_dist([counter[0]-jump, P_lines[j - 1][1].subs('x', counter[0]-jump)],[counter[0], P_lines[j - 1][1].subs('x', counter[0])])
                    else:
                        counter[0] -= jump
                        X_couter += frechetcalcu.euc_dist([counter[0]+jump, P_lines[j - 1][1].subs('x', counter[0]+jump)],[counter[0], P_lines[j - 1][1].subs('x', counter[0])])
                counter[0] = P[j][0]
                X_couter = X[j]
            if Q_lines[i-1][2] > 0:
                Y_couter += frechetcalcu.euc_dist([counter[1]-jump, Q_lines[i - 1][1].subs('x', counter[1]-jump)], [counter[1], Q_lines[i - 1][1].subs('x', counter[1])])
                counter[1] += jump
            else:
                Y_couter += frechetcalcu.euc_dist([counter[1]+jump, Q_lines[i - 1][1].subs('x', counter[1]+jump)], [counter[1], Q_lines[i - 1][1].subs('x', counter[1])])
                counter[1] -= jump
            X_couter = X[0]
        Y_couter = Y[i]
        counter[0] = Q[i][0]

    xscat = [good_space[i][0] for i in range(len(good_space))]
    yscat = [good_space[i][1] for i in range(len(good_space))]
    plt.scatter(xscat,yscat,s=jump*100)


#itay! it you mission to start from here!
def pathLimit(P,Q,path_jump):

    return
