

************ qtile installation on Arch Linux *************
-------------------------------------------------------------
Below is a screen shot of my qtile. The Python code for customization is given in the config file:

![Screenshot from 2025-01-06 01-04-22](https://github.com/user-attachments/assets/f35ac613-a606-4ca1-8c68-cd98bad02ba3)


Note: I had a pre-existing hyperland which was using sddm. I had to kill wayland, disable sddm using  and enable lightdm 
in order for qtile to run. This was offcourse after qtile installation

- ps aux | grep wayland
- killall -9 wayland-session hyperland
- killall -9 wayland
- ps aux | grep wayland
- killall -9 wayland-session hyperland
- killall -9 wayland-session hyperland
- killall -9 wayland-session hyperland
- killall -9 wayland-session hyperland
- killall -9 wayland-session hyperland
- killall -9 wayland-session hyperland
- killall -9 wayland-session hyperland
- Xorg :0 &
- ps aux | grep x
- killall -9 Xorg
- sudo killall -9 Xorg
- Xorg :0 &
- export Display=:0
- qtile start
- qtile start
- qtile start
- shutdown now




Installation:
-------------
sudo pacman -S qtile
sudo pacman -S python-pip xorg-server xorg-xrandr xorg-xsetroot alacritty dmenu
sudo pacman -S lxappearance
sudo pacman -S nitrogen thunar
sudo pacman -S xfce4-terminal picom archlinux-wallpaper lightdm lightdm-gtk-greeter
sudo systemctl enable lightdm.service
systemctl status display-manager.service

---------------------------------
sudo systemctl stop sddm.service    #This wont be needed if I do not already have hyperland
---------------------------------


-------------------------------
#do this only if qtile is run in a VM

cp /etc/xdg/picom.conf .config/
vim .config picom.conf
vim .config/picom.conf

and then  chnage
 
vsync = true

to 

vsnc = false
----------------------------------




# Configuration file
--------------------
#it probably wont be needed
#mkdir -p ~/.config/qtile
#cp /usr/share/qtile/default_config.py ~/.config/qtile/config.py


cd ~/.config/qtile
vim config.py


=====================================================================

#Adusting scaling settings for virtual vox

sudo pacman -Syu
sudo pacman -S virtualbox-guest-utils linux-headers
sudo systemctl enable vboxservice
sudo systemctl start vboxservice
sudo modprobe vboxguest
sudo modprobe vboxsf
sudo modprobe vboxvideo
sudo reboot


========================================================================



# Looking for potential errors in the config.py

cat ~/.local/share/qtile/qtile.log


# config file

cd .config/qtile/
vim config.py


#Restart qtile to see the changes
qtile cmd-obj -o cmd -f restart

=======================================================================
# To set start up programs
add an autostart.sh to ~/.config/qtilite

#add commands for start up programs i.e., nitrogen and picom 

#make it executable by

chmod +x autostard.sh


#And add hook to the configuration by using Python decorators


========================================================================



