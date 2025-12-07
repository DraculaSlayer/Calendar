from curses import wrapper
import curses
import os
import subprocess
#import time

PATH_MAIN = "."

#page = ["Notion", "Calendar", "Task"]

class Calendar:

    #// Loop Main // (Fuck you niggar)
    def __init__(self):
        self.key = ""

        self.files = self.task_ToDo()
        self.position = []
        self.running = True
        self.y = 0
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
    
    def new(self, stdscr):
        while self.running:
#            stdscr.clear()
            stdscr.refresh()
            
            self.position = self.draw()
            
            stdscr.move(self.y, 4)

            self.handler_key()

    #// Draw //
    def draw(self):

        list_position = []

        y_str = -1

        for i in range(0, len(self.files)):

            y_str += 2

            list_position.append(y_str)

            self.stdscr.addstr(list_position[i], 5, self.files[i])

        return list_position

    
    #// Logic //
    def enter(self):
        for i in range(len(self.position)):
            if self.y == self.position[i]:

                print(i)
                #subprocess.Popen(["/usr/bin/bash", "vim", self.files[i]])

    def add(self):
        print("MI MAMI")


    #// Manager Keys // 
    def handler_key(self):

        self.key = self.stdscr.getch()

#        print(self.key)

        # Q
        if self.key == 113:
            self.running = False

        # Key Arrows (move curso)
        if self.key == 258:
            if self.y >= curses.LINES - 1:
               pass
            else:
                self.y += 1

        if self.key == 259:
            if self.y <= 0:
                pass
            else:
                self.y -= 1
        
        # Enter
        if self.key == 10:
            self.enter()

        # Add
        if self.key == 141:
            self.add()

    #// Logic from the files //
    def task_ToDo(self):
        directory = os.listdir(PATH_MAIN)

        if "todo.txt" in directory:
            with open(f"{PATH_MAIN}/todo.txt", "r") as f:
                for i in f.readlines():
                    match i[0:3]:
                        case "(A)":
                            print("holis"),
                        case "(B)":
                            print("siloh"),
                        case _:
                            pass

        return directory

if __name__ == "__main__":
    gg = Calendar()
    wrapper(gg.new)

