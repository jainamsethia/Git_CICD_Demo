def predict_label(value):
    """A tiny example function for CI testing."""
    return "positive" if value >= 0.5 else "negative"

def predict_with_message(value):
    label = predict_label(value)
    return f"Model predicts: {label}"

if __name__ == "__main__":
    print("Prediction:", predict_label(0.8))
    print(predict_with_message(0.3))