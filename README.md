# CMake Pytest module

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

> This module allows the discovery of Pytest scripts and exposes them through CTest.

---

## About

The advantage of using this module is that you can use a common filtering and
configuration mechanism if you use CMake with for example GoogleTest or other
tools that also integrate into the CTest runner.

---

## Usage

In your CMake include the `Pytest.cmake` file, you must enable tests in your project
as well as have a suitable Python installation with Pytest module installed.

```cmake
project(MyProject)

find_package(Python COMPONENTS Interpreter Development)
enable_testing()

include(Pytest.cmake)

pytest_discover_tests(
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    TEST_PREFIX "UNITTEST_"
    TEST_SUFFIX "_${CMAKE_SYSTEM_PROCESSOR}"
    XML_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/report
)
```

For more information see the [module](Pytest.cmake) itself, it has inline documentation.

### Skipped tests

During execution tests that are deselected will be marked as skipped, this should only happen
if the collection arguments were different than execution arguments. Skipped tests can also be
picked up by ctest but this requires setting the exit code to 5 when no tests were executed,
something which is not done by `pytest`, see issues [#812](https://github.com/pytest-dev/pytest/issues/812)
and [#5689](https://github.com/pytest-dev/pytest/issues/5689).
This can be solved with a few hooks, see [example conftest](example/conftest.py).

---

## License

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
