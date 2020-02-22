import pytest
import numpy as np

from elmpy import ELMRegressor


class TestELMRegressor:
    def test_init(self):
        elm = ELMRegressor()

        assert elm.n_hidden == 50
        assert elm.alpha == 1.0
        assert elm.gamma is None

        assert elm.w_in is None
        assert elm.w_out is None
        assert elm.bias is None

    def test_fit(self):
        elm = self.fit_elm()

        assert elm.w_in.shape == (50, 1)
        assert elm.bias.shape == (50,)
        assert elm.w_out.shape == (50, 2)

    def test_predict(self):
        elm = self.fit_elm()

        assert elm.predict(np.array([5])).shape == (2,)

    def fit_elm(self):
        xs = np.vstack(np.arange(0, 10, 0.1))
        ys = np.hstack([np.sin(xs), np.cosh(xs)])

        elm = ELMRegressor()
        elm.fit(xs, ys)

        return elm
