#cinnamon

# below is the command wto get Picture aspect that can be changed in background settings
# gsettings get org.cinnamon.desktop.background picture-options
# outputs are
'''
none	 	- for no picture
wallpaper	- for Mosaic
centered	- for Centered Mode
scaled 		- for Scaled mode
stretched 	- for streched mode
zoom 		- for zoomed mode
spanned 	- for for spanned mode
'''

# to set slideshow
# gsettings set org.cinnamon.desktop.background.slideshow slideshow-enabled false
'''
inputs allowed : true , false
'''
'''
gsettings set org.cinnamon.desktop.background.slideshow  image-source 'directory:///home/wallpaper'   

'''
