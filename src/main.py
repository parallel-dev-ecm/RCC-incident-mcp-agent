import os
import pandas as pd
import json
from utils import load_json, preprocess
from classifier import IncidentClassifier
import matplotlib.pyplot as plt

def run_mcp_agent(input_path, output_path):
    # Load and preprocess
    incidents = load_json(input_path)
    df = preprocess(incidents)

    # Initialize classifier
    clf = IncidentClassifier()

    # Apply classification
    df[["classification", "confidence"]] = df.apply(
        lambda row: pd.Series(clf.classify(row)), axis=1
    )

    # Save result as JSON
    result = df.to_dict(orient="records")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=4, default=str)

    # Print summary to terminal
    print("✅ Classification complete.")
    print(df[["incident_id", "classification", "confidence"]])
    plot_classification_summary(df)


def plot_classification_summary(df):
    counts = df["classification"].value_counts()
    plt.figure(figsize=(6, 4))
    counts.plot(kind="bar", color="skyblue")
    plt.title("Incident Classification Summary")
    plt.xlabel("Classification")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input_file = "data/sample_input.json"
    output_file = "output/classified_output.json"
    run_mcp_agent(input_file, output_file)