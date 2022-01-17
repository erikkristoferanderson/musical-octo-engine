import synthesizer
from synthesizer import Player, Synthesizer, Waveform

synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.3, use_osc2=False)
player = Player()
player.open_stream()


def play_a_sound():
    print('sound!')


def play_a_note(note):
    player.play_wave(synthesizer.generate_constant_wave(note, 1.0))


def play_notes(notes_to_play):
    player.play_wave(synthesizer.generate_chord(notes_to_play, 1.0))


def go(var1, var2, var3, var4, var5, var6, var7, var8):
    val_1 = var1.get()
    val_2 = var2.get()
    val_3 = var3.get()
    val_4 = var4.get()
    val_5 = var5.get()
    val_6 = var6.get()
    val_7 = var7.get()
    val_8 = var8.get()

    vals = [val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8]
    if sum(vals) == 8 or sum(vals) == 4 or sum(vals) == 1:
        notes = ["C3", "E3", "G3", "C4", "D4", "E4", "G4", "A4"]
    elif sum(vals) == 7 or sum(vals) == 2:
        notes = ["C3", "Eb3", "G3", "C4", "D4", "Eb4", "G4", "A4"]
    elif sum(vals) == 6 or sum(vals) == 3:
        notes = ["C3", "F3", "Ab3", "C4", "Eb4", "F4", "Ab4", "Bb4"]
    elif sum(vals) == 5:
        notes = ["C3", "Eb3", "G3", "C4", "D4", "Eb4", "G4", "A4"]
    else:
        notes = ["C3", "E3", "G3", "C4", "D4", "E4", "G4", "A4"]

    zipped_notes_and_vals = zip(notes, vals)

    notes_to_play = [note for note, val in zipped_notes_and_vals if val]
    print(notes_to_play)
    if len(notes_to_play) > 0:
        play_notes(notes_to_play)
    else:
        print("Zounds, Batman!")
