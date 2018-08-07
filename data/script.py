import math
import cmath
import random
import numpy as np
# SciPy is for spherical harmonics
import scipy
# Library for Density Plots
import seaborn as sns

# Plotting library 
from matplotlib import pyplot as plt 

xw = 0.028      # Bottoms mol fraction
zf = 0.36       # Feed mol fraction
xd = 0.823      # Distillate mol fraction
q = 1.13        # Calculated q or liquid portion of feed
reflux = 2.96   # Reflux ratio

# VLE Data
vle = np.loadtxt('vle.dat')
x_eq = vle[:,0]
y_eq = vle[:,1]

# Intersection point of operating lines
yi=(zf+xd*q/reflux)/(1+q/reflux)
xi=(-(q-1)*(1-reflux/(reflux+1))*xd-zf)/((q-1)*reflux/(reflux+1)-q)

# Rectifying line 
# Start point: (xi, yi)
# End point: (xd, xd)
m_rec = reflux/(reflux+1) 			# Slope
c_rec = xd/(reflux+1) 				# Intercept 

# Get stripping line
# Starting point: (xw, xw) 
# End point : (xi, yi)
m_strip = (xw - yi)/(xw- xi) 		# Slope
c_strip = xw*(yi - xi)/(xw - xi) 	# Intercept

# Get rectifying line points
# Use eqn : y_rec = m_rec*x_rec + c_rec
x_rec = np.linspace(xi, xd, num=20) 
y_rec = m_rec*x_rec + c_rec
rec_data = np.column_stack((x_rec,y_rec))
np.savetxt('rectifying.dat',rec_data,header='x_rec y_rec')

# Get stripping line points
# Use eqn : y_strip = m_strip * x_strip + c_strip
x_strip = np.linspace(xw, xi, num=20) 
y_strip = m_strip*x_strip + c_strip
strip_data = np.column_stack((x_strip,y_strip))
np.savetxt('strppr.dat',strip_data,header='x_strip y_strip')

# Get the feed line points
# Points : (xi, yi) and (zf, zf)
if q != 0:
	m_feed = q/(q-1) 			# Slope of the feed line
	c_feed = -zf/(q-1) 			# Intercept

if zf<xi:
	x_feed = np.linspace(zf, xi, num=20)
	y_feed = m_feed*x_feed + c_feed
elif zf>xi:
	x_feed = np.linspace(xi, zf, num=20)
	y_feed = m_feed*x_feed + c_feed 
else: 							# For q=0
	x_feed = [zf, xi]
	y_feed = [zf, yi]

feed_data = np.column_stack((x_feed,y_feed))
np.savetxt('feed.dat',feed_data,header='x_feed y_feed')