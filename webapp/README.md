## Web App Interface for the DIY Spectrometer

Must be run locally on the computer connected to the spectrometer webcam. Assumes that the webcam window will have "Photospectrometer" in its title. (`wmctrl` can be used to set the title of a given window.)

Uses `wmctrl` to change focus to that window, then takes a screenshot with `gnome-screenshot`. Returns focus to the browser, then loads the screenshot.

To be extended to also display analysis of the spectrum. 
