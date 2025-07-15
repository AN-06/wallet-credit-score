def score_wallets(features_df):
    df = features_df.copy()

    # Normalize select features (0 to 1 scale)
    for col in ['tx_count', 'unique_actions', 'total_usd_value', 'avg_usd_value']:
        df[col + '_score'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min() + 1e-6)

    # Recency score (lower days = better)
    df['recency_score'] = 1 - (df['days_since_last_tx'] / (df['days_since_last_tx'].max() + 1e-6))

    # Ratio balance score: if well-behaved, ratios should be close to 1
    df['behavior_score'] = 1 - abs(df['deposit_redeem_ratio'] - 1) / (df['deposit_redeem_ratio'] + 1)
    df['behavior_score'] += 1 - abs(df['borrow_repay_ratio'] - 1) / (df['borrow_repay_ratio'] + 1)
    df['behavior_score'] = df['behavior_score'] / 2  # average

    # Final weighted score
    df['final_score'] = (
        0.4 * df['tx_count_score'] +
        0.2 * df['recency_score'] +
        0.2 * df['behavior_score'] +
        0.2 * df['unique_actions_score']
    )

    # Scale to 0–1000
    df['credit_score'] = (df['final_score'] * 1000).astype(int)
    return df[['wallet', 'credit_score']]
