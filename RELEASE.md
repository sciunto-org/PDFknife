How to release
==============

* Update CHANGELOG
* Bump version with bumpver:
    pip install bumpver
    bumpver update --patch
* Send the package on pypi
    pip install build twine
    python -m build
    twine upload dist/*
