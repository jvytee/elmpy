from sklearn.base import BaseEstimator, RegressorMixin
import elmpy


class ELMRegressor(elmpy.ELMRegressor, BaseEstimator, RegressorMixin):
    pass
