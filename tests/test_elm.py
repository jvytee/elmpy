import pytest
from elmpy import ELMRegressor


class TestELMRegressor:
    def test_init(self):
        elm = ELMRegressor()

        assert elm.w_in is None
        assert elm.w_out is None
        assert elm.bias is None
