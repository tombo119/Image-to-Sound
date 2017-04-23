from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note, Rest
import math

def generateMusic(inputV, inputTempo):

    dimension = math.log(len(inputV), 2) #Equals N, where the length of inputV is 2^N
    duration = math.pow(len(inputV)/4, -1) #Scales the note duration accordingly.

    #--------Construction of Note Sequence----------------

    note_sequence = [Note(0,4), Rest(0.75), Note(0,4), Rest(0.75)] #Create two bars of rest at the start.

    for value in inputV:

        #Note Value:
        #0-C, 1-C#, 2-D, 3-D#, 4-E, 5-F, 6-F#
        #7-G, 8-G#, 9-A, 10-A#, 11-B

        #----DIATONIC------------

        #Over 4 Octaves, 28 notes
        #0-9 -> 3C
        #10-18 -> 3D
        #37-46
        #82-90 -> 4E

        #127-136 -> 5C , 137-146 -> 5D

        diatonicValue = [0, 2, 4, 5, 7, 9, 11]

        Dictionary = dict({(0,0,0): 0, (255,0,0): 1, (255,255,0): 2, (0,255,0): 3, (0,255,255): 4, (0,0,255): 5, (255,0,255): 6, (255,255,255): 7})
        note_value = diatonicValue[ Dictionary[tuple(value)] % 7]
        octave = 4 + (Dictionary[tuple(value)] // 7)
        print(octave)
        note = Note(note_value, octave, duration)
        note_sequence.append(note)

        #------------------------

        #Adds them to the note sequence

    melody = NoteSeq(note_sequence)


    #--------Backing Drumbeat Construction --------------------

    b = Note(11, 2, volume= 50)
    hh = Note(6, 3, volume= 50)

    drumBeat = NoteSeq([b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh, b, hh, hh, hh])

    #-------Creating MIDI file -------------

    m2 = Midi(number_tracks=2, tempo=inputTempo, channel=[0,9], instrument= [1,1])
    #See https://www.midi.org/specifications/item/gm-level-1-sound-set for instrument codes
    m2.seq_notes(drumBeat, track=0, channel=9) #Channel 9 = Percussion
    m2.seq_notes(melody, track=1, channel=0)

    m2.write("output.mid")
    print("Success")
