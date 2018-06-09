## MIDI Processing for Orchestrion Roll MIDI Files

This is a Python utility for stripping out pitches from MIDI files: optically scanned orchestrion rolls include several pitches used as control values for sustain, xylophone, mandolin. While potentially converted to something resembling these control functions in the future, the pitches certainly should not sound when the MIDI file plays back, and for the time being, their velocity may be set to a value of zero.

This `process_roll_file` package enables the use of the `RollMIDIFile()` class. The class's `clean_file()` method will import a MIDI file according to a path argument, silence control notes in a list of pitch numbers supplied via the `control_pitches` keyword argument, and scale the tempo of the entire file by a scalar factor supplied via the `tempo_scale_factor` keyword argument.

Dependencies: [mido](https://github.com/olemb/mido)
