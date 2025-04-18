import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt  # Corrected import

def IsEven(n):
    if (n % 2 == 0):
        return True
    else:
        return False

def ThreeXPlus1(x, sols):
    if x == 1:
        sols.append(1)
        return 1
    sols.append(x)
    if IsEven(x):
        return ThreeXPlus1(x // 2, sols)
    else:
        return ThreeXPlus1(3 * x + 1, sols)

def main():
    sols = []
    start_value = int(input("Enter a starting value for the 3x+1 sequence: "))
    ThreeXPlus1(start_value, sols)

    # Visualization
    plt.figure(figsize=(12, 8))
    plt.plot(range(len(sols)), sols, marker='o', linestyle='-', color='b', label='3x+1 Sequence')

    # Annotate points, excluding the first and last points
    for i in range(1, len(sols) - 1):
        plt.text(i, sols[i], str(sols[i]), fontsize=8, ha='right', va='bottom')

    # Highlight the starting point
    plt.scatter(0, sols[0], color='green', s=100, label='Start Point')  # Start
    plt.text(0, sols[0], str(sols[0]), fontsize=8, ha='right', va='bottom')

    # Highlight the ending point
    plt.scatter(len(sols) - 1, sols[-1], color='red', s=100, label='End Point')  # End
    plt.text(len(sols) - 1, sols[-1], str(sols[-1]), fontsize=8, ha='right', va='bottom')

    # Add a horizontal line at y=1
    plt.axhline(y=1, color='gray', linestyle='--', linewidth=1, label='Convergence Point (y=1)')

    # Add title and labels
    plt.title(f"Detailed 3x+1 Sequence Starting from {start_value}", fontsize=16)
    plt.xlabel("Step", fontsize=12)
    plt.ylabel("Value", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()