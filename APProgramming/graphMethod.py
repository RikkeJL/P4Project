import matplotlib.pyplot as plt


def plotGraph(soundwave, soundwave2, time):
    plt.figure(figsize=(12, 5))  # sets the size of the figure in inches
    plt.plot(time, soundwave2, lineWidth=2, label="Sound Effect")  # plots the soundwave with effect input
    plt.plot(time, soundwave, linestyle='dashed', lineWidth=2, label="original sound")  # plots the soundwave without input
    plt.xlim((time[30], time[20000]))  # Sets the limit of the x-axis
    plt.ylim((-0.4, 0.32))  # Sets the limit of the x-axis
    plt.xlabel('$t$ [s]')  # Sets the label for the x-axis
    plt.ylabel('$x(t)$ [Pa]')  # sets the label for the y-axis
    plt.legend()  # Makes the labels appear in the plot
    plt.grid(True)  # sets there to be a grid in the graph
    plt.show()  # Shows the graph.
