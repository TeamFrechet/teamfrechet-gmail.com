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
    f = m * (x - point1[0]) + point2[1]
    return [f,m]


# P becomes the X-axis Q becomes Y-axis
def pathLimit(P,Q,path_jump):
    frecht_distance = frechetcalcu.frechetDist(P,Q)
    X = ([P[j][1] for j in range(len(P))])
    Y = ([Q[j][1] for j in range(len(Q))])
    Ppath = [P[0]]
    Qpath = [Q[0]]
    # temp path on P,Q straight lines

    path = []
    # final common path of P and Q

    #should think of a differnt idea!!
    counter = [P[0][0],Q[0][0]]
    # for making Ppath ,Qpath

    x = sym.symbols('x')
    # to use straightLine function

    n = len(P)
    for i in range(1,n):
        mp = straightLine(P[i - 1],P[i])[1]
        f = straightLine(P[i - 1],P[i])[0]
        mq = straightLine(Q[i - 1],Q[i])[1]
        g = straightLine(Q[i - 1],Q[i])[0]
        print('f',f,'g',g)
        while True:
            if mp == 0:
                # f = const
                Ppath.append([counter[0], f])
            else:
                Ppath.append([counter[0],f.subs(x,counter[0])])
            if mq == 0:
                # g = const
                Qpath.append([counter[1], g])
            else:
                Qpath.append(([counter[1],g.subs(x,counter[1])]))
            counter[0] += path_jump
            counter[1] += path_jump
            if(frechetcalcu.frechetDist(Ppath, Qpath)[0] > frecht_distance[0]) or counter[0] >= P[i][1] or counter[1] >= Q[i][1]:
                # breack when:
                # the frechet distance between current chosen lines, is bigger then the leash or is one of the shpits
                break
        # here should save the two curve that good for current frechet distance - Ppath,Qpath
        if counter[0] >= P[i][1] and counter[1] < Q[i][1]:
            # got to the spitz P point
            counter[0] = P[i][1]
            path.append([Ppath[0], Qpath[0]])
            if mq == 0:
                path.append([counter[0],g])
            else:
                path.append([counter[0],g.subs(x,counter[1])])
        elif counter[1] >= Q[i][1] and counter[0] < P[i][1]: # got to the spitz Q point
            counter[1] = Q[i][1]
            path.append([Ppath[0][1], Qpath[0][1]])
            if mp == 0:
                path.append([f, counter[1]])
            else:
                path.append([f.subs(x, counter[0]),counter[1]])
        else:
            # got to the spitz of both P and Q points
            path.append([Ppath[0][1], Qpath[0][1]])
            path.append([P[i][1],Q[i][1]])
        Ppath = [Ppath[len(Ppath)-1]]
        Qpath = [Qpath[len(Qpath)-1]]
    for i in range(1,len(path)):
        print()
        plt.plot([path[i-1][0],path[i][0]],[path[i-1][1],path[i][1]],'y')
    plt.suptitle('common path')
    plt.show()
