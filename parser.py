import requests
from definitions import *

# Twitch chat reader
def read_chat():
    r = requests.get('http://localhost:3000/')
    return r.json()

# Command validation
def validate(command):
    command = command[1:]
    if command in COMMANDS:
        return COMMANDS[command]
    else:
        print("Command not valid.")
        return None

def validate_tempo(tempo):
    try:
        tempo = float(tempo)
    except ValueError:
        print("Tempo not valid.")        
        return None
    if tempo > 4:
        print("Tempo greater than four.")
        return None
    return tempo

def check_balance(myStr): 
    open_list = ["[", "<"] 
    close_list = ["]", ">"] 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
    else: 
        return False

# Check if melody note is valid
def is_valid_m(note):
    in_notes  = note[:-1] in NOTES
    octave    = note[-1]
    if octave.isnumeric():
        octave    = int(note[-1])
        in_octave = octave >= OCTAVE_MIN and octave <= OCTAVE_MAX
    else:
        in_octave = False
    valid = in_notes and in_octave
    return valid

def is_valid_d(note):
    if not check_balance(note):
        print("Unbalanced drums parentheses.")
        return False
    for i in range(len(note)):
        if not note[i] in DRUMS:
            print("Non-existent drum character.")
            return False
    return True

def validate_drum_tempo(tempo):
    return tempo in [1,2,3,4]

def get_note(note):
    note_ref  = NOTES[note[:-1]]
    octave    = int(note[-1])
    note_ref = note_ref + (octave-4)*11
    return note_ref

def melody_maker(command, note, tempo):
    if not is_valid_m(note):
        print('Melody note not valid.')
        return None
    note_ref = get_note(note)
    return (note_ref, tempo)

def chord_maker(command, note, tempo):
    minor = False
    if note[-1] == 'm':
        minor = True
        note = note[:-1]
    if not is_valid_m(note):
        print("Chord main note not valid.")
        return None
    note_ref = get_note(note)
    third = note_ref+4
    if minor:
        third -= 1
    fifth = note_ref+7
    return ((note_ref, third, fifth), tempo)    

def drum_maker(command, note, tempo):
    if not validate_drum_tempo(tempo):
        print("Drum tempo not valid.")
        return None
    if not is_valid_d(note):
        print('Drum note not valid.')
        return None
    note = note.replace("."," ")
    return (note, tempo)

def send_foxdot(fox_note):
    print(fox_note)

# Main parser
def parse(command):
    command  = command.lower()
    split    = command.split(" ")

    if len(split) != 3:
        return None

    command  = split[0]
    note     = split[1]
    tempo    = split[2]
    
    # Validate and substitute command
    command = validate(command)
    tempo = validate_tempo(tempo)
    if command is None or tempo is None:
        return None

    if   command == "m":
        fox_note = melody_maker(command, note, tempo)
    elif command == "c":
        fox_note = chord_maker(command, note, tempo)
    elif command == "x":
        fox_note = drum_maker(command, note, tempo)
    else:
        return None
    if fox_note is None:
        return None
    
    return (command, fox_note)

def main():
    chat = ["!x x.[x-]<x!> 4"] #read_chat()
    for command in chat:
        # try:
        fox_note = parse(command)
        if not fox_note is None:
            send_foxdot(fox_note)
        else:
            pass # Send Invalid Note message

if __name__ == "__main__":
    main()