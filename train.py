
import argparse
import os
import sys

import torch
import torch.nn as nn
from torch.autograd import Variable

from common import *
from dset import *
from loss import *
from utils import *

parser = argparse.ArgumentParser(description="These options are useful regardless of what model is being trained"
                                             " thus it is fair to call them \"model agnostic\".",
                                 add_help=False)
parser.add_argument("model_name", type=str, default=None,
                    help="Name of the model that should be trained")
parser.add_argument("--learning-rate", type=float, default=0.01,
                    help="Step size to use while taking an optimizer step")
parser.add_argument("--num-epochs", type=int, default=50, 
                    help="Number of times to iterate over dataset")

def main():
    index = -1
    for i, arg in enumerate(sys.argv):
        if arg in VALID_MODEL_NAMES.keys():
            index = i

    global general_args
    general_args = parser.parse_args(sys.argv[1:index+1])
    model_add_options, model_validate_options, model = get_model(general_args.model_name)

    global model_args
    model_parser = argparse.ArgumentParser()
    model_add_options(model_parser)
    model_parser.parse_args(sys.argv[index+1:])
    return 0

if __name__ == "__main__":
    sys.exit(main())
