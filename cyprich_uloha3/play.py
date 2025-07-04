from machine import Pin, PWM
from utime import sleep

from cyprich_uloha3.melodies import *  # import melodies.py
from cyprich_uloha3.notes import *  # import notes.py

buzzer = PWM(Pin(5), freq=30000)  # pin where buzzer is connected

volume = 0  # set volume to a value between 0 and 1000


# functions to play the melodies

def playtone(frequency):
    buzzer.duty_u16(volume)  # maximal volume at duty cycle equal to 32768
    buzzer.freq(frequency)


def be_quiet():
    buzzer.duty_u16(0)  # turns sound off


def duration(tempo, t):
    # calculate the duration of a whole note in milliseconds (60s/tempo)*4
    # beats
    wholenote = (60000 / tempo) * 4

    # calculate the duration of the current note
    # (we need an integer without decimals, hence the // instead of /)
    if t > 0:
        noteDuration = wholenote // t
    elif (t < 0):
        # dotted notes are represented with negative durations
        noteDuration = wholenote // abs(t)
        noteDuration *= 1.5  # increase their duration by a half

    return noteDuration


def playsong(mysong):
    try:

        print(mysong[0])  # print title of the song to the shell
        tempo = mysong[1]  # get the tempo for this song from the melodies list

        # iterate over the notes of the melody.
        # The array is twice the number of notes (notes + durations)
        for thisNote in range(2, len(mysong), 2):

            noteduration = duration(tempo, int(mysong[thisNote + 1]))

            if (mysong[thisNote] == "REST"):
                be_quiet()
            else:
                playtone(notes[mysong[thisNote]])

            # we only play the note for 90% of the duration...
            sleep(noteduration * 0.9 / 1000)
            be_quiet()
            # ... and leave 10% as a pause between notes
            sleep(noteduration * 0.1 / 1000)

    except BaseException:  # make sure the buzzer stops making noise when something goes wrong or when the script is stopped
        be_quiet()


def set_volume(new_volume):
    """Set the volume of the music."""
    global volume
    volume = new_volume
