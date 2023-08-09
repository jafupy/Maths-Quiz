import os

def awaitKeypress(prompt=None):
    if prompt != None:
        print(prompt)
    if os.name == 'nt':
        import msvcrt
        msvcrt.getch()
    else:
        import termios, tty, sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)