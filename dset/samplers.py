
import torch
from torch.utils.data.sampler import Sampler

class Sampler(Sampler):
    def __init__(self, data_source):
        pass

    def __iter__(self):
        """Provides a way to iterate over the indices of dataset elements
        """
        raise NotImplementedError

    def __len__(self):
        """Returns the length of the returned iterators
        """
        raise NotImplementedError
