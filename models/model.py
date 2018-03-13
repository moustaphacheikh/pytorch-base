
import argparse

import torch
import torch.nn as nn

def add_model_options(parser):
    """This function takes a child parser and adds all 
       options corresponding to the model hyperparameters.
    """
    raise NotImplementedError

def validate_model_options(options, args):
    """Given the parsed options and arguments, this function makes 
       sure that all the values are valid.
    """
    raise NotImplementedError

class Model(nn.Module):
    def __init__(self):
        super(self, Model).__init__()
        pass

    def forward(self, x):
        raise NotImplementedError
