# Kubernetes ePUB Documentation

### This repository contains all the [Kubernetes documentation](https://kubernetes.io/docs/home/) in ePUB format, generated automatically.

## How the files are structured?
ePUB files are grouped in sections:

* Setup
* Concepts
* Getting Started Guide (Independent Solutions)
* Tasks
* Tutorials
* Reference
* Imported Docs

For a more detailed index, see [here](https://kubernetes.io/docs/home/#browsedocs)

## Dependencies
* `librsvg`: For Mac: `brew install librsvg`. [ref](https://pypi.org/project/foliantcontrib.pandoc/)
* `python3`
    * `pipenv`
    * `pypandoc`
    * `requests-html`

# How to run the code
1. Install the dependencies. Use `$ pipenv install` for installing python packages.
2. `$ pipenv shell`
3. `$ python kubernetes-doc.py`
