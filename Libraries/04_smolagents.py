# ============================================================
# 🤖 4. smolagents - HuggingFace এর AI Agent Library
# ============================================================
# Install: pip install smolagents
#
# কী করে? AI Agent তৈরি করে যে নিজে নিজে tools ব্যবহার করে
# সমস্যা সমাধান করতে পারে। যেমন: web search করা, code run
# করা, calculator ব্যবহার করা ইত্যাদি।
#
# কে বানিয়েছে? HuggingFace (Open Source)
# ============================================================

from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

# -------------------------------------------------------
# PART 1: সবচেয়ে সহজ Agent বানানো
# -------------------------------------------------------
 
# Model সেট করো (HuggingFace এর free model)
model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

# Agent বানাও যে web search করতে পারবে
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],  # Agent এর কাছে এই tools আছে
    model=model
)

# Agent কে কাজ দাও!
# result = agent.run("What is the capital of Bangladesh?")
# print(result)

# -------------------------------------------------------
# PART 2: নিজের Tool বানানো
# -------------------------------------------------------
from smolagents import tool

# @tool decorator দিয়ে যেকোনো function কে tool বানানো যায়
@tool
def calculate_bmi(weight_kg: float, height_m: float) -> str:
    """
    Calculate BMI (Body Mass Index) from weight and height.
    
    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters
    
    Returns:
        BMI value and category as a string
    """
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight (কম ওজন)"
    elif bmi < 25:
        category = "Normal (স্বাভাবিক)"
    elif bmi < 30:
        category = "Overweight (বেশি ওজন)"
    else:
        category = "Obese (স্থূলতা)"
    
    return f"BMI: {bmi:.1f} → {category}"

@tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Convert currency using approximate rates.
    
    Args:
        amount: Amount to convert
        from_currency: Currency to convert from (USD, BDT, EUR)
        to_currency: Currency to convert to (USD, BDT, EUR)
    
    Returns:
        Converted amount as string
    """
    # Approximate rates (BDT base)
    rates = {
        "USD": 110,   # 1 USD = 110 BDT (approximate)
        "EUR": 120,   # 1 EUR = 120 BDT (approximate)
        "BDT": 1,
        "GBP": 140,
    }
    
    if from_currency not in rates or to_currency not in rates:
        return "Currency not supported"
    
    # Convert to BDT first, then to target
    bdt_amount = amount * rates[from_currency]
    result = bdt_amount / rates[to_currency]
    
    return f"{amount} {from_currency} = {result:.2f} {to_currency}"

# -------------------------------------------------------
# PART 3: নিজের Tools দিয়ে Agent বানানো
# -------------------------------------------------------

# Custom tools দিয়ে agent
custom_agent = CodeAgent(
    tools=[calculate_bmi, convert_currency],
    model=model
)

# এভাবে use করবে:
# result = custom_agent.run("What is the BMI of a person who weighs 70kg and is 1.75m tall?")
# print(result)

# result = custom_agent.run("Convert 100 USD to BDT")
# print(result)

# -------------------------------------------------------
# PART 4: Tools একা একাও test করতে পারো
# -------------------------------------------------------

print("=== Tool সরাসরি test করা ===")
print(calculate_bmi(70, 1.75))
print(convert_currency(100, "USD", "BDT"))
print(convert_currency(50, "EUR", "USD"))

# -------------------------------------------------------
# PART 5: Multiple Tools সহ Powerful Agent
# -------------------------------------------------------

powerful_agent = CodeAgent(
    tools=[
        DuckDuckGoSearchTool(),   # Web search করতে পারবে
        calculate_bmi,            # BMI calculate করতে পারবে
        convert_currency,         # Currency convert করতে পারবে
    ],
    model=model,
    max_steps=5  # সর্বোচ্চ 5 step নেবে
)

# এই agent কে complex question করতে পারো:
# result = powerful_agent.run(
#     "Search for the current USD to BDT exchange rate and convert 200 USD"
# )

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# smolagents = AI Agent framework
# Agent = AI যে নিজে নিজে tools ব্যবহার করতে পারে
# @tool decorator → যেকোনো function কে tool বানাও
# CodeAgent → agent তৈরি করো tools আর model দিয়ে
# agent.run("প্রশ্ন") → agent নিজে উত্তর খোঁজে
# -------------------------------------------------------

print("\n=== smolagents সম্পর্কে মূল কথা ===")
print("1. smolagents দিয়ে AI Agent বানানো যায়")
print("2. Agent নিজে নিজে tools ব্যবহার করে সমস্যা solve করে")
print("3. @tool দিয়ে যেকোনো Python function কে tool বানানো যায়")
print("4. HuggingFace, OpenAI, Anthropic সব model support করে")
