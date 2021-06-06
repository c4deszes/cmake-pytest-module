cmake_minimum_required(VERSION 3.18)

project(PytestExample)

find_package(Python COMPONENTS Interpreter Development)
enable_testing()

include(../Pytest.cmake)

pytest_discover_tests(
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    TEST_PREFIX "PYTEST_"
    TEST_SUFFIX "_${CMAKE_SYSTEM_PROCESSOR}"
    XML_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/report
)
