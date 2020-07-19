import matplotlib.pyplot as plt
import pyfits as pf

#change for different stars
camera = "SAE"
title_star = "Canopus"
star = 2111805 #ASCC number

#import calibrated light curve taken by the South African eastern camera
filename = '/data2/sanna/FitsSAE/'+str(star)+'SAE_detrended.fits'
data = pf.getdata(filename)

#plot the light curve
plt.plot(data['jd'], data['mag0'], '.', alpha = 0.1)
plt.ylabel("Magnitude")
plt.xlabel("Time (Julian Date)")
plt.title(str(title_star) + " (camera " + str(camera) +")")
plt.gca().invert_yaxis()
plt.show()
