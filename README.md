Project
=======

Project is a library made to solve problem x.


# Development

## Testing

### Install package

    $ pip install -e .

### Running tests

    $ pytest tests/

### Running tests with Code Coverage

    $ pytest --cov=project tests/

### Running doctests

    $ pytest --doctest-modules project/

## Documentation

To generate/update the Sphinx documentation from the source code run the following commands:

    $ pip install -r requirements.txt
    $ sphinx-apidoc -f -o docs/source project
    $ cd docs
    $ make html


<!-- * [Changelog](CHANGELOG.md)
* [Contributors](CONTRIBUTORS.md)
* [License](LICENSE.md) -->

### Distribution

In order to distribute your library you can upload it to PyPI

https://packaging.python.org/distributing/

---
Contents
========

```eval_rst
.. toctree::

   CHANGELOG
   CONTRIBUTORS
   LICENSE

   source/modules
```

---

Indices and tables
==================
```eval_rst
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
