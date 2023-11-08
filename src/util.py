from typing import Iterable
from itertools import islice


def batch(dataset: Iterable, batch_size: int) -> Iterable:
    """Creates batches from an iterable.

    Args:
        dataset (Iterable): Your dataset you want to batch given as an iterable (e.g. a list).
        batch_size (int): Your desired batch size
    
    Returns:
        Iterable: An iterable of tuples of size equal to batch_size.

    Example:
        >>> batches = batch([1,2, 3, 4, 5], 2)
        >>> print(list(batches))
        [(1, 2), (3, 4), (5,)]
    """
    iterable_dataset = iter(dataset) # dataset as input - iterate over it 
    while True:
        chunk = tuple(islice(iterable_dataset, batch_size)) # slicing with non-negatives 
        # up to the batch size group together and then drop from data - do the same for the remaining data
        if not chunk: # when the dataset is empty break the while loop
            break
        yield chunk
    
    # This function divides data into batches of 32 tokens 
    # Using iterable concept: any object which can be iterated over - like a list