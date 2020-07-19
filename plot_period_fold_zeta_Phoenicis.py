import matplotlib.pyplot as plt
import pyfits as pf

#change for different stars
camera = "SAE"
title_star = "zeta Phoenicis"
star = 2198437 #ASCC number
period = 1.6697671

#import calibrated light curve taken by the South African eastern camera
filename = '/data2/sanna/FitsSAE/'+str(star)+'SAE_detrended_binned.fits'
data_binned = pf.getdata(filename)

#plot period fold
plt.plot(data_binned[1]%(period*2), data_binned[0], '.', alpha = 0.3)
plt.ylabel("Magnitude")
plt.xlabel("Time (days)")
plt.title(str(title_star) + " binned period fold (camera " + str(camera) +")")
plt.gca().invert_yaxis()
plt.show()