import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(num_points):
    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)
    
    inside_circle = x**2 + y**2 <= 1
    
    pi_estimate = 4 * np.sum(inside_circle) / num_points
    
    return pi_estimate, x, y, inside_circle

n_values = [100, 1000, 10000,1000000]

for n in n_values:
    pi_estimate, x, y, inside_circle = estimate_pi(n)
    
    print(f"Estimate of π with {n} points: {pi_estimate}")
    
    # Plot the points
    plt.figure(figsize=(6, 6))
    plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside Circle')
    plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Monte Carlo Estimation of π with {n} Points\nπ ≈ {pi_estimate}")
    plt.legend()
    plt.axis("equal")
    plt.show()
