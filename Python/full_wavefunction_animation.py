import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
L = 1.0  # Length of the box
hbar = 1.0  # Reduced Planck constant (set to 1 for simplicity)
m = 1.0  # Mass of the particle (set to 1 for simplicity)

# Spatial grid
x = np.linspace(0, L, 500)

# Time grid (common for all n)
t_max = 4 * np.pi * hbar / ((1**2 * np.pi**2 * hbar**2) / (2 * m * L**2))  # Period for n=1
t = np.linspace(0, t_max, 200)

# Wavefunction components
def psi_n(x, n):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def real_part(x, t, n):
    E_n = (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)
    return psi_n(x, n) * np.cos(E_n * t / hbar)

def imaginary_part(x, t, n):
    E_n = (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)
    return -psi_n(x, n) * np.sin(E_n * t / hbar)

# Create the figure and subplots
fig, axes = plt.subplots(5, 1, figsize=(10, 15))
fig.suptitle('Real and Imaginary Parts of Ψₙ(x, t) for n = 1, 2, 3, 4, 5', y=1.02)

# Initialize empty lines for real and imaginary parts
lines_real = []
lines_imag = []
subplot_titles = []
for i, n in enumerate(range(1, 6)):
    ax = axes[i]
    ax.set_xlim(0, L)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Wavefunction")
    ax.grid(True)
    
    # Add subplot title (n=1, n=2, ..., n=5) in the top-right corner
    subplot_title = ax.text(0.95, 0.90, f"n = {n}", transform=ax.transAxes, 
                            fontsize=12, verticalalignment='top', horizontalalignment='right',
                            bbox=dict(facecolor='white', alpha=0.8))
    subplot_titles.append(subplot_title)
    
    # Initialize lines for real and imaginary parts
    line_real, = ax.plot([], [], label="Re(Ψₙ(x, t))", color="blue")
    line_imag, = ax.plot([], [], label="Im(Ψₙ(x, t))", color="red")
    lines_real.append(line_real)
    lines_imag.append(line_imag)
    
    # Place the legend outside the plot
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

# Adjust layout to make space for the legend
plt.tight_layout()

# Animation function
def animate(frame):
    # Current time
    current_t = t[frame]
    
    # Update real and imaginary parts for each n
    for i, n in enumerate(range(1, 6)):
        y_real = real_part(x, current_t, n)
        y_imag = imaginary_part(x, current_t, n)
        lines_real[i].set_data(x, y_real)
        lines_imag[i].set_data(x, y_imag)
    
    return lines_real + lines_imag + subplot_titles

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=50, blit=True)

# Save the animation as an MP4 file
ani.save('full_wavefunction_animation.mp4', writer='ffmpeg', fps=30, dpi=200)

# Show the animation
plt.show()
