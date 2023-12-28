# rename.py | change the filename for generated file
# author: mairebaap

import os
import argparse as ap

# create arguments for usablility

argument = ap.ArgumentParser()

argument.add_argument('--fn', help='filename', type=str)
argument.add_argument("--ren", help='renames the file', type=str)
argument.add_argument('--ext', help='extension of the file', type=str)
args = argument.parse_args()

filename = args.fn
rename = args.ren + "." + args.ext

os.rename(filename, rename)