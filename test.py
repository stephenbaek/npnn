import argparse
from pathlib import Path


def __main__():
    parser = argparse.ArgumentParser(
        prog="My Image Classifier",
        description="JANE DOE - UVA SDS DS:6210 Final Project",
    )
    parser.add_argument("dirpath")

    args = parser.parse_args()

    filelist = list(Path(args.dirpath).glob("*.*"))
    for filepath in filelist:
        print(filepath)
