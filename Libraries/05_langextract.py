# ============================================================
# 🔍 5. LangExtract - Google এর Text থেকে Data বের করার Library
# ============================================================
# Install: pip install langextract
#          pip install langextract[openai]   (OpenAI দিয়ে)
#
# কী করে? যেকোনো unstructured text (চিঠি, report, article)
# থেকে structured data বের করে। যেমন: paragraph থেকে
# নাম, তারিখ, ঠিকানা, medicine dose ইত্যাদি extract করে।
#
# কে বানিয়েছে? Google (Open Source)
# ============================================================

import langextract as lx
import os

# -------------------------------------------------------
# PART 1: সহজ Example - Article থেকে তথ্য বের করা
# -------------------------------------------------------

# এটা আমাদের input text (যেকোনো বাস্তব text হতে পারে)
sample_text = """
Rahim Ahmed was born on March 15, 1990 in Dhaka, Bangladesh.
He works as a Software Engineer at TechCorp, earning BDT 80,000 per month.
His email is rahim.ahmed@techcorp.com and phone number is 01712345678.
He lives at 45 Green Road, Dhanmondi, Dhaka-1205.

Karim Hassan, age 32, is a Doctor at City Hospital.
He earns BDT 120,000 monthly and lives in Chittagong.
Contact: karim.hassan@cityhospital.bd
"""

# -------------------------------------------------------
# PART 2: Example data দিয়ে LangExtract কে শেখানো
# -------------------------------------------------------
# LangExtract কে বলতে হবে "এই ধরনের তথ্য বের করো"
# তার জন্য কয়েকটা example দিতে হয়

examples = [
    lx.ExampleData(
        text="""
        John Smith, born January 5, 1985, works at Google as a Developer.
        Email: john@google.com, Salary: $5000/month.
        """,
        extractions=[
            lx.Extraction(extraction_class="name", extraction_text="John Smith"),
            lx.Extraction(extraction_class="birth_date", extraction_text="January 5, 1985"),
            lx.Extraction(extraction_class="company", extraction_text="Google"),
            lx.Extraction(extraction_class="job_title", extraction_text="Developer"),
            lx.Extraction(extraction_class="email", extraction_text="john@google.com"),
        ]
    )
]

# -------------------------------------------------------
# PART 3: Prompt দিয়ে বলো কী বের করতে চাও
# -------------------------------------------------------

prompt_description = """
Extract the following information from the text:
- Person's name (name)
- Birth date (birth_date)
- Company name (company)
- Job title (job_title)
- Email address (email)
- Monthly salary (salary)
- Location/City (location)
"""

# -------------------------------------------------------
# PART 4: Extract করো!
# (API key লাগবে - Gemini অথবা OpenAI)
# -------------------------------------------------------

# Gemini দিয়ে (Google এর):
# os.environ["LANGEXTRACT_API_KEY"] = "your-gemini-api-key"
# result = lx.extract(
#     text_or_documents=sample_text,
#     prompt_description=prompt_description,
#     examples=examples,
#     model_id="gemini-1.5-flash",
# )

# OpenAI দিয়ে:
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
# result = lx.extract(
#     text_or_documents=sample_text,
#     prompt_description=prompt_description,
#     examples=examples,
#     model_id="gpt-4o",
#     fence_output=True,
#     use_schema_constraints=False
# )

# -------------------------------------------------------
# PART 5: Result দেখা (API key থাকলে)
# -------------------------------------------------------
# extractions = result.extractions
#
# for extraction in extractions:
#     print(f"Type: {extraction.extraction_class}")
#     print(f"Value: {extraction.extraction_text}")
#     print(f"Found at position: {extraction.start_char} - {extraction.end_char}")
#     print("---")

# -------------------------------------------------------
# PART 6: Manual Simulation - API ছাড়া দেখো কিভাবে কাজ করে
# -------------------------------------------------------
import re

def simple_extractor(text):
    """API ছাড়া সহজ extraction দেখাই"""
    results = {}
    
    # Email বের করা
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    results["emails"] = emails
    
    # Phone number বের করা (Bangladeshi format)
    phone_pattern = r'01[3-9]\d{8}'
    phones = re.findall(phone_pattern, text)
    results["phones"] = phones
    
    # BDT amount বের করা
    amount_pattern = r'BDT\s[\d,]+'
    amounts = re.findall(amount_pattern, text)
    results["amounts"] = amounts
    
    return results

print("=== Simple Extraction (API ছাড়া) ===")
extracted = simple_extractor(sample_text)
for key, values in extracted.items():
    print(f"{key}: {values}")

# -------------------------------------------------------
# PART 7: বিভিন্ন use case
# -------------------------------------------------------
print("\n=== LangExtract কোথায় ব্যবহার হয়? ===")
use_cases = {
    "Medical": "Doctor এর prescription থেকে medicine, dose, frequency বের করা",
    "Legal": "Contract থেকে parties, dates, terms বের করা",
    "Finance": "Invoice থেকে amount, vendor, date বের করা",
    "HR": "CV/Resume থেকে skills, experience, education বের করা",
    "News": "Article থেকে people, events, locations বের করা",
}
for domain, use_case in use_cases.items():
    print(f"📌 {domain}: {use_case}")

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# LangExtract = AI দিয়ে text থেকে structured data বের করা
# তুমি example দাও → সে শেখে → নতুন text এ apply করে
# Every extraction-এ source text-এ exact location দেখায়
# Medical, Legal, Finance সব domain এ কাজ করে
# -------------------------------------------------------
