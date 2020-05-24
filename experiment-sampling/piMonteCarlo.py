#!/Users/josephkloiber/anaconda3/bin/python3

# levels in this script refer to the number of steps in a factor 
# specific to the terminology we use in Formal Design of Experiments

import numpy as np
import matplotlib.pyplot as plt

################################################################################
# set the geometrical bounds for the example
samples = 1001
radius = 1

save_image = 0

mc_points = []
mc_pi_est_var = []

ls_points = []
ls_pi_est_var = []

circled_x = []
circled_y = []

square_points = []
circle_points = []
################################################################################

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

def get_encircled_points(points, radius):
    del circled_x[:]
    del circled_y[:]
    for i in range(np.size(points[:,0])):
        magnitude=np.sqrt(np.power(points[i,0], 2)+np.power(points[i,1], 2))
        if(magnitude <= radius):
            circled_x.append( points[i,0] )
            circled_y.append( points[i,1] )
    return

def count_encircled_points(points):
    magnitude=np.power(np.power(points[:,0], 2) + np.power(points[:,1], 2), 0.5)
    return np.size(np.where(magnitude <= 1))

def plot_configuration(index, radius, title):
    plt.figure(index)
    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)
    plt.title(title)
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.axis('equal')

################################################################################
# 1. Display data 

# 1a. The Square, Circle and Radius
square_points = populate_square(radius)
circle_points = popluate_circle(radius)
radius_plot = np.zeros([2, 2])
radius_plot[0] = ([0, 0])
radius_plot[1] = ([radius, 0])

## 1b. Pi Truth Value for plotting
truth = np.zeros([2, 2])
truth[0] = ([0, np.pi])
truth[1] = ([samples, np.pi])

# 2. Build Monte Carlo Samples
mc_points = monte_carlo_points_2d(samples, radius)

# 3. Build Latin Square Samples
ls_points = latin_square_points_2d(samples, radius)

# 4. Calculate the Monte Carlo Variances
mc_pi_estimates = []
for count in range(1,samples):
    mc_pi_estimates.append(4* count_encircled_points(mc_points[:count]) / count)
    mc_pi_est_var.append(np.var(mc_pi_estimates))

# 5. Calculate the Latin Square Variances
ls_pi_estimates = []
for count in range(1,samples):
    ls_pi_estimates.append(4* count_encircled_points(ls_points[:count]) / count)
    ls_pi_est_var.append(np.var(ls_pi_estimates))

################################################################################


    
################################################################################
# Build and show the Monte Carlo points

plot_configuration(1, radius, "1000 Random Samples Monte Carlo Sampling")

plt.plot(mc_points[:,0], mc_points[:,1], 'bo', label='Monte Carlo')
plt.plot(square_points[:,0], square_points[:,1], 'r-', linewidth=5)
plt.plot(circle_points[:,0], circle_points[:,1], 'g-', linewidth=5)
if(save_image != 0):
    plt.savefig('./images/monte_carlo_points.png')

get_encircled_points(mc_points, radius)
plt.plot(circled_x, circled_y, 'ko' )
plt.plot(square_points[:,0], square_points[:,1], 'r-', linewidth=5)
plt.plot(circle_points[:,0], circle_points[:,1], 'g-', linewidth=5)
################################################################################

################################################################################
# Build and show the latin square points

plot_configuration(2, radius, "1000 Random Samples Latin Square Sampling")


plt.plot(ls_points[:,0], ls_points[:,1], 'bo', label='Monte Carlo')
get_encircled_points(ls_points, radius)
plt.plot(circled_x, circled_y, 'ko' )
plt.plot(square_points[:,0], square_points[:,1], 'r-', linewidth=5)
plt.plot(circle_points[:,0], circle_points[:,1], 'g-', linewidth=5)
if(save_image != 0):
    plt.savefig('./images/latin_sqaure_points.png')
################################################################################

################################################################################
# Let sample count increase and estimate pi each time using MC

plt.figure(3)
plt.title("Monte Carlo Pi Estimates Over Increasing Sample Count")
plt.ylim(0, 4)
plt.xlabel("Sample Count")
plt.ylabel("Esitmate")
plt.plot(mc_pi_estimates, label='Estimate of Pi')
plt.legend(loc='lower left')
plt.plot(truth[:,0], truth[:,1], 'r-', label='Pi Truth')
if(save_image != 0):
    plt.savefig('./images/monte_carlo_estimate.png')
################################################################################

################################################################################
# Let sample count increase and estimate pi each time using LS

plt.figure(4)
plt.title("Latin Square Pi Estimates Over Increasing Sample Count")
plt.ylim(0, 4)
plt.xlabel("Sample Count")
plt.ylabel("Esitmate")
plt.plot(ls_pi_estimates, 'k', label='Estimate of Pi')
plt.legend(loc='lower left')
plt.plot(truth[:,0], truth[:,1], 'r-', label='Pi Truth')
if(save_image != 0):
    plt.savefig('./images/latin_square_estimate.png')
################################################################################

################################################################################
# Compare the variances of the two methods

plt.figure(5)
plt.title("Monte Carlo / Latin Square Pi Estimates Overlay")
plt.ylim(0, 4)
plt.xlabel("Sample Count")
plt.ylabel("Esitmate")
plt.plot(mc_pi_estimates, label='MC Estimate of Pi')
plt.plot(ls_pi_estimates, 'k', label='LS Estimate of Pi')
plt.legend(loc='lower left')
plt.plot(truth[:,0], truth[:,1], 'r-', label='Pi Truth')
if(save_image != 0):
    plt.savefig('./images/mc_ls_estimate.png')
################################################################################

################################################################################
plt.figure(6)
plt.xlabel("Sample Count")
plt.ylabel("Variance")
plt.title("Variance as a Function of Sample Count - Monte Carlo")
plt.plot(mc_pi_est_var, label="Monte Carlo Variance")
plt.legend(loc='upper right')
if(save_image != 0):
    plt.savefig('./images/mc_variance.png')
################################################################################

################################################################################
plt.figure(7)
plt.xlabel("Sample Count")
plt.ylabel("Variance")
plt.title("Variance as a Function of Sample Count - LatinSquare")
plt.plot(ls_pi_est_var, 'k', label="Latin Square Variance")
plt.legend(loc='upper right')
if(save_image != 0):
    plt.savefig('./images/ls_variance.png')
################################################################################

################################################################################
plt.figure(8)
plt.xlabel("Sample Count")
plt.ylabel("Variance")
plt.title("Variance as a Function of Sample Count - Monte Carlo")
plt.plot(mc_pi_est_var, label="Monte Carlo Variance")
plt.plot(ls_pi_est_var, 'k', label="Latin Square Variance")
plt.legend(loc='upper right')
if(save_image != 0):
    plt.savefig('./images/mc_ls_variance.png')
################################################################################
plt.show()
