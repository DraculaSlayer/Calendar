from curses import wrapper
import curses
import os
import subprocess
#import time

PATH_MAIN = "."

class Calendar:

    #// Loop Main // (Fuck me niggar)
    def __init__(self):
        self.key = ""

        self.buffer = self.task_ToDo()
        self.position = []
        self.running = True
        self.y = 0
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
    
    def new(self, stdscr):
        while self.running:
            stdscr.clear()
            stdscr.refresh()
            
            self.position = self.draw()
            
            stdscr.move(self.y, 4)

            self.handler_key()

    #// Draw //
    def draw(self):

        list_position = []

        y_str = 0

        self.stdscr.addstr(0, 5, "a: Add        d: Delete        x: Completed")

        for i in range(0, len(self.buffer)):

            y_str += 2

            list_position.append(y_str)

            self.stdscr.addstr(list_position[i], 5, self.buffer[i])

        return list_position
    
    #// Logic //
    def completed(self):
        for i in range(len(self.position)):
            if self.y == self.position[i]:
                complete = self.buffer[i]
                tach = complete[0:3]
                complete = complete.replace(tach, "x")
                self.buffer[i] = complete 

                self.change_file(f"{PATH_MAIN}/todo.txt")

                self.buffer = self.task_ToDo()

    def add(self):

        task = ""
        position_cursor = 0
        self.stdscr.move(curses.LINES-1, position_cursor)

        list_keys = ["KEY_BACKSPACE"]

        while True:       
            INPUT = self.stdscr.getkey()

            if INPUT == "\n":
                self.buffer.append(task+"\n")
                break
            if INPUT == "KEY_BACKSPACE":
                task = task[:-1]
                
                for i in range(curses.COLS-1):
                    self.stdscr.addch(curses.LINES-1, i, " ")
                    self.stdscr.refresh()
           
            if INPUT in list_keys:
                pass
            else:
                task = task + INPUT

            self.stdscr.move(curses.LINES-1, position_cursor)
            
            self.stdscr.addstr(curses.LINES-1, 0, task)
            self.stdscr.refresh()
    
    def delete(self):
        for i in range(len(self.position)):
            if self.y == self.position[i]:
                self.buffer.pop(i)
    
    #// Manager Keys // 
    def handler_key(self):

        self.key = self.stdscr.getch()

#        print(self.key)

        # Q
        if self.key == 113:
            self.running = False

        # Key Arrows (move curso)
        if self.key == 258 or self.key == 107:
            if self.y >= curses.LINES - 1:
               pass
            else:
                self.y += 1

        if self.key == 259 or self.key == 106:
            if self.y <= 0:
                pass
            else:
                self.y -= 1
        
        # Completed (x)
        if self.key == 120:
            self.completed()

        # Add (a)
        if self.key == 97:
            self.add()

        # Delete (d)
        if self.key == 100:
            self.delete()

    #// Logic from the files //
    def task_ToDo(self):
        directory = os.listdir(PATH_MAIN)

        if "todo.txt" in directory:
            with open(f"{PATH_MAIN}/todo.txt", "r") as f:
                return f.readlines()
    
    def change_file(self, file):
        with open(file, "w") as f:
            for i in self.buffer:
                f.writelines(i)

if __name__ == "__main__":
    gg = Calendar()
    wrapper(gg.new)
