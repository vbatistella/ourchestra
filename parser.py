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
        return "notfound"

def validate_tempo(tempo):
    if not tempo.isnumeric():
        raise Exception("Invalid tempo name.")
    return int(tempo)


# Check if melody note is valid
def is_valid_m(note):
    in_notes  = note[:-1] in NOTES
    octave    = note[-1]
    if octave.isnumeric():
        octave    = int(note[-1])
        in_octave = octave >= OCTAVE_MIN and octave <= OCTAVE_MAX
    else:
        in_octave = False
    valid     = in_notes and in_octave
    if not valid:
        Exception("Invalid melody note.")
    return valid

def melody_maker(command, note, tempo):
    if not is_valid_m(note):
        return
    note_ref  = NOTES[note[:-1]]
    octave    = int(note[-1])
    note_ref = note_ref + (octave-4)*11
    return (note_ref, tempo)

def chord_maker(command, note, tempo):
    return

def drum_maker(command, note, tempo):
    return

def send_foxdot(fox_note):
    print(fox_note)

# Main parser
def parse(command):
    command  = command.lower()
    split    = command.split(" ")
    command  = split[0]
    note     = split[1]
    tempo    = split[2]
    
    # Validate and substitute command
    command = validate(command)
    tempo = validate_tempo(tempo)
    
    if   command == "m":
        fox_note = melody_maker(command, note, tempo)
    elif command == "c":
        fox_note = chord_maker(command, note, tempo)
    elif command == "x":
        fox_note = drum_maker(command, note, tempo)
    else:
        raise Exception("Invalid command name.")
    
    return fox_note

def main():
    chat = ["!m G4 1"] #read_chat()
    for command in chat:
        # try:
        fox_note = parse(command)
        # except:
        #     print("Invalid")
        # else:
        send_foxdot(fox_note)

if __name__ == "__main__":
    main()