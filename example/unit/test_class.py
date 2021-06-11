import pytest

class TestClass:

    def test_case1(self):
        pass

    def test_case2(self):
        pass

    @pytest.mark.skip
    def test_case3(self):
        pass
