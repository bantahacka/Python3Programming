# Name: projectile_height.py
# Author: Joe Bloggs, v1.0, contact_email
# Description: Calculate height of a projectile
"""
    Docstring contents here
"""

from math import pi, cos, tan

# Formula: y = y0 + x tan theta - gx^2/2(v0 cos theta)^2
# Where: y = Projectile height, y0 = Barrel height, x = Horizontal distance travelled
# theta = Elevation angle in radians (deg * (pi/180))
# g = Acceleration due to gravity (9.81m2)
# v0 = Initial velocity m/s

barrel_height = 1.0
horizontal_distance = 0.5
theta = 80 * (pi/180)
acceleration = 9.81
initial_velocity = 44

projectile_height = barrel_height + horizontal_distance * tan(theta) - ((acceleration * horizontal_distance**2) / (2*(initial_velocity * cos(theta))**2))
print("Height of projectile: %.2fm" % projectile_height)


