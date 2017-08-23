'''
    SET PATH
'''
import os

__path__ = [os.path.dirname(os.path.abspath(__file__))]

from .core import __app__

if __name__ == '__main__':
    __app__.run(debug=True)
