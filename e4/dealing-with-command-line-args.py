"""
    Nothing robust or complex, just getting feet wet with sys.argv and argparse
"""
from sys import argv
import argparse

class solution():
    def parseArgs(self, argv):
        # Help cases
        if "-h" in argv:
            print("A simple script for practicing dealing with sys.argv and argparse")
            argv.remove("-h")
        if "-help" in argv:
            print("A simple script for practicing dealing with sys.argv and argparse")
            argv.remove("-help")

        # Sample flags which change some arbitrary setting
        if "-v" in argv:
            v = True
        if "-t" in argv:
            t = True
        if "-x" in argv:
            x = True

class solution2():
    def parseArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(dest="command", choices=["cat","ls","rm","head", "tail"], help="This is the command which will envoke")
        # Simple flag arguments
        parser.add_argument('-v', action="store_true", default=False)
        parser.add_argument('-t', type=int, default=0)
        args = parser.parse_args()

        print(args.command)

sol1=solution()
sol1.parseArgs(argv)
print("===============\nArgparse Implementation\n")
sol2=solution2()
sol2.parseArgs()
