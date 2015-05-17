## Web App Interface for the DIY Spectrometer

Must be run locally on the computer connected to the spectrometer webcam. Assumes that the webcam window will have "Photospectrometer" in its title. (`wmctrl` can be used to set the title of a given window.)

Update: We are using GTK UVC Video Viewer, due to the ability to control the settings of the camera, but it won't allow the window title to be changed. So, instead, we are finding the webcam window by searching for ' fps)', as its title ends with a constantly updating display of the frames per second. (We are not using Guvcview as the settings window also has this name.)

Uses `wmctrl` to change focus to that window, then takes a screenshot with `gnome-screenshot`. Returns focus to the browser, then loads the screenshot.

To be extended to also display analysis of the spectrum. 
