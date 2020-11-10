from FoxDot import *
import subprocess
import math
import parser
import tocator

# I'm putting this here because I think it can hypothetically make a difference in a bizarre corner case
Clock.set_time(7)
Scale.default = "chromatic" #we want chromatic because it has all of our western notes
Root.default = 0 #C

Clock.bpm = 100

DEBUG = True
running = True

# Kickers
# Kickers decide whether or not the queues can be dequeued and actually sent to our "tocator"

def melody_kicker(queue):
    """returns a pair of lists to play with strum()"""
    return None

def chord_kicker(queue):
    """returns a pair of lists to play with strum()"""
    return None

def drum_kicker(queue):
    """returns a string to play with play()"""
    return None

def main():
    global running

    #user inputs via chat
    melody_queue = []
    chord_queue = []
    drum_queue = []

    tempo = var([1,2,3,4],1) #this works
    t = False

    
    pid = subprocess.Popen(['python3', 'maestro.py']) #starts FoxDot

    # This is where we will be constantly checking for messages and actually do stuff
    while(running):
        _, beat = (int(Clock.now()), tempo)
        #here goes the code that fetches input
        pass
        # 

        if beat == 3 and not t:
            t = True

        if beat == 4 and t: #every 4th beat we check if we can change our players
            if DEBUG:
                print('beat 4')
            melody = melody_kicker(melody_queue)
            chords = chord_kicker(chord_queue)
            drums = drum_kicker(drum_queue)
            if melody:
                tocator.single_note(melody)
            if chords:
                tocator.chord(chords)
            if drums:
                tocator.beats(drums)
            t = False

    print("'tis the end, fellas")


if __name__ == "__main__":
    main()