#!/usr/bin/python3

# python3 -m pip install matplotlib
import matplotlib
# from python std library
import csv

# python3 -m pip install np
import numpy as np
matplotlib.use('Agg')
# sudo apt install python3-tk
import matplotlib.pyplot as plt


def main():

    # style your graph
    plt.style.use('bmh')
    # creates sequences of evenly spaced numbers
    x = np.linspace(0, 5)

    # generates pseudo-random numbers for random processes
    np.random.seed(19680801)
    # returns a figure instance and an object or an array of Axes objects
    fig, ax = plt.subplots()

    # plots a curve having the form of a sine wave
    ax.plot(x, np.sin(x) + x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) - 2 * x + np.random.randn(50))
    ax.plot(x, np.sin(x) + np.random.randn(50))
    # sets title
    ax.set_title("Number of...")


    # SAVE the graph locally
    plt.savefig("/home/student/mycode/graphing/graph.png")
    # Save to "~/static"
    plt.savefig("/home/student/static/graph.png")
    print("Graph created.")

if __name__ == "__main__":
    main()
