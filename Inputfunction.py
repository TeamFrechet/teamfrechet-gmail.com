import matplotlib.pyplot as plt
import math
import numpy as np
import sympy as sym
import frechetcalcu
import curvesTrack as track

# this class is the main class
# use for input P,Q by user
# this class also contain a function use for symbol curve to calculate frechet distance - not part of the final project
# to use it approach main directly
# use frechetcalcu to calculate the distance and curvesTrack to calculate and plot the path between the two curves

# function draw
# can use for all P matrix
# do not forget to use plt.show() after using this function!
def functionDraw(P,color): # P matrix 2 x n #color = tab:green
    n = len(P)
    for i in range(1,n):
        plt.plot([P[i-1][0],P[i][0]],[P[i-1][1],P[i][1]],c=color)


# symbol function O N L Y
# useless for track calculate with points
###############################
def symbolFunction():

    #chose here the function
    x = sym.symbols('x')
    func1 = x+2 # P
    func2 = sym.sin(x)# Q
    return [func1,func2]


# symbol function O N L Y
# useless for track calculate with points
###############################
def matrixMaker(f,n,jump):
    samples = []
    x = sym.symbols('x')
    for i in np.arange(0,n,jump):
        samples.append([i,f.subs(x,i)])
    print(samples)
    return samples


# research
# symbol function O N L Y
# useless for track calculate with points
###############################
def drawDistanceSamples(func1,func2,approx,jump):
    P = matrixMaker(func1,approx,jump) # for taking samples - non polygonal curves
    Q = matrixMaker(func2,approx,jump) # for taking samples - non polygonal curves
    # P = [[1, 1], [2, 1], [2, 2]]
    # Q = [[2, 2], [0, 1], [2, 4]]
    frec = frechetcalcu.frechetDist(P,Q) # frec[0] is the leash length frec[1] is the distance matrix
    print('leash size', frec[0]) # the leash size
    X = ([P[i][0] for i in range(len(P))])
    Py = ([P[j][1] for j in range(len(P))])
    Qy = ([Q[j][1] for j in range(len(Q))])
    plt.plot(X, Py, 'bo')
    plt.plot(X,Py,'b')
    plt.plot(X, Qy, 'bo')
    plt.plot(X,Qy,'b')

    plt.title(frec[0])
    plt.suptitle('frechet distance=')
    flagp = np.ones(len(P))
    flagq = np.ones(len(P))
    flagp = np.multiply(flagp,-1)
    flagq = np.multiply(flagq,-1)

    # give feasible path but not the best one

    for i in range(len(frec[1])):
        for j in range(len(frec[1])):
            if ((frec[1])[i, j] <= frec[0] and flagp[i] == -1):
                plt.plot([P[i][0], Q[j][0]], [P[i][1], Q[j][1]], c='tab:grey')
                flagp[i] = j
                flagq[j] = i
    for i in range(len(frec[1])):
        for j in range(len(frec[1])):
            if (((frec[1]).transpose())[i,j] <= frec[0] and flagq[i] == -1 and flagp[i]!=j):
                plt.plot([P[j][0], Q[i][0]], [P[j][1], Q[i][1]], c='tab:green')
                flagq[i] = j
    plt.show()




if __name__ == '__main__':

    # use this code if you want to use samples matrix

    # aproxximate = 5
    # samples_jump = 0.5
    # P = symbolFunction()[0]
    # Q = symbolFunction()[1]
    # drawDistanceSamples(P,Q,aproxximate,samples_jump)

    # use this code if you wat to use points

    # draw the curves
    P = [[12.8289,228.248],[24.0543,253.104],[46.8761,257.56],[46.3385,242.508],[85.4033,257.023],[97.2302,254.693],[95.6174,215.27],[104.502,233.594],[105.571,215.419]]
    Q = [[47.2345,215.27],[48,240],[89.8827,249.659],[67.6065,215.331],[84.9682,200.029],[102.413,190.692],[176.614,216.736],[112.902,213.953]]
    R = [[27.25,300.27],[41,320],[60.8827,352.65],[40.6,300.3],[60,300.02],[89.4,170],[101.1,104.7],[107.9,142.953]]
    #P = [[0,0],[1,1],[2,2],[3,3]]
    #Q = [[0,0.25],[1,1.25],[2,2.25],[3,3.25]]
    #R = [[0,0.5],[1,1.5],[2,2.5],[3,3.5]]
    functionDraw(P,'tab:blue')
    functionDraw(Q,'tab:red')
    # frechet diatance for 2 curves
    frec_P_Q = frechetcalcu.frechetDist(P,Q)  # frec[0] is the leash lenght frec[1] is the distance matrix
    plt.title(frec_P_Q[0])
    plt.suptitle('frechet distance between P&Q=')


    plt.figure()

    ######## continue from here ########
    #track.free_space_area(P,Q,frec_P_Q[0])
    #track.pathLimit(P,Q,3) # function in curvesTrack class for calculate the path
    # this function is not right!! itay on the frechet path. do not use curvesTrack
    functionDraw(P,'tab:blue')
    functionDraw(Q,'tab:red')
    functionDraw(R,'tab:green')
    # frechet diatance for 3 curves
    plt.title(frechetcalcu.multiple_frechetDist(P,Q,R)[0])
    plt.suptitle('frechet distance between P&Q&R=')
    print(frechetcalcu.multiple_frechetDist(P,Q,R)[0])
    print(frechetcalcu.frechetDist(P,R)[0])
    print(frechetcalcu.frechetDist(Q,R)[0])
    plt.show()
