When not plugging in anything, my internal input and outputs work perfectly. When I plug in my headphones, which do not have microphone but only speakers, my input devices look like this (using pavucontrol i.e., pulseaudio volume control):

Internal Microphone (unplugged)
Microphone (plugged in)

#Solution
--->sudo apt install alsa-tools-gui

--->hdajackretask

Select the appropriate sound card up top in Select a codec:

Then make the Black Mic (headphone jack) override Not connected

Lower right corner, select Install boot override
![Screenshot from 2024-12-29 16-55-36](https://github.com/user-attachments/assets/a19658ac-9d57-458b-ab60-f9184aeb7ffa)





