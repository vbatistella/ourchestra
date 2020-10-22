from FoxDot import *

# I'm putting this here because I think it can hypothetically make a difference in a bizarre corner case
Clock.set_time(7)
Scale.default = "chromatic"
Root.default = 0

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
    print("é hora, meus bacanos")

    melody_queue = []
    chord_queue = []
    drum_queue = []
    
    # This starts FoxDot, the question is "when"
    Go()

    # This is where we will be constantly checking for messages and actually do stuff
    while(running):
        pass

    print("'tis the end, fellas")


if __name__ == "__main__":
    main()