import process_roll_file

all_roll_strings = ['002', '003', '004', '005', '006', '009', '011', '012', '013', '014']

roll_number_strings_one = ['002', '004', '005', '006', '009', '012', '014']
roll_number_strings_two = ['003', '009', '011',  '013']

def clean_files(roll_number_strings, control_pitches):
    # strip same control pitches from rolls in a list of roll roll_strings
    for roll_number_string in roll_number_strings:
        my_file = process_roll_file.RollMIDIFile("../rolls/roll" + roll_number_string + "/midi" + roll_number_string + "truncated.mid")
        my_file.clean_file(tempo_scale_factor=1.2, control_pitches=control_pitches)
    return my_file

default_control_pitches = [19, 20, 80, 82, 83]
default_control_pitches = [x + 12 for x in default_control_pitches] # octave transposition if necessary
returned_file = clean_files(roll_number_strings_one, default_control_pitches)
returned_file = clean_files(roll_number_strings_two, [x + 2 for x in default_control_pitches])
