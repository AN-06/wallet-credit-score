import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.preprocess import load_json, parse_transactions
from src.feature_engineering import extract_features
from src.scoring import score_wallets

def main():
    data_path = 'data/user_transactions.json'
    output_csv = 'outputs/wallet_scores.csv'
    output_plot = 'outputs/score_distribution.png'

    # Step 1: Load & parse
    print("Loading and parsing transactions...")
    data = load_json(data_path)
    df = parse_transactions(data)

    # Step 2: Feature engineering
    print("Extracting features...")
    features_df = extract_features(df)

    # Step 3: Scoring
    print("Scoring wallets...")
    scored_df = score_wallets(features_df)

    # Step 4: Save scores
    os.makedirs("outputs", exist_ok=True)
    scored_df.to_csv(output_csv, index=False)
    print(f"Scores saved to {output_csv}")

    # Step 5: Plot score distribution
    print("Plotting score distribution...")
    plt.figure(figsize=(10, 6))
    sns.histplot(scored_df['credit_score'], bins=10, kde=True)
    plt.title("Wallet Credit Score Distribution")
    plt.xlabel("Credit Score")
    plt.ylabel("Wallet Count")
    plt.savefig(output_plot)
    print(f"Plot saved to {output_plot}")


if __name__ == "__main__":
    main()
