from FoxDot import *
import subprocess
import math
import parser
import tocator

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
    n = []
    l = []
    kick = False
    total = 0
    out = 0
    print("a queueue eh")
    print(queue)
    for note in queue:
        if note:
            if total+note[1] <= 4:
                n.append(note[0])
                l.append(note[1])
                total += note[1]
                out+=1
                print('vou adicionar pra kickar %s e %d' % (note[0], note[1]))
            if total+note[1] >= 4:
                print('kickin time bois')
                kick = True
                break

    print("passei do for e vou printar a queueue de novo")
    print(queue)

    if kick:
        for i in range(out):
            if queue:
                queue.pop(0)

    print("passei do kick e a queueueue eh")
    print(queue)

    if n and l and kick:
        return (n, l)
    else:
        print('nao quero tocar ainda meu jovem')
        return None

def chord_kicker(queue):
    """returns a pair of lists (in a tuple) to play with strum()"""
    c = []
    l = []
    kick = False
    total = 0
    out = 0
    for chord in queue:
        if chord:
            if total+chord[1] <= 4:
                c.append(chord[0])
                l.append(chord[1])
                total += chord[1]
                out+=1
            elif total+chord[1] >= 4:
                print('chord kickin my dudes')
                kick = True
                break

    if kick:
        for i in range(out):
            queue.pop(0)

    if c and l and kick:
        return (c, l)
    else:
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

        #here we fetch the input and, if there is any, parse it
        chat = parser.read_chat()
        if chat:
            for message in chat:
                entry = parser.parse(message)
                if entry[1]:
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
                print('beat 4')
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

    print("'tis the end, fellas")


if __name__ == "__main__":
    main()