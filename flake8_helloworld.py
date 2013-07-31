
__version__ = '0.1'

import pep8


def check_helloworld(physical_line):
    if pep8.noqa(physical_line):
        return
    pos = physical_line.find('Hello World')
    if -1 != pos:
        return pos, 'HW01 use "Hello World"'


check_helloworld.name = name = 'flake8-helloworld'
check_helloworld.version = __version__
