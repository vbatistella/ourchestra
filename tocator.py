from FoxDot import *

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
        print(notes)
        print(durations)
    m1 >> pluck(notes, dur = [durations])

def chord(chord_roots = [], durations = []):
    if DEBUG:
        print(chord_root)
        print(notes)
        print(duration)
    
    #handy-dandy chord-making function that does stuff in parser haha

    c1 >> pluck(chords, dur=durations)