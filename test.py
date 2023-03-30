import argparse
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="My Image Classifier",
        description="JANE DOE - UVA SDS DS:6210 Final Project",
    )
    parser.add_argument("imagedir", type=str, help="Test image directory path.")
    parser.add_argument("labelfile", type=str, help="Test annotation file path.")

    args = parser.parse_args()
    print(args)
    filelist = list(Path(args.imagedir).glob("*.*"))
    for filepath in filelist:
        print(filepath)
