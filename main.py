from curses import wrapper
import curses
import time

page = ["Notion", "Calendar", "Task"]

def input(keys: list, stdscr): 

def task(stdscr):
    stdscr.clear()

    stdscr.addstr(0, 0, "Add")
    stdscr.refresh()

    while True:

        time.sleep(4)
        break

def menu(stdscr):
    stdscr.clear()

    posy = 2 

    list_pos = []

    for i in page:
        stdscr.addstr(posy, 5, i)
        posy += 2
        list_pos.append(posy)
    stdscr.refresh()

    return list_pos

def main(stdscr):
    # Clear screen
    stdscr.clear()

    curses.cbreak()

    y = 0

    k = ""

    while True:
        # Draw 
        list_pos = menu(stdscr)

        # Update position cursor
        stdscr.move(y, 4)

        # Read the keys 
        k = stdscr.getch()

        if k == 113:
            break

        if k == 121:
            for i in range(0, len(list_pos)):
                if y+2 == list_pos[i]:
                    if page[i] == page[2]:
                        task(stdscr)

        if k == 258:
            y += 1
        if k == 259:
            y -= 1

wrapper(main)
