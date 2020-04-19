#!/Users/josephkloiber/anaconda3/bin/python3

# levels in this script refer to the number of steps in a factor 
# specific to the terminology we use in Formal Design of Experiments

import numpy as np
import matplotlib.pyplot as plt

def popluate_circle(radius):
    points = np.zeros([360,2])
    for step in range(0,360,1):
        points[step] = [radius*np.cos(np.radians(step)), radius*np.sin(np.radians(step))]
    return(points)

def populate_square(radius):
    points = np.zeros([5, 2])
    points[0] = [-radius, -radius]
    points[1] = [radius, -radius]
    points[2] = [radius, radius]
    points[3] = [-radius, radius]
    points[4] = [-radius, -radius]
    return(points)

def monte_carlo_points_2d(levels, radius):
    # sample count number of random points inside a square of dimensions 2R
    return  np.random.rand(levels,2) * (2 * radius) - radius

def latin_square_points_2d(levels, radius):
    # Compute the main diagonal of points
    pitch = (2 * radius) / levels
    points = np.zeros([levels,2])
    bgn = -radius + (0.5 * pitch)
    x_file = np.random.permutation(levels) # X's
    y_rank = np.random.permutation(levels) # Y's
    for level in range(levels):
         points[level] = [bgn+x_file[level]*pitch, bgn+y_rank[level]*pitch]
    return points

def count_encricled_points(levels, points):
    magnitude=np.power(np.power(points[:,0], 2) + np.power(points[:,1], 2), 0.5)
    return np.size(np.where(magnitude <= 1))

# set the geometrical bounds the example
samples = 1000
radius = 4

mc_points = []
mc_pi_est_var = []
ls_pi_est_var = []

square_points = populate_square(radius)
circle_points = popluate_circle(radius)

################################################################################
# Build and show the Monte Carlo points

plt.figure(1)
plt.xlim(-radius, radius)
plt.ylim(-radius, radius)
plt.title("1000 Random Samples Monte Carlo Sampling")
plt.xlabel("Width")
plt.ylabel("Height")
plt.axis('equal')

mc_points = monte_carlo_points_2d(samples, radius)
plt.plot(mc_points[:,0], mc_points[:,1], 'bo', label='Monte Carlo')
plt.plot(square_points[:,0], square_points[:,1], 'r-', linewidth=5)
plt.plot(circle_points[:,0], circle_points[:,1], 'g-', linewidth=5)
################################################################################

################################################################################
# Build and show the latin square points

plt.figure(2)
plt.xlim(-radius, radius)
plt.ylim(-radius, radius)
plt.title("1000 Random Samples Latin Square Sampling")
plt.xlabel("Width")
plt.ylabel("Height")
plt.axis('equal')

mc_points = monte_carlo_points_2d(samples, radius)
plt.plot(mc_points[:,0], mc_points[:,1], 'ko', label='Monte Carlo')
plt.plot(square_points[:,0], square_points[:,1], 'r-', linewidth=5)
plt.plot(circle_points[:,0], circle_points[:,1], 'g-', linewidth=5)
################################################################################

################################################################################
# Let sample count increase and estimate pi each time using MC

plt.figure(3)
plt.title("Monte Carlo Pi Estimates Over Increasing Sample Count")
plt.ylim(0, 4)
plt.xlabel("Sample Count")
plt.ylabel("Esitmate")
mc_pi_estimates = []
for count in range(1,1001):
    mc_points = monte_carlo_points_2d(count, 1)
    mc_pi_estimates.append(4* count_encricled_points(count, mc_points) / count)
    mc_pi_est_var.append(np.var(mc_pi_estimates[0:count]))
plt.plot(mc_pi_estimates, label='Estimate of Pi')
truth = np.zeros([2, 2])
truth[0] = ([0, np.pi])
truth[1] = ([1001, np.pi])
plt.legend(loc='lower left')
plt.plot(truth[:,0], truth[:,1], 'r-', label='Pi Truth')
################################################################################

################################################################################
# Let sample count increase and estimate pi each time using LS

plt.figure(4)
plt.title("Latin Square Pi Estimates Over Increasing Sample Count")
plt.ylim(0, 4)
plt.xlabel("Sample Count")
plt.ylabel("Esitmate")
ls_pi_estimates = []
for count in range(1,1001):
    ls_points = latin_square_points_2d(count, 1)
    ls_pi_estimates.append(4* count_encricled_points(count, ls_points) / count)
    ls_pi_est_var.append(np.var(ls_pi_estimates[0:count]))
plt.plot(ls_pi_estimates, 'k', label='Estimate of Pi')
truth = np.zeros([2, 2])
truth[0] = ([0, np.pi])
truth[1] = ([1001, np.pi])
plt.legend(loc='lower left')
plt.plot(truth[:,0], truth[:,1], 'r-', label='Pi Truth')
################################################################################

################################################################################
# Let sample count increase and estimate pi each time using LS

plt.figure(5)
plt.title("Monte Carlo / Latin Square Pi Estimates Overlay")
plt.ylim(0, 4)
plt.xlabel("Sample Count")
plt.ylabel("Esitmate")
plt.plot(mc_pi_estimates, label='MC Estimate of Pi')
plt.plot(ls_pi_estimates, 'k', label='LS Estimate of Pi')
truth = np.zeros([2, 2])
truth[0] = ([0, np.pi])
truth[1] = ([1001, np.pi])
plt.legend(loc='lower left')
plt.plot(truth[:,0], truth[:,1], 'r-', label='Pi Truth')
################################################################################

################################################################################
plt.figure(6)
plt.xlabel("Sample Count")
plt.ylabel("Variance")
plt.title("Variance as a Function of Sample Count - Monte Carlo")
plt.plot(mc_pi_est_var, label="Monte Carlo Variance")
# plt.plot(ls_pi_est_var, 'k', label="Latin Square Variance")
plt.legend(loc='upper right')
################################################################################

################################################################################
plt.figure(7)
plt.xlabel("Sample Count")
plt.ylabel("Variance")
plt.title("Variance as a Function of Sample Count - LatinSquare")
plt.plot(ls_pi_est_var, 'k', label="Latin Square Variance")
plt.legend(loc='upper right')
################################################################################

################################################################################
plt.figure(8)
plt.xlabel("Sample Count")
plt.ylabel("Variance")
plt.title("Variance as a Function of Sample Count - Monte Carlo")
plt.plot(mc_pi_est_var, label="Monte Carlo Variance")
plt.plot(ls_pi_est_var, 'k', label="Latin Square Variance")
plt.legend(loc='upper right')
################################################################################
plt.show()
