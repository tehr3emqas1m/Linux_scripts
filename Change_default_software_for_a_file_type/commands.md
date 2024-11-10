********************************************** xdg-mime *********************************************

First set the path to a file of a prticular file type. e.g, an mp3 file

xdg-mime query filetype /media/tehreem/52F2921FF29206FF/music/abc.mp3


This returns audio/mpeg, so do the following:



xdg-mime default vlc.desktop audio/mpeg
