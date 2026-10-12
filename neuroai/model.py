"""Baseline model training and evaluation for NeuroAI. Includes two data-splitting strategies used to demonstrate why participant-level splitting matters."""

# LATER: not needed for the Voice Lab MVP


def participant_level_split(df):
    """Split data so that all recordings from the same participant stay in the same split (no leakage)."""
    # TODO: I will implement this
    pass


def recording_level_split(df):
    """Split data by individual recording, ignoring participant identity. Deliberately flawed: used only to demonstrate data leakage."""
    # TODO: I will implement this
    pass


def train_baseline(X, y):
    """Train a simple baseline classifier on the extracted features."""
    # TODO: I will implement this
    pass


def evaluate(model, X, y):
    """Evaluate a trained model on held-out data and return performance metrics."""
    # TODO: I will implement this
    pass


def explain_with_shap(model, X):
    """Generate SHAP explanations showing which features drove the model's predictions."""
    # TODO: I will implement this
    pass
