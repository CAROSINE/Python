# ============================================================
# 🔒 12. MOSTLY AI - Privacy-Safe Synthetic Data Generator
# ============================================================
# Install: pip install mostlyai
# Full install: pip install 'mostlyai[local]'
#
# কী করে? Real data থেকে Synthetic (নকল কিন্তু realistic)
# data তৈরি করে যা privacy-safe। Machine learning এর জন্য
# unlimited fake data তৈরি করা যায়।
#
# কে বানিয়েছে? MOSTLY AI (Commercial + Open Source SDK)
# ============================================================

from mostlyai.sdk import MostlyAI
import pandas as pd
 
# -------------------------------------------------------
# PART 1: Synthetic Data কী এবং কেন দরকার?
# -------------------------------------------------------
print("=== Synthetic Data কী? ===")
print("""
🔴 Real Data এর সমস্যা:
   - Privacy risk (মানুষের personal data)
   - GDPR/PDPA আইনে share করা যায় না
   - কম data থাকলে ML model ভালো হয় না

🟢 Synthetic Data সমাধান:
   - Real data এর pattern শিখে fake data বানায়
   - Privacy নেই কারণ real মানুষের data না
   - যত খুশি তত data তৈরি করা যায়
   - ML training এর জন্য perfect
""")

# -------------------------------------------------------
# PART 2: Sample Real Data (যা থেকে synthetic তৈরি হবে)
# -------------------------------------------------------

# ধরো এটা তোমার company র customer data
# (এই data real না, শুধু example)
original_data = pd.DataFrame({
    "customer_id": range(1, 11),
    "name": ["Rahim", "Karim", "Sadia", "Mitu", "Jamal",
             "Fatima", "Abdul", "Nasrin", "Rafiq", "Sumaiya"],
    "age": [25, 32, 28, 45, 38, 29, 52, 34, 41, 27],
    "city": ["Dhaka", "Chittagong", "Dhaka", "Sylhet", "Dhaka",
             "Rajshahi", "Dhaka", "Khulna", "Chittagong", "Dhaka"],
    "monthly_income": [45000, 80000, 35000, 120000, 65000,
                       42000, 150000, 55000, 90000, 38000],
    "loan_approved": [True, True, False, True, True,
                      False, True, True, True, False],
    "credit_score": [720, 800, 580, 850, 750,
                     620, 900, 780, 820, 600],
})

print("=== Original Data (10 records) ===")
print(original_data)
print(f"\nShape: {original_data.shape}")

# -------------------------------------------------------
# PART 3: MOSTLY AI দিয়ে Synthetic Data বানানো
# -------------------------------------------------------

# LOCAL mode (নিজের computer এ):
print("\n=== Synthetic Data তৈরি করা ===")

# SDK initialize করো (local mode)
mostly = MostlyAI(local=True)

# Generator train করো (real data থেকে শেখে)
print("Step 1: Generator training...")
# g = mostly.train(
#     config={
#         'name': 'Customer Data Generator',
#         'tables': [{
#             'name': 'customers',
#             'data': original_data,
#             'tabular_model_configuration': {
#                 'max_training_time': 2,  # 2 minutes এ train শেষ
#             }
#         }]
#     }
# )
# print("Generator trained! ✅")

# Synthetic data generate করো
print("Step 2: Generating synthetic data...")
# synthetic_data = mostly.probe(g, size=1000)  # 1000 synthetic records
# print(f"Generated {len(synthetic_data)} synthetic records!")

# -------------------------------------------------------
# PART 4: Manual Simulation (SDK ছাড়া concept দেখাই)
# -------------------------------------------------------
import random
import numpy as np

def generate_synthetic_customers(original_df: pd.DataFrame, n: int) -> pd.DataFrame:
    """
    Original data এর pattern শিখে synthetic data তৈরি করে
    (Simplified simulation - বাস্তবে MOSTLY AI অনেক বেশি sophisticated)
    """
    # Original data থেকে statistics বের করো
    age_mean = original_df["age"].mean()
    age_std = original_df["age"].std()
    
    income_mean = original_df["monthly_income"].mean()
    income_std = original_df["monthly_income"].std()
    
    approval_rate = original_df["loan_approved"].mean()
    
    credit_mean = original_df["credit_score"].mean()
    credit_std = original_df["credit_score"].std()
    
    cities = original_df["city"].value_counts(normalize=True)
    
    # Synthetic records তৈরি করো
    bangla_names = [
        "Mehedi", "Tanvir", "Nusrat", "Rakib", "Sharmin",
        "Imran", "Tasnim", "Farhan", "Roksana", "Jubair",
        "Anika", "Sabbir", "Morshed", "Dilruba", "Hasnat"
    ]
    
    synthetic = {
        "customer_id": range(n+1, n+n+1),
        "name": [random.choice(bangla_names) + f" {i}" for i in range(n)],
        "age": np.clip(np.random.normal(age_mean, age_std, n).astype(int), 18, 70),
        "city": np.random.choice(cities.index, n, p=cities.values),
        "monthly_income": np.clip(
            np.random.normal(income_mean, income_std, n).astype(int), 
            15000, 500000
        ),
        "loan_approved": np.random.binomial(1, approval_rate, n).astype(bool),
        "credit_score": np.clip(
            np.random.normal(credit_mean, credit_std, n).astype(int),
            300, 900
        ),
    }
    
    return pd.DataFrame(synthetic)

print("\n=== Simulated Synthetic Data (20 records) ===")
synthetic_df = generate_synthetic_customers(original_data, 20)
print(synthetic_df.head(10))

# -------------------------------------------------------
# PART 5: Original vs Synthetic তুলনা
# -------------------------------------------------------
print("\n=== Original vs Synthetic Statistics ===")
print("\nAge:")
print(f"  Original  → Mean: {original_data['age'].mean():.1f}, Std: {original_data['age'].std():.1f}")
print(f"  Synthetic → Mean: {synthetic_df['age'].mean():.1f}, Std: {synthetic_df['age'].std():.1f}")

print("\nMonthly Income:")
print(f"  Original  → Mean: ৳{original_data['monthly_income'].mean():,.0f}")
print(f"  Synthetic → Mean: ৳{synthetic_df['monthly_income'].mean():,.0f}")

print("\nLoan Approval Rate:")
print(f"  Original  → {original_data['loan_approved'].mean():.1%}")
print(f"  Synthetic → {synthetic_df['loan_approved'].mean():.1%}")

print("\nCity Distribution:")
print("  Original:")
for city, count in original_data["city"].value_counts().items():
    print(f"    {city}: {count}")

# -------------------------------------------------------
# PART 6: Synthetic Data এর Use Cases
# -------------------------------------------------------
print("\n=== MOSTLY AI কোথায় ব্যবহার হয়? ===")
use_cases = {
    "ML Training": "বেশি data দরকার? Synthetic data দিয়ে ML model train করো",
    "Testing": "Software testing এ real user data ব্যাবহারের বদলে",
    "Data Sharing": "Research বা partner দের privacy-safe data share করো",
    "GDPR Compliance": "আইন মেনে AI develop করো",
    "Rare Events": "Fraud বা rare medical cases এর বেশি example তৈরি করো",
    "Banking": "Transaction data থেকে synthetic financial data",
    "Healthcare": "Patient data থেকে privacy-safe training data",
}
for use_case, description in use_cases.items():
    print(f"📌 {use_case}: {description}")

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# MOSTLY AI = Real data → Fake কিন্তু Realistic Data তৈরি
# Privacy-safe: কোনো real মানুষের data থাকে না
# ML এর জন্য unlimited training data পাওয়া যায়
# mostly.train(data) → generator শেখে
# mostly.probe(generator, size=1000) → 1000 synthetic records
# -------------------------------------------------------
