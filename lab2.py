import math
import numpy as np
import tools
import Point
dimention=3


# def antigrad(x):
#     return 2*x
#example!!!!
#d( ln(1+exp( w*(3x+9y) ))) /dx=
### (3w * exp(..) )/(1 + exp(...))
#
#

#### print(grad(antigrad,begin,0.002))

begin=np.array([3,3])
center_0=(-5,-5 ,5)
center_1=(5,5,-6)
if __name__ == '__main__':
    #set Coords
    my_points=list()
    for i in Point.generatePoints(100, +1, 3, center_0, dimention=dimention):
        my_points.append(i)
    for i in Point.generatePoints(100, -1, 3, center_1, dimention=dimention):
        my_points.append(i)

    #set func
    def Q(W = np.zeros((dimention,1)) ):
        ans=0
        for point in range(len(my_points)):
            #get exp in func
            scalarMult=0
            for dim in range(dimention):
                scalarMult+= my_points[point].coords[dim] * W[dim]
            scalarMult*=my_points[point].weight

            ans+=math.log1p(1+math.exp(scalarMult))
        return ans

    # set Antigrad
    def antigrad(W):
        ans=np.zeros((dimention,1))

        #get exp -(x01*y0*exp(-y0*(w01*x01 + w02*x02 + w03*x03)))/(exp(-y0*(w01*x01 + w02*x02 + w03*x03)) + 1);

        for dim in range(dimention):
            #get exp
            for point in range(len(my_points)):
                loc_exp=0
                for loc_dim in range(dimention):
                    loc_exp=+my_points[point].coords[loc_dim]*W[loc_dim]*my_points[point].weight
                loc_ai=my_points[point].coords[dim]*my_points[point].weight*math.exp(loc_exp)/(1+math.exp(loc_exp))
                ans[dim]+=loc_ai
        return ans

    c=1;k=1
    begin=[[c],[k],[2.0]]
    answer=tools.grad(antigrad,np.array(begin),epsilon=0.02,showSteps=True)
    print(answer)
        #HERE IS PLOTTER

    plotter = tools.plotter()
    x=list();y=list();w=list()
    for i in range(len(my_points)):
        x.append(my_points[i].coords[0])
        y.append(my_points[i].coords[1])
        w.append(my_points[i].weight)
    plotter.plot_point(x,y,w)
    #ans
    x=np.linspace(center_0[0] , center_1[0] , 15)
    y=[answer[1]*i+answer[0] for i in x]
    plotter.plot_func(x, y, "yellow")
    #begin
    x = np.linspace(center_0[0], center_1[0], 15)
    y = [c* i + k for i in x]
    plotter.plot_func(x, y, "red")

    plotter.show()
