# ============================================================
# 🐸 11. Chainfrog - AI Workflow Automation Library
# ============================================================
# Note: "Chainfrog" নামে exact library পাওয়া কঠিন।
# এটা সম্ভবত LangChain বা similar AI workflow tool এর
# variant অথবা নতুন emerging library।
# এখানে AI Workflow/Chain concept দেখাচ্ছি।
#
# AI Workflow মানে: একটার output অন্যটার input হয়
# যেমন: Text → Translate → Summarize → Email পাঠাও
# ============================================================

# -------------------------------------------------------
# AI Workflow / Chain Concept Python দিয়ে দেখাই
# -------------------------------------------------------
from typing import Callable, Any
import json

# -------------------------------------------------------
# PART 1: Simple Chain বানানো
# -------------------------------------------------------

class AIChain:
    """
    Simple AI Workflow Chain
    এক step এর output → পরের step এর input
    """
    
    def __init__(self, name: str):
        self.name = name
        self.steps = []
    
    def add_step(self, func: Callable, step_name: str = ""):
        """Chain এ নতুন step যোগ করো"""
        self.steps.append({
            "name": step_name or func.__name__,
            "func": func
        })
        return self  # Method chaining এর জন্য self return
    
    def run(self, initial_input: Any) -> Any:
        """Chain চালাও"""
        print(f"\n🐸 Starting Chain: {self.name}")
        print(f"📥 Input: {initial_input}")
        print("-" * 40)
        
        current_data = initial_input
        
        for i, step in enumerate(self.steps, 1):
            print(f"\nStep {i}: {step['name']}")
            current_data = step["func"](current_data)
            print(f"  Output: {current_data}")
        
        print("\n" + "=" * 40)
        print(f"✅ Chain Complete!")
        print(f"📤 Final Output: {current_data}")
        return current_data

# -------------------------------------------------------
# PART 2: Real Example - Text Processing Chain
# -------------------------------------------------------

# Step functions বানাই
def clean_text(text: str) -> str:
    """Text পরিষ্কার করো"""
    return text.strip().lower()

def count_words(text: str) -> dict:
    """শব্দ count করো"""
    words = text.split()
    return {
        "original_text": text,
        "word_count": len(words),
        "words": words
    }

def find_long_words(data: dict) -> dict:
    """5+ letter এর words বের করো"""
    long_words = [w for w in data["words"] if len(w) >= 5]
    data["long_words"] = long_words
    data["long_word_count"] = len(long_words)
    return data

def create_report(data: dict) -> str:
    """Report বানাও"""
    return f"""
📊 Text Analysis Report
-----------------------
Total Words: {data['word_count']}
Long Words (5+ letters): {data['long_word_count']}
Long Words Found: {', '.join(data['long_words'])}
    """.strip()

# Chain তৈরি করো
text_chain = AIChain("Text Analysis Chain")
text_chain.add_step(clean_text, "Clean Text")
text_chain.add_step(count_words, "Count Words")
text_chain.add_step(find_long_words, "Find Long Words")
text_chain.add_step(create_report, "Create Report")

# Run করো!
sample_text = "  Python programming language is very popular for artificial intelligence  "
final_report = text_chain.run(sample_text)

# -------------------------------------------------------
# PART 3: Data Processing Chain
# -------------------------------------------------------

def load_sales_data(data: list) -> list:
    """Sales data load করো"""
    return [{"product": item[0], "amount": item[1], "region": item[2]} 
            for item in data]

def filter_high_sales(data: list) -> list:
    """50000 এর বেশি sales filter করো"""
    return [item for item in data if item["amount"] > 50000]

def calculate_totals(data: list) -> dict:
    """Total calculate করো"""
    total = sum(item["amount"] for item in data)
    return {
        "filtered_data": data,
        "total_high_sales": total,
        "count": len(data)
    }

def format_output(data: dict) -> str:
    """সুন্দর করে দেখাও"""
    lines = ["📈 High Sales Report (>50,000):", "-" * 30]
    for item in data["filtered_data"]:
        lines.append(f"  {item['product']}: ৳{item['amount']:,} ({item['region']})")
    lines.append("-" * 30)
    lines.append(f"Total: ৳{data['total_high_sales']:,}")
    lines.append(f"Count: {data['count']} products")
    return "\n".join(lines)

# Raw sales data
raw_data = [
    ("Laptop", 75000, "Dhaka"),
    ("Mouse", 1500, "Chittagong"),
    ("Monitor", 55000, "Dhaka"),
    ("Keyboard", 3000, "Sylhet"),
    ("Headphone", 8000, "Rajshahi"),
    ("Printer", 65000, "Dhaka"),
]

# Sales chain বানাও
sales_chain = AIChain("Sales Analysis Chain")
sales_chain.add_step(load_sales_data, "Load Data")
sales_chain.add_step(filter_high_sales, "Filter High Sales")
sales_chain.add_step(calculate_totals, "Calculate Totals")
sales_chain.add_step(format_output, "Format Output")

result = sales_chain.run(raw_data)

# -------------------------------------------------------
# PART 4: Conditional Chain (Branch করা)
# -------------------------------------------------------

class SmartChain(AIChain):
    """Branch করতে পারে এমন chain"""
    
    def add_conditional_step(self, condition: Callable, 
                              if_true: Callable, 
                              if_false: Callable):
        """শর্তের উপর নির্ভর করে আলাদা step চালাও"""
        def conditional_func(data):
            if condition(data):
                print(f"  → Condition TRUE: running {if_true.__name__}")
                return if_true(data)
            else:
                print(f"  → Condition FALSE: running {if_false.__name__}")
                return if_false(data)
        
        self.steps.append({
            "name": f"Conditional ({if_true.__name__} / {if_false.__name__})",
            "func": conditional_func
        })
        return self

def is_high_score(score: int) -> bool:
    return score >= 70

def send_promotion_email(score: int) -> str:
    return f"🎉 Congratulations! Score {score}/100 → Promoted!"

def send_improvement_email(score: int) -> str:
    return f"📚 Keep studying! Score {score}/100 → More practice needed."

smart_chain = SmartChain("Student Evaluation Chain")
smart_chain.add_conditional_step(is_high_score, send_promotion_email, send_improvement_email)

print(smart_chain.run(85))
print(smart_chain.run(45))

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# AI Workflow/Chain = একের পর এক step এ কাজ করা
# এক step এর output → পরের step এর input হয়
# Text processing, data analysis, AI pipelines এ ব্যবহার হয়
# LangChain এই concept এর সবচেয়ে popular implementation
# -------------------------------------------------------
