# Contribution Guide

## Coding Standard
Contributors SHOULD follow
[Python Enhancement Proposals](https://www.python.org/dev/peps/) such as:

- [PEP 0008 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 0257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

### Unit Tests

Ensure you don't break unit tests that already are functional and do your best
to increase the code coverage when possible.

**Running Unit Tests:**

```sh
# --stop        Stop processing tests on failure
# --verbose     Increase verbosity
# --nocapture   Display the stdout from each test
nosetests \
    --stop \
    --verbose=2
```

**Checking Test Coverage:**

```sh
nosetests \
    --with-coverage \
    --cover-erase \
    --cover-package=egswanmgr \
    --cover-html

# Open the coverage report
xdg-open cover/index.html
```

***Installing Dependencies:***

- *For both development and testing:*

    ```sh
    pip install -e .[dev] -e .[test]
    ```

- *For development-only:*

    ```sh
    pip install -e .[dev]
    ```

- *For testing-only:*

    ```sh
    pip install -e .[test]
    ```
