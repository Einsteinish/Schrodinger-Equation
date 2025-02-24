import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1.0  # Length of the box
x = np.linspace(0, L, 500)  # Position array from 0 to L
n_max = 5  # Maximum quantum number for the visualization
hbar = 1.0545718e-34  # Reduced Planck constant (in J·s)
m = 9.10938356e-31  # Mass of the electron (in kg)

# Function to calculate energy levels
def energy_level(n):
    return (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

# Set up the figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
fig.suptitle('Particle in a Box: Wavefunction, Probability Density, and Energy Levels', y=0.95)  # Adjust title position

# Plot wavefunctions and probability densities
for n in range(1, n_max + 1):
    # Wavefunction
    psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    ax1.plot(x, psi_n, label=f'n = {n}')
    
    # Probability density
    prob_density = psi_n**2
    ax2.plot(x, prob_density, label=f'n = {n}')

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

# Plot energy levels
n_values = np.arange(0, n_max + 1)  # Quantum numbers from 0 to n_max
E_values = [energy_level(n) for n in n_values]  # Energy values
ax3.plot(n_values, E_values, 'go-', lw=2, label='Energy Levels')  # Energy curve

# Add text annotations for energy levels
for i in range(1, n_max + 1):
    ax3.text(i, E_values[i] + 0.05 * E_values[n_max], f'E_{i} = {E_values[i]:.2e}', fontsize=10, color='g', ha='center')

# Set axis limits and labels for energy levels
ax3.set_xlim(0, n_max)
ax3.set_ylim(0, energy_level(n_max) * 1.1)  # Adjust y-axis limit
ax3.set_xlabel('Quantum Number $n$')
ax3.set_ylabel('Energy $E_n$ (J)')
ax3.grid(True)
ax3.legend()

# Adjust subplot spacing to reduce the gap
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the rect parameter to control spacing

# Display the plot
plt.show()
