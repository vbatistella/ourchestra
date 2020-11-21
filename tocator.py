from FoxDot import *
import time

Clock.set_time(7)
Scale.default = "chromatic"
Root.default = 0

DEBUG = False

"""
THE TOCATOR
The idea is to have a FoxDot player for each track and play them all simultaneously. 
We named it like so due to the fact that it shouldn't be confused with FoxDot's players.

m1 - the melody track, is on default on pluck
c1 - the chord track, is on default on <something>
x1 - the drum track, I really don't think it cares about the instrument, it just uses play
"""

def single_note(notes = [], durations=[]):
    if DEBUG:
        print("i am going to play the following notes")
        print(notes)
        print(durations)

    m1 >> viola(notes, dur=durations)

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

    x1 >> play(groove, dur=1)

def main():
    DEBUG = True
    beats()
    time.sleep(3)
    beats("1234")
    time.sleep(3)
    beats("--xo")
    time.sleep(3)
    print("end")

if __name__ == "__main__":
    main()