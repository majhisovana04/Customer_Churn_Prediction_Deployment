import joblib

model = joblib.load("churn_model.pkl")

print("Model type:", type(model))

# If it's a pipeline, show steps
if hasattr(model, "steps"):
    print("\nPipeline steps:")
    for name, step in model.steps:
        print(f"{name} -> {type(step)}")
else:
    print("\nNot a pipeline model")
    print("Model type:", type(model))
    print("Number of input features:", model.n_features_in_)

