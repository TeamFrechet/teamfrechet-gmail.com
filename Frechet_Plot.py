from frechetcalcu import *
from intersection_point import *
def feasible_path(dist,P,Q):
    F = [[0,0]]
    i=0
    j=0
    k=0;
    P1 = [[ P[0][0], P[0][1]]]
    Q1 = [[Q[0][0], Q[0][1]]]
        ##remember to test if j and i both reach the end in general and at similar points.
        ##important future note: keep in mind that the lines may be too small for circle , just a thought, may be relivent later.
    while(i+1<len(P) and j+1<len(Q)):
        if (i+1)<len(P) :
           inter = circle_line_segment_intersection(P[i+1],dist,Q[j],Q[j+1],False)    #the the intersection points between the frech distance and lines of the other curve.
           if inter == []:
               if (j + 1) < len(Q):
                   inter = circle_line_segment_intersection(Q[j + 1], dist, P[i], P[i + 1], False)
                   if inter == []:
                        return print("error")
                   else: j=j+1
                   k = k + 1;
                   F[k] = (F[k-1,0] + euc_dist(P1,inter[0])),F[k-1,1]+euc_dist(Q1[0],Q[j+1])            #distance between the previous point the next point/intersection point.
                   P1[0] = inter[0]
                   Q1[0] = Q[j+1]

           else:
               ## ask the team if there is a point in a min here or if it is even possible , can test for it after plot is added.
               ##if the funcion ends before len(P)==i and len(Q)==j that may mean that min is needed or something is wrong in my thinking
               inter2=circle_line_segment_intersection(Q[j + 1], dist, P[i], P[i + 1], False)
               if inter2 != []:
                    print("other path...")
               i=i+1
               k = k + 1;
               F[k] =  F[k-1,0]+euc_dist(P1[0], P[i + 1]),F[k-1,1]+euc_dist(Q1, inter[0])
               Q1[0] = inter[0]
               P1[0] = P[i + 1]
              ## else: min(inter[0],inter[])



    functionDraw(F,'tab:purple')



P = [[12.8289,228.248],[24.0543,253.104],[46.8761,257.56],[46.3385,242.508],[85.4033,257.023],[97.2302,254.693],[95.6174,215.27],[104.502,233.594],[105.571,215.419]]
Q = [[47.2345,215.27],[48,240],[89.8827,249.659],[67.6065,215.331],[84.9682,200.029],[102.413,190.692],[176.614,216.736],[112.902,213.953]]
dist = frechetDist(P,Q)
dist = dist[0]
feasible_path(dist,P,Q)


