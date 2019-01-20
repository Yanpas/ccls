#!/usr/bin/env python3

import sys
import argparse

from .executor import Executor

def main(args):
	ap = argparse.ArgumentParser("runner")
	ap.add_argument("-e", help="ccls executable path", required=True)
	ap.add_argument("-p", help="path to project to test", required=True)
	apargs = ap.parse_args(args)
	e = Executor(apargs.e, apargs.p)
	e.run()


main(sys.argv[1:])
