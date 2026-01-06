import numpy as np 
import matplotlib.pyplot as plt

def plot_chessboard(size=8):
    # Generate checkerboard pattern
    board = np.indices((size, size)).sum(axis=0) % 2

    # Define chessboard colors
    cmap = plt.cm.colors.ListedColormap(["#f0d9b5", "#b58863"])

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(board, cmap=cmap, interpolation="nearest")

    # Set ticks and labels
    ax.set_xticks(np.arange(size))
    ax.set_yticks(np.arange(size))
    ax.set_xticklabels([chr(ord('A') + i) for i in range(size)])
    ax.set_yticklabels([str(size - i) for i in range(size)])

    # Draw grid lines
    ax.set_xticks(np.arange(-0.5, size, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, size, 1), minor=True)
    ax.grid(which="minor", color="black", linewidth=1)

    # Remove major tick marks
    ax.tick_params(which='major', bottom=False, left=False)

    plt.title("Chessboard", fontsize=16, fontweight='bold')
    plt.show()

plot_chessboard(8)
