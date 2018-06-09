# Jeffrey Trevino, 6/8/18
# program for processing piano roll MIDI file
import mido

class RollMIDIFile():

    def __init__(self, input_path):
        # loads .mid from disk as attribute "input_mid"
        self._input_path = input_path
        self.input_mid = mido.MidiFile(input_path)

    def _strip_control_pitches(self, control_pitch_list):
    # strips control pitches from remaining event list
    # input: event list, list of pitches to strip
    # output: filtered event list
        for track in self.input_mid.tracks[1:]:
            for event in track:
                if event.type == 'note_on' or event.type == 'note_off':
                    if event.note in control_pitch_list:
                        print("Silencing" + str(event))
                        event.velocity = 0

    def _write_output_file(self):
    # write new MIDI file to disk
        self.input_mid.save(self._input_path[:-4] + "clean.mid")

    def _set_tempo(self, tempo_scale_factor=1.0):
        # the third message in the first track will be the tempo message
        # first, set it to 1000000 microseconds per quarter, the default for the file before edit
        # then multiply the value by the scale factor (1.2 to get to 50 bpm).
        current_tempo = self.input_mid.tracks[0][2].tempo
        self.input_mid.tracks[0][2].tempo = int(current_tempo * 2 * tempo_scale_factor)

    def clean_file(self, tempo_scale_factor=1.0, control_pitches=[]):
    # cleans the instance's event list and writes the cleaned event list to a new midi file.
    # input: none
    # output: none
        self._set_tempo(tempo_scale_factor)
        self._strip_control_pitches(control_pitches)
        self._write_output_file()
