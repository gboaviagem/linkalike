"""Some useful datasets."""
import pathlib
import pandas as pd


def movielens100k():
    """Fetch the movielens 100k dataset.

    The MovieLens 100k can be found here [1]_.

    Return
    ------
    interactions : pd.DataFrame
    users : pd.DataFrame
    items : pd.DataFrame

    References
    ----------
    [1] https://grouplens.org/datasets/movielens/100k/

    """
    root = pathlib.Path(__file__).parent.parent / "resources"
    data = pd.read_csv(root / "ml_100k_data.gz", sep=",")
    user = pd.read_csv(root / "ml_100k_user.gz", sep=",")
    item = pd.read_csv(root / "ml_100k_item.gz", sep="|")

    return data, user, item
