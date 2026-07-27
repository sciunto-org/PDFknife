import subprocess
import logging

from ._utils import default_output

logger = logging.getLogger()


def clean(filename, output=None):
    if output is None:
        output = default_output('CLEANED', filename)

    command = ['gs',
               '-dNOPAUSE',
               '-dBATCH',
               '-sDEVICE=pdfwrite',
               '-dCompatibilityLevel=1.4',
               '-dPDFSETTINGS=/prepress',
               '-dAutoRotatePages=/None',
               '-sOutputFile=' + output,
               filename]
    logger.debug(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
