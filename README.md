# 💳 DeFi Wallet Credit Scoring (Aave V2)

This project evaluates the behavior and reliability of DeFi wallets by assigning a **credit score (0–1000)** based on their interaction history with Aave V2 protocol. It uses wallet-level transaction data to quantify trust, activeness, and responsibility.

---

## 🏗️ Architecture & Processing Flow

The project processes raw DeFi transaction data and computes wallet credit scores through the following stages:

                                     📥 Input: Raw Aave V2 Data (JSON)
                                                     ↓  
                                           🧹 Preprocessing
                                                     ↓  
                                         📊 Feature Engineering
                                                     ↓  
                                        🧠 Credit Score Modeling
                                                     ↓  
                                           📈 Output Generation


---

## 🧠 Methodology

We derive credit scores using a **rule-based, interpretable approach**. Each wallet's transaction data is aggregated and converted into features that reflect their **activity**, **diversity**, **recency**, and **financial behavior**. Scores are then calculated by:

- ✅ **Feature normalization** (scaled between 0–1)
- ✅ **Weighted aggregation** into a final score
- ✅ **Scaling** to a 0–1000 credit score

---

## 🔍 Features Used

### ✅ Raw Wallet Features

- `tx_count`: Total number of transactions
- `unique_actions`: Number of distinct transaction types
- `total_usd_value`: Total USD-equivalent value transacted
- `avg_usd_value`: Average USD value per transaction
- `days_since_last_tx`: Days since the wallet was last active
- `deposit_redeem_ratio`: Ratio of redeem to deposit amounts
- `borrow_repay_ratio`: Ratio of repay to borrow amounts

---

### 📏 Scoring Weights

| Feature                  | Weight |
|--------------------------|--------|
| Transaction Activity     | 40%    |
| Recency                  | 20%    |
| Behavior Balance (ratios)| 20%    |
| Action Diversity         | 20%    |

---

### 🧮 Final Score Calculation

```python
credit_score = int(final_score * 1000)
```
---

## 📁 Data Setup

⚠️ **Note:** The `data/` folder is not included in this repository due to size restrictions.

To run the scoring system:

1. Create a folder named `data/` in the root directory.
2. Place your Aave V2 JSON file (e.g., `aave_data.json`) inside the folder.
3. Ensure each record follows this format:


```json
{
  "userWallet": "0x...",
  "action": "deposit",
  "actionData": {
    "amount": "100",
    "assetPriceUSD": "1.00"
  },
  "timestamp": 1687632712
}
```
### 🗃️ Data Source

The dataset used here is a raw Aave V2 transaction-level JSON file containing thousands of wallet actions and financial behavior logs:

- 📄 **Raw JSON (~87MB)**: [Download from Google Drive](https://drive.google.com/file/d/1ISFbAXxadMrt7Zl96rmzzZmEKZnyW7FS/view?usp=sharing)
- 📦 **Zipped Version (~10MB)**: [Download from Google Drive](https://drive.google.com/file/d/14ceBCLQ-BTcydDrFJauVA_PKAZ7VtDor/view?usp=sharing)

You can use either version depending on your bandwidth or storage preference.

---

## 📊 Output Files

- `outputs/wallet_scores.csv` – Wallets with computed credit scores  
- `outputs/score_distribution.png` – Histogram of wallet scores

### 📷 Sample Score Distribution

![Wallet Score Distribution](outputs/score_distribution.png)
---

## 📈 Insights from Score Distribution

The credit score distribution is **right-skewed**, with:

- A large number of wallets scoring **below 100**, indicating poor recency or minimal activity.
- A moderate number scoring between **100–400**.
- Few wallets show consistently healthy behavior to score above **400**.

This is typical in DeFi where many addresses are:

- Inactive or one-time users  
- Bots or airdrop hunters  
- Test or throwaway wallets

---

## 🚀 Getting Started

### 📥 Clone the Repo

```bash
git clone https://github.com/AN-06/wallet-credit-score.git
cd wallet-credit-score
```
### 🔧 Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the Scoring
```bash
   python score_wallets.py
```
### 🧰 Project Structure

```bash
wallet-credit-score/
├── data/                      # Input JSON (NOT uploaded)
├── outputs/                   # Credit scores and plots
├── src/
│   ├── preprocess.py          # Parses raw JSON data
│   ├── feature_engineering.py # Aggregates wallet features
│   └── scoring.py             # Credit score calculation
├── score_wallets.py           # Main driver script
├── README.md                  # 📄 This file
└── analysis.md                # 📊 Score analysis report
```

### 🛠️ Requirements
   Python 3.7 or higher

  #### Required Libraries
  - pandas
  - matplotlib
  - seaborn
  
  Install them manually using:
 ```bash
     pip install pandas matplotlib seaborn
   ```

### 📚 Use Cases
- 🏦 Filter high-trust wallets for lending protocols
- 🧪 Study user behavior and protocol engagement
- ⚠️ Detect risky, inactive, or spammy wallets
- 🎯 Build credit delegation or trust-based access layers

---
