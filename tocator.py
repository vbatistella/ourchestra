from FoxDot import *
import time

Clock.set_time(7)
Scale.default = "chromatic"
Root.default = 0

DEBUG = False

"""
The idea is to have a FoxDot player for each track and play them all simultaneously. 

m1 - the melody track, is on default on pluck
c1 - the chord track, is on default on <something>
x1 - the drum track, I really don't think it cares about the instrument, it just uses play
"""

def single_note(notes = [], durations = []):
    if DEBUG:
        print("i am going to play the following notes")
        print(notes)
        print(durations)

    m1 >> pluck(notes, dur =durations)

def chord(chords = [], durations = []):
    if DEBUG:
        print("i am going to play the follwoing chords:")
        print(chords)
        print(duration)

    c1 >> pluck(chords, dur=durations)

def beats(groove = "- - "):
    if DEBUG:
        print("i am going to play the following groove:")
        print(groove)

    x1 >> play(groove)

def main():
    DEBUG = True
    beats()
    time.sleep(4)
    beats("x-o-")
    Go()
    time.sleep(2) #this doesnt work lol
    beats("xxxx")

if __name__ == "__main__":
    main()