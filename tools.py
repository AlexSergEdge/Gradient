import math
import numpy as np
import matplotlib.pyplot as plt


def grad(antigrad,Xbeg=np.array,epsilon=0.02,jump=0.2,showSteps=False):
    dim=len(Xbeg)
    x_i=Xbeg
    x_p=2*x_i

    def step():
        err = 0
        for i in range(dim):
            err = err+((x_i[i]-x_p[i]) * (x_i[i]-x_p[i]))
        return err

    index=0
    while (step()>epsilon and index<7000):
        x_p=x_i
        x_i=x_i-jump*antigrad(x_i)
        if(showSteps):
            index+=1
            print("x_i="+str(x_i)+"  index="+str(index)+"  grad="+str(antigrad(x_i)))


    return x_i

def norm_vec(vector=np.array):
    sum=0
    for i in vector:
        sum+=i*i
    sum=math.sqrt(sum)
    return sum

class plotter:

    def plot_point(self,X=np.array, Y=np.array, W=np.array):
        for i in range(len(X)):
            if (W[i] == 1):
                plt.scatter(X[i], Y[i],c="red",s=50)
            else:
                plt.scatter(X[i], Y[i],c="blue",s=50)
    def plot_func(self,X,Y,color):
        if color == "yellow":
            plt.plot(X,Y,c="yellow",label="ccc")
        if color == "red":
            plt.plot(X, Y, c="red", label="ccc")
    def show(self):
        plt.show()








