## MIDI Processing for Piano Roll Scan MIDI Files

This Python code (1) finds the first song demarcator, (2) truncates the MIDI file to everything after the first demarcator, and (3) writes a new MIDI file (to the run directory) that no longer contains any of the sustain pedal, xylophone, and mandolin control note on/off events.
