# Scripts

1. test_changes.sh - Test if the changes are valid and can be released. flake8/pytest are run and the version is checked.
2. test_release.sh - Test the release on test.pypi.org.
3. release.sh - Release the package to PyPI if both tests are successful.


reference links:

- https://packaging.python.org/en/latest/guides/using-testpypi/
