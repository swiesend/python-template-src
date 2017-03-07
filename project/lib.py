"""An example library.

Here you can see how to implement some functionality.
"""

def hello(*args,**kwargs):
    """A placeholder function which prints its input arguments.

    This `docstring` is part of the sphinx documentation. You can build the
    documentation by running (from the project's ``root`` directory)::

        $ pip install -r requirements.txt           \n
        $ sphinx-apidoc -f -o docs/source project   \n
        $ cd docs                                   \n
        $ make html

    Have fun!

    Arguments:
        *args       (list): anonym function arguments
        **kwargs    (dict): named function arguments

    Returns:
        None:    only prints to stdout

    Examples:
        Examples should be written in `doctest` format, and should illustrate how
        to use the function.

        >>> hello("world")
        ('world',) {}

        >>> hello(greet="everyone")
        () {'greet': 'everyone'}

    """
    print(args, kwargs)
