import matplotlib
import matplotlib.pyplot as plt
import numpy as np

mag = list()
dist = list()
power = list()

def graph_menu(x,mag,dist,power)):
    print("\nWould you like to plot:")
    print("(1) Both graphs")
    print("(2) Force diagram")
    print("(3) Bending moment diagram")
    graphchoice = input("")
    if graphchoice == "1":
        force(x,mag,dist,power))
        bend(x,mag,dist,power))
    elif graphchoice == "2":
        force(x,mag,dist,power))
    elif graphchoice == "3":
        bend(x,mag,dist,power))
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
    x = np.linspace(0,xend,num=100)
    print(x)
    graph_menu(x,mag,dist,power))

def force(x,mag,dist,power):
    print(x)
    y = np.linspace()
    plt.plot(x,)
    plt.show()


main_menu()