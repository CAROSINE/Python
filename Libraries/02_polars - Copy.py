# ============================================================
# ⚡ 2. Polars - Fast Data Analysis Library
# ============================================================
# Install: pip install polars
#
# কী করে? Data analysis করে, Pandas-এর মতোই কিন্তু
# অনেক বেশি দ্রুত। Rust দিয়ে বানানো।
# কে বানিয়েছে? Ritchie Vink (Open Source)
# ============================================================

import polars as pl

# -------------------------------------------------------
# PART 1: DataFrame তৈরি করা
# -------------------------------------------------------
df = pl.DataFrame({
    "name":   ["Rahim", "Karim", "Sadia", "Mitu", "Jamal"],
    "age":    [25, 30, 22, 28, 35],
    "salary": [30000, 50000, 25000, 45000, 60000],
    "city":   ["Dhaka", "Chittagong", "Dhaka", "Sylhet", "Dhaka"],
    "dept":   ["IT", "HR", "IT", "Finance", "IT"]
})

print("=== পুরো DataFrame ===")
print(df)

# -------------------------------------------------------
# PART 2: Basic Info
# -------------------------------------------------------
print("\n=== Columns (কী কী আছে?) ===")
print(df.columns)

print("\n=== Shape (row, column) ===")
print(df.shape)

print("\n=== প্রথম 3 row ===")
print(df.head(3))

# -------------------------------------------------------
# PART 3: Filter - শর্ত দিয়ে row বের করা
# -------------------------------------------------------

# শুধু Dhaka-র লোকজন
dhaka = df.filter(pl.col("city") == "Dhaka")
print("\n=== Dhaka-র লোকজন ===")
print(dhaka)

# Salary 30000 এর বেশি
high_salary = df.filter(pl.col("salary") > 30000)
print("\n=== বেশি salary (>30000) ===")
print(high_salary)

# দুটো শর্ত একসাথে: Dhaka AND IT
dhaka_it = df.filter(
    (pl.col("city") == "Dhaka") & (pl.col("dept") == "IT")
)
print("\n=== Dhaka + IT Department ===")
print(dhaka_it)

# -------------------------------------------------------
# PART 4: Select - নির্দিষ্ট column নাও
# -------------------------------------------------------
name_salary = df.select(["name", "salary"])
print("\n=== শুধু Name ও Salary ===")
print(name_salary)

# -------------------------------------------------------
# PART 5: নতুন Column যোগ করা
# -------------------------------------------------------
df_bonus = df.with_columns(
    (pl.col("salary") * 0.10).alias("bonus"),
    (pl.col("salary") * 1.10).alias("total_pay")
)
print("\n=== Bonus যোগ করার পরে ===")
print(df_bonus)

# -------------------------------------------------------
# PART 6: Group By - Group করে statistics
# -------------------------------------------------------

# City অনুযায়ী average salary
city_stats = df.group_by("city").agg(
    pl.col("salary").mean().alias("avg_salary"),
    pl.col("name").count().alias("total_people")
)
print("\n=== City অনুযায়ী Average Salary ===")
print(city_stats)

# -------------------------------------------------------
# PART 7: Sort করা
# -------------------------------------------------------
sorted_df = df.sort("salary", descending=True)
print("\n=== Salary বেশি থেকে কম (Sorted) ===")
print(sorted_df)

# -------------------------------------------------------
# PART 8: CSV Read / Write
# -------------------------------------------------------
df.write_csv("employees.csv")
print("\n✅ employees.csv এ save হয়েছে")

df_loaded = pl.read_csv("employees.csv")
print("\n=== CSV থেকে Load করা ===")
print(df_loaded)

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# pl.DataFrame({}) → data তৈরি
# .filter() → row বের করো শর্ত দিয়ে
# .select() → column বেছে নাও
# .with_columns() → নতুন column বানাও
# .group_by().agg() → group করে statistics বের করো
# .sort() → সাজাও
# -------------------------------------------------------
