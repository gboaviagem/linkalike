"""Utilities for graphs."""
import networkx as nx


def make_edgelist(
        df, from_node='USER_ID', to_node='ITEM_ID', weight=None,
        meta_cols=None):
    """Make the edgelist out of a dataset.

    The only edge attribute currently avaiable is `weight`.

    Parameters
    ----------
    df : pd.DataFrame
    from_node : str, default='USER_ID'
        Name of column with source nodes.
    to_node : str, default='ITEM_ID'
        Name of column with destination nodes.
    weight : str, default=None
        Name of column in the dataset with the weight of the edge.

    """
    meta_cols = _check_meta(df, from_node, meta_cols)
    meta_cols = _check_meta(df, to_node, meta_cols)

    if weight is not None:
        df_ = df.rename(columns={weight: 'weight'})

        while weight in meta_cols:
            meta_cols.remove(weight)

        meta_cols = ['weight'] + meta_cols
        elist = [
            tuple([e[0], e[1], {'weight': e[2]}])
            for e in df[[from_node, to_node, weight]].to_numpy()
        ]
        elist = [
            tuple([
                d[from_node], d[to_node],
                {k: v for k, v in d.items() if k not in [from_node, to_node]}
            ]) for d in
            df[[from_node, to_node] + meta_cols].to_dict(orient='records')
        ]
    else:
        elist = [tuple(e) for e in df[[from_node, to_node]].to_numpy()]

    return elist


def make_nodelist(df, node_id='USER_ID', meta_cols=None):
    """Make the nodelist out of a dataset.

    Parameters
    ----------
    df : pd.DataFrame
    node_id : str, default='USER_ID'
        Name of User column in the datasets.
    meta_cols : list of str, default=None
        List of node metadata columns, if any.
        If None, no column is used as metadata.

    """
    meta_cols = _check_meta(df, node_id, meta_cols)
    nodelist = [
        tuple([d[node_id], {k: v for k, v in d.items() if k != node_id}])
        for d in df[[node_id] + meta_cols].to_dict(orient='records')
    ]
    return nodelist


def _check_meta(df, node_id, meta_cols=None):
    if meta_cols is None:
        meta_cols = list()
    assert isinstance(meta_cols, list), (
        "The metadata columns must be provided as a list of str."
    )

    while node_id in meta_cols:
        meta_cols.remove(node_id)

    not_found = set(meta_cols) - set(df.columns)
    assert len(not_found) == 0, (
        "The following metadata columns are not found among "
        f"the input dataframe: {not_found}."
    )
    return meta_cols
