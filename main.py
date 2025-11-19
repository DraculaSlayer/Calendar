import curses
from curses import wrapper
import time

def menu(stdscr):

    page = ["Notes", "calendar"]

    posy = 4

    for i in page:
        stdscr.clear()
        stdscr.addstr(posy, 2, i);
        posy += 2

    stdscr.refresh()


def main(stdscr):

    stdscr.clear()

    x = 5
    y = 0

    running = True

    while running:
        #   Draw
        # --------

        menu(stdscr)
        stdscr.addstr(y, x, "X")
        
        # --------

        #Logic Main
        k = stdscr.getch()

        if k == 113:
            stdscr.clear()
            running = False

        if k == 104:
            if y == curses.LINES - 1:
                pass
            else:
                y += 1
        if k == 106:
            if y == 0:
                pass
            else:
                y -= 1


if __name__ == "__main__":
    stdscr = curses.initscr()
    stdscr.keypad(True)
    curses.noecho()
    curses.curs_set(0)

    main(stdscr)
