from sklearn.base import BaseEstimator, RegressorMixin
from elmpy.elm import ELMRegressor


class ELMRegressor(ELMRegressor, BaseEstimator, RegressorMixin):
    pass
