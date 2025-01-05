from terminal import main
import curses

if __name__ == "__main__":
    try :
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass