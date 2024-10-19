import sys,argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog='AoC DayFile Creator')
parser.add_argument('day_num',type=int,help='day of the advent to create files for')
arg = parser.parse_args()

d = str(arg.day_num).rjust(2,'0')
Path(f'day_{d}.txt').touch()
Path(f'day_{d}.py').touch()
Path(f'day_{d}_test.txt').touch()