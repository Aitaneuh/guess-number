from matplotlib import pyplot as plt

def generate_graphs(simulations, guesses):
    plt.plot(simulations, guesses)
    plt.grid(True)
    plt.title('Average Number of Guesses vs Range Size')
    plt.xlabel('Range of the random number')
    plt.ylabel('Average number of guesses')
    plt.show()