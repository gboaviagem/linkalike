"""Unit tests."""
import pytest
import numpy as np
import pandas as pd

from linkalike.utils import pairwise_dissimilarities


@pytest.fixture
def df():
    """Input data.

    If one executes `df.to_numpy()`, the output is:

    [
        ['sit', 'amet', 'dolor', 'amet'],
        ['amet', 'ipsum', 'dolor', 'dolor'],
        ['dolor', 'amet', 'sit', 'dolor'],
        ['amet', 'ipsum', 'sit', 'ipsum'],
        ['sit', 'amet', 'Lorem', 'sit'],
        ['ipsum', 'amet', 'sit', 'Lorem'],
        ['Lorem', 'dolor', 'dolor', 'ipsum']
    ]

    """
    # Making a fake and small dataset
    lipsum = "Lorem ipsum dolor sit amet".split(" ")
    N = 7
    nodes = [f"n{i}" for i in range(N)]
    rnd = np.random.RandomState(seed=42)
    df = pd.DataFrame(
        rnd.choice(lipsum, size=(N, 4), replace=True), index=nodes)

    return df


def test_pairwise_dissimilarities(df):
    """Test pairwise dissimilarities on a dataframe."""
    dist_df = pairwise_dissimilarities(df)
    expected = np.array([
        [0, 3, 3, 4, 2, 3, 3],
        [3, 0, 3, 2, 4, 4, 3],
        [3, 3, 0, 3, 3, 2, 4],
        [4, 2, 3, 0, 4, 3, 3],
        [2, 4, 3, 4, 0, 3, 4],
        [3, 4, 2, 3, 3, 0, 4],
        [3, 3, 4, 3, 4, 4, 0]])
    np.testing.assert_array_equal(dist_df.to_numpy(), expected)

    assert all(df.index == dist_df.index)
