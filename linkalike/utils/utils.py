"""Utilities."""
import numpy as np
import pandas as pd
from tqdm import tqdm


def pairwise_dissimilarities(df, cols=None, indices=None, verbose=False):
    """
    Compute pairwise dissimilarities between rows in a dataframe.

    The dissimilarity between two rows is taken as the number of
    column-wise mismatches.

    Parameters
    ----------
    df : pd.DataFrame
    cols : list or pandas.core.indexes.range.RangeIndex, default=None
    indices : list or pandas.core.indexes.base.Index, default=None
    verbose : bool, default=False

    Example
    -------
    >>> # Making a fake and small dataset
    >>> import numpy as np
    >>> import pandas as pd
    >>> lipsum = "Lorem ipsum dolor sit amet".split(" ")
    >>> N = 7
    >>> nodes = [f"n{i}" for i in range(N)]
    >>> rnd = np.random.RandomState(seed=42)
    >>> df = pd.DataFrame(
    ...     rnd.choice(lipsum, size=(N, 4), replace=True), index=nodes)
    >>> df.to_numpy().tolist()
    [
        ['sit', 'amet', 'dolor', 'amet'],
        ['amet', 'ipsum', 'dolor', 'dolor'],
        ['dolor', 'amet', 'sit', 'dolor'],
        ['amet', 'ipsum', 'sit', 'ipsum'],
        ['sit', 'amet', 'Lorem', 'sit'],
        ['ipsum', 'amet', 'sit', 'Lorem'],
        ['Lorem', 'dolor', 'dolor', 'ipsum']
    ]

    >>> # Computing the pairwise dissimilarities
    >>> from linkalike.utils.utils import pairwise_dissimilarities
    >>> dist_df = pairwise_dissimilarities(df)
    >>> dist_df.to_numpy().tolist()
    [
        [0, 3, 3, 4, 2, 3, 3],
        [3, 0, 3, 2, 4, 4, 3],
        [3, 3, 0, 3, 3, 2, 4],
        [4, 2, 3, 0, 4, 3, 3],
        [2, 4, 3, 4, 0, 3, 4],
        [3, 4, 2, 3, 3, 0, 4],
        [3, 3, 4, 3, 4, 4, 0]
    ]

    """
    if cols is None:
        cols = df.columns
    if indices is None:
        indices = df.index

    assert set(indices).issubset(df.index)
    assert set(cols).issubset(df.columns)

    arr = df.loc[indices, cols].to_numpy()
    nrows, _ = arr.shape
    distances = np.zeros((nrows, nrows), dtype=int)

    for k in (tqdm(range(nrows), desc='Users') if verbose else range(nrows)):
        arr_shifted = np.roll(arr, shift=-k, axis=0)  # Upward circular shift
        dist = np.diag(
            np.count_nonzero(arr != arr_shifted, axis=1)
        ).astype(int)
        # Storing these distances in the k-th diagonal
        distances += np.roll(dist, shift=k, axis=1)

    return pd.DataFrame(distances, columns=indices, index=indices)
