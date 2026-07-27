import logging
import subprocess
import shutil
import tempfile
import os.path


from .merge import merge
from .split import split

logger = logging.getLogger()


def recto(filename, output=None, *, engine='pdfjam'):
    dirpath = tempfile.mkdtemp()
    logger.debug(f'Temp directory {dirpath}')

    logger.debug('Split pages...')
    split(filename, output='PAGE-%05d-1.pdf', outpath=dirpath)

    logger.debug(os.listdir(dirpath))
    num_pages = len([name for name in os.listdir(dirpath)])
    logger.debug(f'PDF has {num_pages}')

    logger.debug('Create blank pages...')
    for i in range(num_pages):
        number = str(i+1).zfill(5)
        blank_path = os.path.join(dirpath, f'PAGE-{number}-2.pdf')
        command = ['convert', 'xc:none', '-page', 'A4', blank_path]

        logger.debug(f'Executed command: {command}')
        subprocess.run(command, check=True)

    pages = [os.path.join(dirpath, name) for name in os.listdir(dirpath)]

    if output is None:
        output = 'RECTO-' + filename

    merge(sorted(pages), output=output)

    shutil.rmtree(dirpath)
