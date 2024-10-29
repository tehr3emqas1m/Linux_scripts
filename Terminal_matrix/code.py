import curses
import random
import time

def matrix_effect(stdscr):
    curses.curs_set(0)  
    stdscr.nodelay(True)
    stdscr.timeout(50)

    #screen dimensions
    sh, sw = stdscr.getmaxyx()
    columns = [0] * sw
    fall_speed = [random.randint(1, 3) for _ in range(sw)] 

    while True:
        stdscr.clear()
        
        # Updating screen dimensions in case of resize
        sh, sw = stdscr.getmaxyx()
        
        # Column tracking and speed lists adjustment with screen width 
        if len(columns) != sw:
            columns = [0] * sw
            fall_speed = [random.randint(1, 3) for _ in range(sw)]

        # Matrix characters
        for i in range(sw):
            if columns[i] == 0:
                # Character density
                if random.random() > 0.001:  # High probability for denser effect
                    columns[i] = random.randint(1, sh // 2)
            if columns[i] > 0:
                if columns[i] < sh - 1:
                    char = chr(random.randint(33, 126))  # ASCII characters from ! to ~
                    stdscr.addstr(columns[i], i, char, curses.color_pair(1))
                
                if random.randint(1, 3) <= fall_speed[i]:
                    columns[i] += 1 

                if columns[i] >= sh:
                    columns[i] = 0  

        stdscr.refresh()
        time.sleep(0.05) 

if __name__ == "__main__":
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    try:
        curses.wrapper(matrix_effect)
    except KeyboardInterrupt:
        pass  #exit with Ctrl+C
