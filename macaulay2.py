from sympy.physics.continuum_mechanics.beam import Beam
from sympy import *
from sympy import init_printing
init_printing() 
E, I = symbols('E, I')

def graph_choice(b):
    print("Type 'y' to plot the shear force and bending moment graphs.")
    if input("") == 'y':
        b.plot_shear_force()
        b.plot_bending_moment()
    else:
        graph_choice(b)
def menu():
    print("Welcome to the Macaulay notation plotter.")
    print("How long is the beam?")
    xend = int(input(""))
    b = Beam(xend, E, I)
    print("How many forces are acting upon the beam?")
    num_forces = int(input(""))
    for x in range(num_forces):
        print("\nForce number " + str(x+1) + ":")
        print("What's the magnitude of the force? (Convention is upwards being positive.)")
        mag = int(input(""))
        print("How far along the beam is the force?")
        dist = int(input(""))
        print("What's the power?")
        power = int(input(""))
        b.apply_load(mag, dist, power-1)
    print("The Macaulay equation for the beam is:")
    pprint(b.shear_force())
    graph_choice(b)

menu()
