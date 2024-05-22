import numpy as np
import matplotlib.pyplot as plt


def roll_dice(num_rolls):
    # Simulation of rolling two dice
    die1 = np.random.randint(1, 7, size=num_rolls)
    die2 = np.random.randint(1, 7, size=num_rolls)
    sums = die1 + die2
    return sums


def calculate_probabilities(sums, num_rolls):
    # Counting the frequency of each sum
    unique, counts = np.unique(sums, return_counts=True)
    probabilities = counts / num_rolls
    return dict(zip(unique, probabilities))


def monte_carlo_simulation(num_rolls):
    sums = roll_dice(num_rolls)
    probabilities = calculate_probabilities(sums, num_rolls)
    return probabilities


def analytical_probabilities():
    # Analytical probabilities for each sum from 2 to 12
    probabilities = {}
    for i in range(2, 13):
        probabilities[i] = (6 - abs(i - 7)) / 36
    return probabilities


def plot_probabilities(monte_carlo_probs, analytical_probs):
    sums = np.arange(2, 13)
    monte_carlo_values = [monte_carlo_probs.get(sum_, 0) for sum_ in sums]
    analytical_values = [analytical_probs[sum_] for sum_ in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums - 0.2, monte_carlo_values, width=0.4, label="Monte Carlo")
    plt.bar(sums + 0.2, analytical_values, width=0.4, label="Analytical")
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability")
    plt.title("Probability of Sums from Rolling Two Dice")
    plt.xticks(sums)
    plt.legend()
    plt.show()


def main():
    num_rolls = 1000000
    monte_carlo_probs = monte_carlo_simulation(num_rolls)
    analytical_probs = analytical_probabilities()
    plot_probabilities(monte_carlo_probs, analytical_probs)


if __name__ == "__main__":
    main()
