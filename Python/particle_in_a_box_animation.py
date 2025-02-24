import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
L = 1.0  # Length of the box
x = np.linspace(0, L, 500)  # Position array from 0 to L
n_max = 5  # Maximum quantum number for the animation
hbar = 1.0545718e-34  # Reduced Planck constant (in J·s)
m = 9.10938356e-31  # Mass of the electron (in kg)

# Function to calculate energy levels
def energy_level(n):
    return (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

# Set up the figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
fig.suptitle('Particle in a Box: Wavefunction, Probability Density, and Energy Levels', y=0.95)  # Adjust title position

# Initialize empty lines for the wavefunction and probability density
line1, = ax1.plot([], [], lw=2, color='b', label='Wavefunction $\psi_n(x)$')
line2, = ax2.plot([], [], lw=2, color='r', label='Probability Density $|\psi_n(x)|^2$')

# Set axis limits and labels for wavefunction and probability density
ax1.set_xlim(0, L)
ax1.set_ylim(-1.5, 1.5)
ax1.set_ylabel('$\psi_n(x)$')
ax1.grid(True)
ax1.legend()

ax2.set_xlim(0, L)
ax2.set_ylim(0, 3)
ax2.set_xlabel('Position $x$')
ax2.set_ylabel('$|\psi_n(x)|^2$')
ax2.grid(True)
ax2.legend()

# Set up the energy levels plot
ax3.set_xlim(0, n_max)
ax3.set_ylim(0, energy_level(n_max) * 1.1)  # Adjust y-axis limit
ax3.set_xlabel('Quantum Number $n$')
ax3.set_ylabel('Energy $E_n$')
ax3.grid(True)

# Initialize the energy curve
n_values = np.arange(0, n_max + 1)  # Quantum numbers from 0 to n_max
E_values = [energy_level(n) for n in n_values]  # Energy values
line3, = ax3.plot([], [], 'go-', lw=2, label='Energy Levels')  # Energy curve

# Add legend to ax3
ax3.legend()

# Store text annotations
text_annotations = []

# Function to initialize the animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

# Function to update the animation for each frame
def update(n):
    # Wavefunction
    psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    line1.set_data(x, psi_n)
    
    # Probability density
    prob_density = psi_n**2
    line2.set_data(x, prob_density)
    
    # Update the title to show the current quantum number
    fig.suptitle(f'Particle in a Box: n = {n}', y=0.95)  # Adjust title position
    
    # Update the energy curve
    line3.set_data(n_values[:n + 1], E_values[:n + 1])
    
    # Clear previous annotations
    for text in text_annotations:
        text.remove()
    text_annotations.clear()
    
    # Add new text annotations for energy levels
    for i in range(1, n + 1):
        text = ax3.text(i, E_values[i] + 0.05 * E_values[n_max], f'E_{i}', fontsize=10, color='g', ha='center')
        text_annotations.append(text)
    
    # Set y-axis ticks and labels
    ax3.set_yticks(E_values[1:n + 1])
    ax3.set_yticklabels([f'E_{i}' for i in range(1, n + 1)])
    
    return line1, line2, line3

# Adjust subplot spacing to reduce the gap
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the rect parameter to control spacing

# Create the animation
ani = FuncAnimation(
    fig,  # Figure to animate
    update,  # Update function
    frames=range(1, n_max + 1),  # Quantum numbers from 1 to n_max
    init_func=init,  # Initialization function
    blit=True,  # Optimize for smoother animation
    interval=1000,  # Delay between frames in milliseconds
    repeat=True  # Loop the animation
)

# Save the animation as an MP4 file
ani.save('particle_in_a_box_animation.mp4', writer='ffmpeg', fps=1, dpi=200)

# Display the animation (optional)
plt.show()
