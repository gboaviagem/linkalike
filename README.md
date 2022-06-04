# LinkAlike
![coverage](./coverage.svg)

LinkAlike aims to build recommender systems using graph link prediction.
As many have written about, the problem of product recommendation may be
described as the prediction of a future edge in a user-item graph.
This graph may be bipartite (i.e. only edges from users to items exist) or
 we may define edges between users or between
items, providing a flavour of content-based recommendation.

## Instalation

It is recommended to create a separated python environment to run `linkalike`. If one chooses to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (my personal favorite), an appropriate environment is created and open through the lines
```sh
conda create --name linkalike_env python=3.7
conda activate linkalike_env
```

Then, the packages can be pip-installed from Github,

```sh
python -m pip install git+https://github.com/gboaviagem/linkalike@main
```

or one may choose to simply install its dependencies:

```sh
git clone https://github.com/gboaviagem/linkalike
cd gspx
bash install.sh
```

## Running unit tests locally

When unit tests are implemented, one may run using `pytest`:
```sh
python -m pytest --cov=linkalike .
```
To update the coverage badge, run
```sh
rm coverage.svg && coverage-badge -o coverage.svg
```

## Update version in production

Update setup.py version and packages and generate package by running:

```sh
python setup.py sdist bdist_wheel
```

## Acknowledgements

The pre-commit hook used to verify codestyle was copied from
[https://github.com/cbrueffer/pep8-git-hook](https://github.com/cbrueffer/pep8-git-hook).
