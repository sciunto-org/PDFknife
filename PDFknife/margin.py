import subprocess
import logging

from ._utils import default_output

logger = logging.getLogger()


def margin(filename, margin=10, output=None):
    if output is None:
        output = default_output('MARGIN', filename)

    m = f'{margin}mm'
    command = ['pdfjam',
               filename,
               '--trim',
               f'\'-{m} -{m} -{m} -{m}\'',
               '--clip',
               'false',
               '--outfile',
               output,
               ]
    logger.debug(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
