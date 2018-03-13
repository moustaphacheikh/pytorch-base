
import torch
from torch.utils.data import Dataset

class Dataset(Dataset):
    def __init__(self):
        pass

    def __getitem__(self, index):
        """Given some index, this function will return the corresponding
           dataset entry.
        """
        raise NotImplementedError

    def __len__(self):
        """Returns the length of our dataset.
        """
        raise NotImplementedError


