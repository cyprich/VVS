

# import time
# from machine import PWM
# from enum import Enum
#
# from du1.utils import inputer, decider
#
#
# class F(Enum):
#     C4 = 262,
#     CS4 = 277,
#     D4 = 294,
#     DS4 = 311,
#     E4 = 330,
#     F4 = 349,
#     FS4 = 370,
#     G4 = 392,
#     GS4 = 415,
#     A4 = 440,
#     AS4 = 466,
#     B4 = 494,
#     C5 = 523,
#     CS5 = 554,
#     D5 = 587,
#     DS5 = 622,
#     E5 = 659,
#     F5 = 698,
#     FS5 = 740,
#     G5 = 784,
#     GS5 = 831,
#     A5 = 880,
#     AS5 = 932,
#     B5 = 988,
#     C6 = 1047,
#
#
# class Note:
#     def __init__(self, frequency: F, length: int):
#         self.frequency = frequency
#         self.length = length
#
#
# class Melody:
#     def __init__(self, name: str, *args: Note):
#         self.name = name
#         self.notes: list[Note] = args
#
#
# class Melodies:
#     def __init__(self):
#         self._freq: int = 440
#         self._max_volume: int = 32_768
#         self._volume: int = int((self._max_volume + 1) / 128)
#         self._buz: PWM = PWM(5, freq=self._freq, duty_u16=self._volume)
#
#         self._melodies: list[Melody] = []
#         notes = ['NOTE_F5', '2', 'NOTE_C6',
#                  '2', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F6', '2', 'NOTE_C6', '4', 'NOTE_AS5', '8',
#                  'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F6', '2', 'NOTE_C6', '4', 'NOTE_AS5', '8', 'NOTE_A5', '8',
#                  'NOTE_AS5', '8', 'NOTE_G5', '2', 'NOTE_C5', '8', 'NOTE_C5', '8', 'NOTE_C5', '8', 'NOTE_F5', '2',
#                  'NOTE_C6', '2', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F6', '2', 'NOTE_C6', '4',
#                  'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F6', '2', 'NOTE_C6', '4', 'NOTE_AS5', '8',
#                  'NOTE_A5', '8', 'NOTE_AS5', '8', 'NOTE_G5', '2', 'NOTE_C5', '-8', 'NOTE_C5', '16', 'NOTE_D5', '-4',
#                  'NOTE_D5', '8', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F5', '8', 'NOTE_F5', '8',
#                  'NOTE_G5', '8', 'NOTE_A5', '8', 'NOTE_G5', '4', 'NOTE_D5', '8', 'NOTE_E5', '4', 'NOTE_C5', '-8',
#                  'NOTE_C5', '16', 'NOTE_D5', '-4', 'NOTE_D5', '8', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8',
#                  'NOTE_F5', '8', 'NOTE_C6', '-8', 'NOTE_G5', '16', 'NOTE_G5', '2', 'REST', '8', 'NOTE_C5', '8',
#                  'NOTE_D5', '-4', 'NOTE_D5', '8', 'NOTE_AS5', '8', 'NOTE_A5', '8', 'NOTE_G5', '8', 'NOTE_F5', '8',
#                  'NOTE_F5', '8', 'NOTE_G5', '8', 'NOTE_A5', '8', 'NOTE_G5', '4', 'NOTE_D5', '8', 'NOTE_E5', '4',
#                  'NOTE_C6', '-8', 'NOTE_C6', '16', 'NOTE_F6', '4', 'NOTE_DS6', '8', 'NOTE_CS6', '4', 'NOTE_C6', '8',
#                  'NOTE_AS5', '4', 'NOTE_GS5', '8', 'NOTE_G5', '4', 'NOTE_F5', '8', 'NOTE_C6', '1']
#         self._melodies.append(Melody("Star Wars", Note(F.AS4, 8), Note(F.AS4, 8), Note(F.AS4, 8), Note(F.F5, 2), Note(F.C6, 2)))
#         self._melodies.append(Melody("Star Wars 2", Note(F.AS4, 8), Note(F.AS4, 8), Note(F.AS4, 8), Note(F.F5, 2), Note(F.C6, 2)))
#
#         self._index = decider("Which melody you want to play?", *[i.name for i in self._melodies])
#
#     def run(self):
#         self._buz.init()
#
#         for note in self._melodies[self._index].notes:
#             self._buz.freq(note.frequency)
#             time.sleep(note.length)
#
#         self.stop()
#
#     def stop(self):
#         self._buz.deinit()

from play import *

class Melodies:
    def __init__(self):
        pass

    def run(self):
        set_volume(256)
        playsong(melody[1])
