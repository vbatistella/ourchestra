from FoxDot import *
import subprocess
import math
import parser
import tocator
import argparse

# I'm putting this here because I think it can hypothetically make a difference in a bizarre corner case
Clock.set_time(7)
Scale.default = "chromatic" #we want chromatic because it has all of our western notes
Root.default = 0 #C

Clock.bpm = 80

DEBUG = True
running = True

# Kickers
# Kickers decide whether or not the queues can be dequeued and actually sent to our "tocator"

def melody_kicker(queue):
    """returns a pair of lists (in a tuple) to play with strum()"""
    if DEBUG:
        print("Melody Kicker")
    n = []
    l = []
    kick = False
    total = 0
    out = []
    if DEBUG:
        print("Queue:")
        print(queue)
    for note in queue:
        if note:
            if total+note[1] <= 4:
                n.append(note[0])
                l.append(note[1])
                total += note[1]
                out.append(note)
                if DEBUG:
                    print('vou adicionar pra kickar %s, %d' % (note[0], note[1]))
            if total >= 4:
                if DEBUG:
                    print('Setando Kick = True')
                kick = True
                break

    if kick:
        for i in out:
            if queue:
                if DEBUG:
                    print("Removendo da queue %s" %(str(queue[0])))
                queue.remove(i)

    if n and l and kick:
        print("Tocando %s %s" % (str(n), str(l)))
        return (n, l)
    else:
        print('Nenhuma melodia nova para tocar')
        return None

def chord_kicker(queue):
    """returns a pair of lists (in a tuple) to play with strum()"""
    if DEBUG:
        print("Chord Kicker")
    c = []
    l = []
    kick = False
    total = 0
    out = []
    if DEBUG:
        print("Queue:")
        print(queue)
    for chord in queue:
        if chord:
            if total+chord[1] <= 4:
                c.append(chord[0])
                l.append(chord[1])
                total += chord[1]
                out.append(xhord)
                if DEBUG:
                    print('vou adicionar pra kickar %s, %d' % (chord[0], chord[1]))
            if total >= 4:
                if DEBUG:
                    print('Setando Kick = True')
                kick = True
                break

    if kick:
        for i in out:
            if queue:
                if DEBUG:
                    print("Removendo da queue %s" %(str(queue[0])))
                queue.remove(i)

    if c and l and kick:
        print("Tocando %s %s" % (str(c), str(l)))
        return (c, l)
    else:
        print('Nenhum acorde novo para tocar')
        return None

def drum_kicker(queue):
    """returns a string to play with play()"""
    if DEBUG:
        print("Drum Kicker")
    return None

def main():
    global running
    global DEBUG

    args = argparse.ArgumentParser(description='Play music, requires supercollider to be runnning FoxDot and chat.js to be running')
    args.add_argument("-d", action="store_true", help="runs in debug mode")
    arglist = vars(args.parse_args())

    DEBUG = arglist['d']

    if DEBUG:
        print('Running in debug mode')

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

        #here we fetch the input and, if there is any, parse it
        chat = parser.read_chat()
        if chat:
            for message in chat:
                entry = parser.parse(message)
                if entry:
                    if entry[0] == "m":
                        melody_queue.append(entry[1])
                    elif entry[0] == "c":
                        chord_queue.append(entry[1])
                    elif entry[0] == "x":
                        drum_queue.append(entry[1])

        if beat == 3 and not t:
            t = True

        if beat == 4 and t: #every 4th beat we check if we can change our players
            if DEBUG:
                print('==================NOVO COMPASSO==================')
            melody = melody_kicker(melody_queue)
            chords = chord_kicker(chord_queue)
            drums = drum_kicker(drum_queue)
            if melody:
                tocator.single_note(melody[0], melody[1])
            if chords:
                tocator.chord(chords[0], chords[1])
            if drums:
                tocator.beats(drums)
            t = False


if __name__ == "__main__":
    main()