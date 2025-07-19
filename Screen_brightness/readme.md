<b>Checking the display</b>
xrandr --verbose | grep " connected" | awk '{print $1}'

<b>(Usually eDP-1, LVDS-1, or similar)</b>

<b>Now:</b> 


```randr --output eDP-1 --brightness $(echo "$(xrandr --verbose | grep -i brightness | awk '{print $2}') - 0.1" | bc)```

