"""User-item graph."""
import networkx as nx

from linkalike.utils.graph import make_edgelist


class UIGraph():
    """Build a user-item graph.

    Parameters
    ----------
    uid : str, default='USER_ID'
        Name of User column in the datasets.
    iid : str, default='ITEM_ID'
        Name of Item column in the datasets.
    wid : str, default=None
        Name of column with the weights of the interaction between
        user and item. It is usually the rating given by the user.
    umeta : list of str, default=None
        List of user metadata columns, if any.
        If None, no metadata is used.
    imeta : list of str, default=None
        List of item metadata columns, if any.
        If None, no metadata is used.
    only_recommend : function (output -> bool) or list of str, default=None
        It defines a subset of the items which will contain the only
        options for recommendations. In other words, items with IDs
        that do not make `function` True, or do not belong to the list,
        are not recommended at all. They are, however, part of the graph.

    Example
    -------

    """
    FROM_ALIAS = 'FROM'
    TO_ALIAS = 'TO'
    SIM_ALIAS = 'SIMILARITY'

    def __init__(
            self, uid='USER_ID', iid='ITEM_ID', wid=None, umeta=None,
            imeta=None, only_recommend=None):
        """Construct."""
        if only_recommend is not None:
            assert (
                only_recommend.__class__.__name__ == "function" or (
                    isinstance(only_recommend, list) and
                    all(isinstance(i, str) for i in only_recommend)
                    )
                ), (
                    "The `only_recommend` parameter must either "
                    "be a python function or a list of str."
                )
        self.uid = uid
        self.iid = iid
        self.wid = wid
        self.umeta = umeta
        self.imeta = imeta
        self.only_recommend = only_recommend
        self.graph = nx.Graph()

    def build_similarity_dataset(df, id_col, meta_cols=None):
        pass

    def add_nodes(self):
        pass

    def add_edges(self, df, df_user=None, df_items=None):
        elist = make_edgelist(
            df, from_node=self.uid, to_node=self.iid, weight=self.wid)
        self.graph.add_edges_from(elist)

        if df_user is not None:
            elist = make_edgelist(
                df_user,
                from_node=self.FROM_ALIAS, to_node=self.TO_ALIAS,
                weight=self.SIM_ALIAS)
            self.graph.add_edges_from(elist)

        if df_item is not None:
            elist = make_edgelist(
                df_item,
                from_node=self.FROM_ALIAS, to_node=self.TO_ALIAS,
                weight=self.SIM_ALIAS)
            self.graph.add_edges_from(elist)
