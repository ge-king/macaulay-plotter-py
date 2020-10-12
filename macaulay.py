import matplotlib
import matplotlib.pyplot as plt
import numpy as np

mag = list()
dist = list()
power = list()

def graph_menu(x,mag,dist,power,xend,num_forces):
    print("\nWould you like to plot:")
    print("(1) Both graphs")
    print("(2) Force diagram")
    print("(3) Bending moment diagram")
    graphchoice = input("")
    if graphchoice == "1":
        force(x,mag,dist,power,xend,num_forces)
        bend(x,mag,dist,power,xend,num_forces)
    elif graphchoice == "2":
        force(x,mag,dist,power,xend,num_forces)
    elif graphchoice == "3":
        bend(x,mag,dist,power,xend,num_forces)
    else:
        print("Error - choose from 1-3.")
        graph_menu()

def main_menu():
    print("Welcome to the Macaulay notation plotter.")
    print("How many forces are acting upon the beam?")
    num_forces = int(input(""))
    for x in range(num_forces):
        print("\nForce number " + str(x+1) + ":")
        print("What's the magnitude of the force? (Convention is upwards being positive.)")
        mag.append(int(input("")))
        print("How far along the beam is the force?")
        dist.append(int(input("")))
        print("What's the power?")
        power.append(int(input("")))

    print("\nWhere would you like the graph to end along the x axis?")
    xend = int(input(""))
    graph_menu(x,mag,dist,power,xend,num_forces)

def force(x,mag,dist,power,xend,num_forces):
    print(dist)
    if dist[0] != 0:
        x = np.linspace(0,dist[0],num=50)
        y = 0*x
        plt.plot(x,y)
        if power[0] == 0:
            y = np.linspace(0,mag[0],num=50)
            x = 0*y+dist[0]
            plt.plot(x,y)
    for k in range(0,num_forces-1):
        x = np.linspace(dist[k],dist[k+1],num=50)
        y = mag[k]*(x-dist[k])**power[k]
        plt.plot(x,y)
    x = np.linspace(dist[num_forces-1],xend,num=50)
    y = mag[num_forces-1]*(x-dist[num_forces-1])**power[num_forces-1]
    plt.plot(x,y)
    plt.show()    


main_menu()
