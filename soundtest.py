from FoxDot import *

Clock.set_time(7)
Scale.default = "chromatic"
Root.default = 0

def major_scale(note):
    major = [note, note+2, note+4, note+5, note+7, note+9, note+11, note+12]
    print(major)
    p1 >> pluck(major)
    Go()


def main():
    major_scale(0)
    print("toquei a escala de Do maior")

if __name__ == "__main__":
    main()