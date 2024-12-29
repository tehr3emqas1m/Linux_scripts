When not plugging in anything, my internal input and outputs work perfectly. When I plug in my headphones, which do not have microphone but only speakers, my input devices look like this (using pulseaudio volume control):

Internal Microphone (unplugged)
Microphone (plugged in)

sudo apt install alsa-tools-gui

hdajackretask
Select the appropriate sound card up top in Select a codec:

Then make the Black Mic (headphone jack) override Not connected

Lower right corner, select Install boot override

