Strange python import issue, example project. Contains two packages:

    ns.one
    ns.two

Install both with pip, but install one in development mode.

    virtualenv venv
    venv/bin/pip install ns.one/
    venv/bin/pip install -e ns.two/

Now watch as ns.one can import but ns.two cannot:

    venv/bin/python
	>>> import ns.one
	>>> import ns.two
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ImportError: No module named two

But if you import pkg_resources first, no problem:

    >>> import pkg_resources
    >>> import ns.two

Notice also that any entry_point defined script has no problem finding an
import because pkg_resources is involved in finding entry points:

    venv/bin/pip install helloworld/
    venv/bin/helloworld

This succeeds without failure even though helloworld imports ns.two.
