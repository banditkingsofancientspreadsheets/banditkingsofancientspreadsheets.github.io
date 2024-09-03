from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, KFold, cross_val_predict, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from .base import BaseModel


class SklearnModel(BaseModel):
    def __init__(self, **params) -> None:
        self.model = None # Initialize scikit-learn model

    def build_pipeline(self, features):
        # specify the sklearn Pipeline here with steps
        pass

    def train(self, X, y):
        self.model.fit(X, y)

    def cross_validate(self, X, y):
        # Train and Cross_validate
        pass

    def predict(self, X):
        # i.e. self.model.predict(X) or self.pipeline.predict(X)
        self.model.predict(X)