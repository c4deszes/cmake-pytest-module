import pytest

test_executed = False
every_test_skipped = True

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global every_test_skipped, test_executed
    outcome = yield
    test_executed = True

    rep = outcome.get_result()

    if not rep.skipped and rep.when == 'setup':
        every_test_skipped = False

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session: pytest.Session, exitstatus: int):
    try:
        # Before pytest 5 the values were contants
        from _pytest.main import EXIT_NOTESTSCOLLECTED
        no_tests_collected = EXIT_NOTESTSCOLLECTED
    except ImportError:
        # From pytest 5 on the values are inside an enum
        from pytest import ExitCode
        no_tests_collected = ExitCode.NO_TESTS_COLLECTED
    if test_executed and every_test_skipped:
        session.exitstatus = no_tests_collected
