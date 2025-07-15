import pandas as pd
import time

def extract_features(df):
    features = []
    grouped = df.groupby('wallet')

    current_time = int(time.time())

    for wallet, group in grouped:
        tx_count = len(group)
        active_days = (group['timestamp'].max() - group['timestamp'].min()) // 86400
        active_days = max(1, active_days)  # avoid divide-by-zero

        total_usd_value = group['usd_value'].sum()
        avg_usd_value = group['usd_value'].mean()
        unique_actions = group['type'].nunique()
        days_since_last_tx = (current_time - group['timestamp'].max()) // 86400

        deposit_usd = group[group['type'] == 'deposit']['usd_value'].sum()
        redeem_usd = group[group['type'] == 'redeemunderlying']['usd_value'].sum()
        borrow_usd = group[group['type'] == 'borrow']['usd_value'].sum()
        repay_usd = group[group['type'] == 'repay']['usd_value'].sum()

        deposit_redeem_ratio = redeem_usd / deposit_usd if deposit_usd > 0 else 0
        borrow_repay_ratio = repay_usd / borrow_usd if borrow_usd > 0 else 0

        feats = {
            'wallet': wallet,
            'tx_count': tx_count,
            'active_days': active_days,
            'total_usd_value': total_usd_value,
            'avg_usd_value': avg_usd_value,
            'unique_actions': unique_actions,
            'days_since_last_tx': days_since_last_tx,
            'deposit_redeem_ratio': deposit_redeem_ratio,
            'borrow_repay_ratio': borrow_repay_ratio
        }

        features.append(feats)

    return pd.DataFrame(features)
