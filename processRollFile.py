# Jeffrey Trevino, 6/8/18
# program for processing piano roll MIDI file


class RollMIDIFile():
    pass

    def __init__(self, path):
        # loads .mid from disk and returns event list
        # input: path to MIDI file to process
        # output: MIDI file event list
        pass

    def _find_first_demarcator(self):
    # find first song demarcator and return truncated event list
    # input: event list, list of possible demarcators
    # output: truncated event list
        pass

    def _strip_control_pitches(self):
    # strips control pitches from remaining event list
    # input: event list, list of pitches to strip
    # output: filtered event list
        pass
    def _write_output_file(self):
    # write new MIDI file to disk
        pass
    def clean_file(self):
    # cleans the instance's event list and writes the cleaned event list to a new midi file.
    # input: none
    # output: none
    self._find_first_demarcator()
    self._strip_control_pitches()
    self._write_output_file()

my_file = RollMIDIFile()
my_file.clean_file()
