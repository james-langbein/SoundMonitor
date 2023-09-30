import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint


def static_data():
    # data
    data_lst = [60, 59, 49, 51, 49, 52, 53]

    # create the figure and axis objects
    fig, ax = plt.subplots()

    # plot the data and customize
    ax.plot(data_lst)
    ax.set_xlabel('Day Number')
    ax.set_ylabel('Temperature (*F)')
    ax.set_title('Temperature in Portland, OR over 7 days')

    # save and show the plot
    fig.savefig('static_plot.png')
    plt.show()


def animated_data():
    # function that draws each frame of the animation
    def animate(i):
        pt = randint(1, 9)  # grab a random integer to be the next y-value in the animation
        x.append(i)
        y.append(pt)

        ax.clear()
        ax.plot(x, y)
        ax.set_xlim([0, 20])
        ax.set_ylim([0, 10])

    # empty lists for x and y data
    x = []
    y = []

    # create the figure and axes objects
    fig, ax = plt.subplots()

    ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)
    plt.show()


def live_plot_from_file():
    # animation function
    def animate(i):
        with open('live_plot_from_file_data.csv', 'r') as f:
            for line in f:
                data.append(int(line.strip()))
        ax.clear()
        ax.plot(data[-5:])  # plot the last 5 data points

    # initial data
    data = [3, 6, 2, 1, 8]

    # create figure and axes objects
    fig, ax = plt.subplots()

    # call the animation
    ani = FuncAnimation(fig, animate, interval=1000)

    # show the plot
    plt.show()


if __name__ == '__main__':
    live_plot_from_file()
