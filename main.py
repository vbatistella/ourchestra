from FoxDot import *
import os
import math

# I'm putting this here because I think it can hypothetically make a difference in a bizarre corner case
Clock.set_time(7)
Scale.default = "chromatic" #we want
Root.default = 0

DEBUG = True
running = True

# Kickers
# Kickers decide whether or not the queues can be dequeued and actually sent to our "tocator"

def melody_kicker(queue):
    pass

def chord_kicker(queue):
    pass

def drum_kicker(queue):
    pass

def main():
    global running
    print("é hora, meus bacanos")

    melody_queue = []
    chord_queue = []
    drum_queue = []
    tempo = var([1,2,3,4],4)
    
    # This starts FoxDot, the question is "when"
    Go()
    at = 0

    # This is where we will be constantly checking for messages and actually do stuff
    while(running):
        _, beat = (int(Clock.now()), tempo)
        print(beat)
        if not beat == at:
            print("bla")
            at = beat

    print("'tis the end, fellas")


if __name__ == "__main__":
    main()