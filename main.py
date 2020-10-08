MAX_TEMPO  = 8
MAX_BASE   = 16
MAX_SAMPLE = 2

melody = [0]*MAX_TEMPO
base   = [[0]*MAX_BASE  ]*MAX_BASE
beats  = [0]*MAX_TEMPO
sample = [[0]*MAX_SAMPLE]*MAX_SAMPLE

queue = []
note_at = 0

def add_queue(item):
    queue.append(item)

def pop_queue():
    return queue.pop(0)

def clear_queue():
    queue = []

def main():
    add_queue("aa")

def add_note(channel, note, tempo):
    if channel == 1:
        melody[channel] = 

if __name__ == "__main__":
    main()