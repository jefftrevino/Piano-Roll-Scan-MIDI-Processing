from setuptools import setup

setup(name='process roll file',
      version='0.0.1',
      py_modules=['process_roll_file'],
      author='Jeffrey Trevino',
      description='process-roll-file is a package for stripping MIDI files of leaders and certain pitches',
      author_email='jeffrey.trevino@gmail.com',
      url='https://github.com/jefftrevino/Piano-Roll-Scan-MIDI-Processing',
      install_requires=(
        'mido',
        ),
      )
