# Placeholders for performing experiment tracking and logging, i.e. mlflow
import mlflow

def log_experiment(experiment_name, model, metrics):
    mlflow.set_experiment(experiment_name)
    # Log model and metrics to MLflow