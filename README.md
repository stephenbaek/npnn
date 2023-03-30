# DS 6210 Numerical Analysis and Optimization Final Project

This repository contains source codes to help students get started with their final project for the 'DS 6210 Numerical Analysis and Optimization for Data Science' course at the University of Virginia School of Data Science. The main objective of this project is to write an image classifier and two gradient-based optimizers to train the classifier from scratch, only using NumPy and Autograd. The performance of the classifier will be assessed on the Tiny ImageNet data set, in which Top-1 and Top-5 accuracies are going to be measured. Anything you introduce in addition to the "vanilla-flavored algorithms" will be subject to extra credits (e.g., varying numerical precisions, safeguarding the numerical sensitivity). This code base is intended to help students jumpstart their project.

## Getting Started
You are encouraged to create a virtual environment using for example (mini)conda or `venv`. In the example below, I'll use `conda` to create a virtual environment named `npnn`.

```bash
conda create -n npnn python=3.9
```

Once a virtual environment has been created, activate the virtual environment.
```bash
conda activate npnn
```

There are several 3rd party libraries used in the starter codes, as listed in the `requirements.txt` file. To install them, simply run the following command.
```bash
pip install -r requirements.txt
```

Now you are all set. Good luck with your project!

## Index
- `data.ipynb`: a Jupyter Notebook to walk you through the process of downloading, reading, parsing, and preprocessing the Tiny ImageNet data set.
- `test.py`: Test file to evaluate your model performance. This file is necessary for submission. Usage example: `python test.py tiny-imagenet-200/val tiny-imagenet-200/val/val_annotations.txt`
