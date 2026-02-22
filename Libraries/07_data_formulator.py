# ============================================================
# 📊 7. Data Formulator - Microsoft এর AI Data Visualization Tool
# ============================================================
# Install: pip install data_formulator
# Run:     python -m data_formulator
#
# কী করে? Data (CSV, Excel) দাও এবং natural language এ বলো
# "show me sales by month" → সে নিজেই chart বানিয়ে দেবে।
# AI দিয়ে data transform করে এবং visualization তৈরি করে।
#
# কে বানিয়েছে? Microsoft Research (Open Source)
# ============================================================
 
# ⚠️ Data Formulator মূলত একটা Web App।
# pip install করে browser এ open হয়।
# Python code দিয়ে directly chart বানানোর library না।
# তবে এর concept বোঝাতে নিচে similar code দেখাচ্ছি।

# -------------------------------------------------------
# Data Formulator কিভাবে start করবে:
# -------------------------------------------------------
print("=== Data Formulator Start করার উপায় ===")
print("Step 1: pip install data_formulator")
print("Step 2: python -m data_formulator")
print("Step 3: Browser এ http://localhost:5000 open হবে")
print("Step 4: CSV/Excel file upload করো")
print("Step 5: Natural language এ বলো কী chart দেখতে চাও")
print("Step 6: AI নিজেই chart বানাবে!")

# -------------------------------------------------------
# PART 1: Data Formulator যা করে তার simulation
# (Pandas + Matplotlib দিয়ে দেখাচ্ছি concept)
# -------------------------------------------------------
import pandas as pd
import json

# Sample Sales Data (যেমন CSV upload করবে)
sales_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [45000, 52000, 48000, 61000, 55000, 70000,
              65000, 72000, 68000, 80000, 75000, 90000],
    "Region": ["North", "North", "South", "South", "East", "East",
                "West", "West", "North", "South", "East", "West"],
    "Product": ["A", "B", "A", "B", "A", "B",
                "A", "B", "A", "B", "A", "B"],
})

print("\n=== Sample Sales Data ===")
print(sales_data.head())

# -------------------------------------------------------
# PART 2: Data Formulator-এ যা বলা যায় (Natural Language)
# -------------------------------------------------------
natural_language_prompts = [
    "Show me total sales by month as a bar chart",
    "Which region has the highest sales? Show as pie chart",
    "Compare Product A and B sales over the year",
    "Show the trend of sales from Jan to Dec",
    "Find months where sales exceeded 65000",
    "Calculate average sales per region",
    "Show top 3 months by sales",
]

print("\n=== Data Formulator কে এই ধরনের কথা বলা যায় ===")
for i, prompt in enumerate(natural_language_prompts, 1):
    print(f"{i}. {prompt}")

# -------------------------------------------------------
# PART 3: Data Formulator যা করে - Manual Simulation
# -------------------------------------------------------
print("\n=== Data Formulator এর পেছনে যা হয় ===")

# AI নিজেই এই ধরনের code generate করে:
print("\n--- 'Show total sales by month' বললে AI এই code চালায়: ---")
monthly_sales_code = """
import pandas as pd
import altair as alt

# Data transform (AI করে)
chart_data = sales_data.groupby('Month')['Sales'].sum().reset_index()

# Chart বানানো (AI করে)  
chart = alt.Chart(chart_data).mark_bar().encode(
    x='Month',
    y='Sales',
    color='Sales:Q'
).properties(title='Monthly Sales')
"""
print(monthly_sales_code)

# -------------------------------------------------------
# PART 4: Actual Data Analysis (Data Formulator ছাড়াই)
# -------------------------------------------------------
print("=== Data Analysis Results ===")

# Monthly total
print("\nMonthly Sales:")
print(sales_data[["Month", "Sales"]].to_string(index=False))

# Region summary
print("\nSales by Region:")
region_summary = sales_data.groupby("Region")["Sales"].agg(["sum", "mean"])
region_summary.columns = ["Total", "Average"]
print(region_summary)

# Top 3 months
print("\nTop 3 Months:")
top3 = sales_data.nlargest(3, "Sales")[["Month", "Sales"]]
print(top3.to_string(index=False))

# -------------------------------------------------------
# PART 5: Data Formulator এর Features Summary
# -------------------------------------------------------
print("\n=== Data Formulator Features ===")
features = {
    "Natural Language": "বাংলা বা English এ বলো কী chart দেখতে চাও",
    "Drag & Drop": "Column গুলো drag করে chart design করো",
    "AI Transform": "AI নিজেই data process করে",
    "Code Inspect": "AI যা code লেখে তা দেখতে পারো",
    "Multiple Charts": "একসাথে অনেক chart বানাতে পারো",
    "Live Data": "Live database থেকেও data টানতে পারে",
    "Export": "Charts export করা যায়",
}
for feature, description in features.items():
    print(f"✅ {feature}: {description}")

print("\n=== Supported Data Sources ===")
sources = ["CSV files", "Excel (XLSX)", "Screenshots", "Plain text",
           "MySQL database", "PostgreSQL", "Google BigQuery", "URLs"]
for source in sources:
    print(f"  📂 {source}")

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# Data Formulator = AI-powered Data Visualization Tool
# pip install → browser open → CSV upload → chat করো
# Natural language এ chart চাইলে AI নিজেই বানিয়ে দেবে
# Microsoft Research বানিয়েছে, GPT-4o/Claude দিয়ে কাজ করে
# -------------------------------------------------------
