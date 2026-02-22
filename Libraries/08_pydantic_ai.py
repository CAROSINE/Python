# ============================================================
# 🏗️ 8. Pydantic-AI - Type-Safe AI Agent Framework
# ============================================================
# Install: pip install pydantic-ai
#
# কী করে? AI দিয়ে কাজ করার সময় data সবসময় correct
# format এ আসে তা নিশ্চিত করে। AI এর output কে
# structured Python objects এ convert করে।
#
# কে বানিয়েছে? Pydantic Team (Samuel Colvin) - Open Source
# ============================================================

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic import BaseModel
from typing import Optional
import os

# -------------------------------------------------------
# PART 1: সহজ Agent - সরাসরি কথা বলা
# -------------------------------------------------------

# Simple text agent বানাও
# (API key environment variable থেকে নেবে)
# os.environ["OPENAI_API_KEY"] = "your-key-here"

simple_agent = Agent(
    'openai:gpt-4o-mini',           # কোন AI model ব্যবহার করবে
    system_prompt='তুমি একজন helpful Bangla assistant।'
)

# এভাবে ব্যবহার করো:
# result = simple_agent.run_sync("বাংলাদেশের রাজধানী কী?")
# print(result.data)

# -------------------------------------------------------
# PART 2: Structured Output - AI থেকে structured data পাওয়া
# -------------------------------------------------------

# Pydantic model দিয়ে বলো AI কী return করবে
class PersonInfo(BaseModel):
    """একজন ব্যক্তির তথ্য"""
    name: str
    age: Optional[int] = None
    city: str
    profession: str
    skills: list[str]

# এই agent সবসময় PersonInfo format এ data দেবে
person_agent = Agent(
    'openai:gpt-4o-mini',
    result_type=PersonInfo,    # ← এটাই magic! output সবসময় PersonInfo হবে
    system_prompt="""
    তুমি একজন HR assistant। Text থেকে person এর তথ্য extract করো।
    সবসময় সঠিক format এ data দাও।
    """
)

# এভাবে ব্যবহার করো:
# result = person_agent.run_sync(
#     "Rahim is a 28-year-old Software Engineer from Dhaka. He knows Python, Django, and React."
# )
# person = result.data  # এটা PersonInfo object হবে
# print(f"Name: {person.name}")
# print(f"Skills: {person.skills}")

# -------------------------------------------------------
# PART 3: Job Analysis - Pydantic AI এর real use case
# -------------------------------------------------------

class JobAnalysis(BaseModel):
    """Job posting থেকে বের করা তথ্য"""
    job_title: str
    company: str
    required_skills: list[str]
    experience_years: Optional[int] = None
    salary_range: Optional[str] = None
    is_remote: bool
    location: str

job_agent = Agent(
    'openai:gpt-4o-mini',
    result_type=JobAnalysis,
    system_prompt="Extract job information from job postings accurately."
)

# Sample job posting text
job_posting = """
Senior Python Developer at TechCorp Bangladesh
Location: Dhaka (Remote friendly)
Experience: 3-5 years required

We are looking for a Python Developer who knows:
- Django and FastAPI
- PostgreSQL and Redis
- Docker and AWS

Salary: BDT 80,000 - 120,000/month
Send CV to hr@techcorp.bd
"""

# এভাবে analyze করো:
# result = job_agent.run_sync(job_posting)
# job = result.data  # JobAnalysis object
# print(f"Title: {job.job_title}")
# print(f"Skills needed: {job.required_skills}")

# -------------------------------------------------------
# PART 4: Agent এ Tools যোগ করা
# -------------------------------------------------------

# Tools যোগ করতে পারো
@simple_agent.tool_plain
def get_current_time() -> str:
    """বর্তমান সময় দাও"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@simple_agent.tool_plain  
def calculate(expression: str) -> float:
    """Simple math calculation করো"""
    # ⚠️ বাস্তবে eval() unsafe, শুধু example এর জন্য
    allowed = set('0123456789+-*/.(). ')
    if all(c in allowed for c in expression):
        return eval(expression)
    return 0.0

# -------------------------------------------------------
# PART 5: Pydantic BaseModel - Data Validation দেখাই
# -------------------------------------------------------
print("=== Pydantic Data Validation (AI ছাড়া) ===")

class Product(BaseModel):
    name: str
    price: float
    quantity: int
    category: str

# Correct data
product1 = Product(
    name="Laptop",
    price=75000.0,
    quantity=10,
    category="Electronics"
)
print(f"✅ Product: {product1.name}, Price: {product1.price}")

# Pydantic automatically converts types
product2 = Product(
    name="Mouse",
    price="1500",   # string হলেও float এ convert হয়
    quantity="5",   # string হলেও int এ convert হয়
    category="Accessories"
)
print(f"✅ Auto-converted: price={product2.price} (type: {type(product2.price).__name__})")

# Wrong data → Error দেবে
try:
    bad_product = Product(
        name="Book",
        price="not-a-price",  # এটা number না!
        quantity=5,
        category="Education"
    )
except Exception as e:
    print(f"❌ Validation Error caught: {type(e).__name__}")

# -------------------------------------------------------
# PART 6: Pydantic-AI এর সুবিধা
# -------------------------------------------------------
print("\n=== Pydantic-AI এর সুবিধা ===")
benefits = {
    "Type Safety": "AI এর output সবসময় correct type এ আসে",
    "Validation": "Wrong data automatically reject হয়",
    "IDE Support": "Autocomplete ও type hints পাওয়া যায়",
    "Multiple Models": "OpenAI, Claude, Gemini সব support করে",
    "Tools": "Custom tools যোগ করা যায়",
    "Structured Output": "JSON/dict এর বদলে Python objects পাওয়া যায়",
}
for benefit, description in benefits.items():
    print(f"✅ {benefit}: {description}")

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# Pydantic-AI = Type-safe AI Agent framework
# result_type=MyClass → AI এর output সবসময় ঐ class এ আসবে
# @agent.tool → AI যে functions ব্যবহার করতে পারবে
# Pydantic validate করে → wrong data থেকে রক্ষা করে
# OpenAI, Claude, Gemini সব দিয়ে কাজ করে
# -------------------------------------------------------
