import subprocess
import logging
import shutil

from ._utils import default_output

logger = logging.getLogger()

ROTATIONS = {'0': 'north', '90': 'east', '180': 'south', '270': 'west'}


def rotate(filename, angle=90, output=None):
    if output is None:
        output = default_output('ROTATED', filename)

    if shutil.which('mutool'):
        command = ['mutool', 'clean', '-R', str(angle), filename, output]
    elif shutil.which('pdftk'):
        direction = ROTATIONS.get(str(angle), 'east')
        command = ['pdftk', filename, 'cat', f'1-end{direction}', 'output', output]
    else:
        raise RuntimeError('No engine found among mutool, pdftk.')

    logger.debug(f'Executed command: {command}')
    subprocess.run(command, check=True)
