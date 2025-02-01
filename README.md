# Monte Carlo Pi Estimation Visualization

This project provides a dynamic and interactive visualization of estimating the value of π (Pi) using the Monte Carlo method. The user can specify the number of random points to be used for the estimation, and the animation will visually demonstrate the process in real-time, showing which points fall inside and outside of the unit circle.

## Introduction

Monte Carlo methods are a class of computational algorithms that rely on repeated random sampling to obtain numerical results. In this project, the Monte Carlo method is used to estimate the value of π by generating random points in a square and determining how many fall inside a unit circle inscribed within the square. This approach is simple yet powerful, and it showcases the effectiveness of randomness in approximation.

## Features

- **Interactive Visualization**: Real-time animation of points being plotted to estimate π.
- **User Input**: Specify the number of points for the simulation.
- **Dynamic Plot Updates**: See how the estimated value of π converges as more points are added.
- **Color-Coded Points**: Points inside the circle are displayed in blue, and points outside are in red.
- **Final Result Display**: The estimated value of π is displayed on the plot after the simulation completes.

## How It Works

The Monte Carlo method for estimating π uses the following approach:

1. Generate random points within a square that bounds a unit circle (centered at the origin, with a radius of 1).
2. Count how many of those points fall inside the circle.
3. Use the ratio of the points inside the circle to the total points to estimate π:
   
   \[
   \text{Estimated } \pi = 4 \times \frac{\text{Number of points inside circle}}{\text{Total number of points}}
   \]

The simulation visualizes this process, updating the plot dynamically as points are generated.

## Installation

### Requirements

- **Python** 3.6+
- **NumPy** (for numerical calculations)
- **Matplotlib** (for visualization)
- **tqdm** (for progress bar visualization)
