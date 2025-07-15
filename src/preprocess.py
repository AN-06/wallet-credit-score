import json
import pandas as pd

def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def parse_transactions(data):
    rows = []

    for record in data:
        action = record.get('action')
        data_field = record.get('actionData', {})
        wallet = record.get('userWallet')
        timestamp = record.get('timestamp')

        amount_str = data_field.get('amount')
        price_str = data_field.get('assetPriceUSD')

        # Safely parse amount and price
        try:
            amount = float(amount_str)
        except (ValueError, TypeError):
            amount = 0.0

        try:
            price = float(price_str)
        except (ValueError, TypeError):
            price = 0.0

        usd_value = amount * price

        rows.append({
            'wallet': wallet,
            'timestamp': timestamp,
            'type': action.lower(),
            'amount': amount,
            'usd_value': usd_value,
        })

    return pd.DataFrame(rows)
