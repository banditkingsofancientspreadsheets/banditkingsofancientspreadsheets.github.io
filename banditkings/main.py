"""
With this structure, the `DataScienceHelper` class in `main.py` orchestrates
the overall data science pipeline, while the specific implementations of
data loading, transformation, modeling, evaluation, and experiment tracking
are separated into their respective modules and files. This separation of
concerns promotes code reusability, maintainability, and testability.
"""

from data.load import load_data
from data.transform import transform_data
from data.data_splitting.train_test_split import split_data
from modeling.base import BaseModel
from modeling.sklearn_models import SklearnModel
from evaluation.metrics import evaluate_model
from experiments.tracking import log_experiment


class DataTransformer:
    # ETL helper class
    def __init__(self, data_path):
        self.data_path = data_path

    def run_etl(self):
        df = load_data(self.data_path)
        transformed_df = transform_data(df)


class DataScienceHelper:
    def __init__(self, data_path, experiment_name) -> None:
        self.data_path = data_path
        self.experiment_name = experiment_name

    def run_experiment(self, model_params):
        # model_params should be a dict i.e. model_params['model_type']

        if model_params["model_type"] == "sklearn":
            model = SklearnModel(**model_params)
        else:
            raise ValueError("Invalid model type")

        # Insert pipeline stuff here
        X_train, X_test, y_train, y_test = split_data(transformed_df)
        model.train(X_train, y_train)
        metrics = evaluate_model(model, X_test, y_test)
        log_experiment(self.experiment_name, model, metrics)


if __name__ == "__main__":
    pass
