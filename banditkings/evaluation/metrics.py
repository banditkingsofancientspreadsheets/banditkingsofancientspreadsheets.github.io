# Custom function to create custom metrics


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    # Calculate evaluation metrics
