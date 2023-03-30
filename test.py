import argparse
import os
from PIL import Image
import numpy as np
from tqdm import tqdm


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog="My Image Classifier",
        description="JANE DOE - UVA SDS DS:6210 Final Project",
    )
    parser.add_argument("imagedir", type=str, help="Test image directory path.")
    parser.add_argument("labelfile", type=str, help="Test annotation file path.")

    args = parser.parse_args()

    # Parse class label names
    labelnames = []
    label2index = {}
    with open('tiny-imagenet-200/wnids.txt', 'r') as f:
        lines = f.readlines()
        labelnames = [line.strip() for line in lines]
        label2index = {label: i for i, label in enumerate(labelnames)}

    # Read labels
    imagepaths = []
    labels = []
    with open(args.labelfile, newline='') as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.strip().split()
            filename = tokens[0]
            label = tokens[1]
            imagepath = os.path.join(args.imagedir, filename)
            if os.path.exists(imagepath):
                imagepaths.append(imagepath)
                labels.append(label)
            else:
                print(f'Warning: {imagepath} cannot be found. Skipping from the list.')

    # Read images
    X = []
    Y = []
    for imagepath, label in tqdm(zip(imagepaths, labels)):
        with Image.open(imagepath) as image:
            X.append(np.array(image.convert('RGB')))
            index = label2index[label]
            Y.append(index)
    X = np.array(X)
    Y = np.array(Y)

    # TODO: Replace the code below with a code to infer your model on the images X.
    A = np.random.rand(64*64*3, 200)
    b = np.random.rand(1,200)
    Z = np.matmul(np.reshape(X, (-1,64*64*3)), A) + b

    # Compute the accuracy
    pred = np.argmax(Z, axis=-1)
    acc = (pred == Y).astype(np.int32)
    print("Accuracy:", np.mean(acc)*100, '%')