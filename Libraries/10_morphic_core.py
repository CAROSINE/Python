# ============================================================
# 🔮 10. Morphic Core - AI-Powered Search & Answer Engine
# ============================================================
# Install: (Web-based tool, Python client available)
# GitHub: https://github.com/miurla/morphic
#
# কী করে? AI-powered search engine যে web search করে
# সুন্দর structured answer দেয়। Next.js দিয়ে বানানো
# full-stack AI search app। Perplexity AI এর মতো।
#
# কে বানিয়েছে? Miurla (Open Source)
# ============================================================

# ⚠️ Morphic মূলত একটা Next.js Web Application।
# pip install করা হয় না — clone করে run করতে হয়।
# তবে এর concept (AI Search + Answer) দেখাচ্ছি।
 
print("=== Morphic কী? ===")
print("Morphic = Open Source Perplexity AI Alternative")
print("Web search করে + AI দিয়ে answer তৈরি করে")
print("তোমার নিজের server এ deploy করতে পারো!")

# -------------------------------------------------------
# কিভাবে setup করবে:
# -------------------------------------------------------
print("\n=== Setup করার উপায় ===")
setup_steps = [
    "git clone https://github.com/miurla/morphic",
    "cd morphic",
    "npm install",
    ".env ফাইলে API keys দাও (OpenAI, Tavily Search)",
    "npm run dev",
    "http://localhost:3000 এ দেখো!"
]
for i, step in enumerate(setup_steps, 1):
    print(f"Step {i}: {step}")

# -------------------------------------------------------
# PART 1: Morphic এর পেছনে যে concept কাজ করে
# -------------------------------------------------------
# Morphic internally এই ধরনের কাজ করে:
# 1. User এর question নেয়
# 2. Web search API (Tavily/Serper) দিয়ে search করে
# 3. Search results AI কে দেয়
# 4. AI সুন্দর answer লেখে citations সহ

# Python দিয়ে similar concept:
import os
import json

def morphic_like_search(question: str, search_results: list) -> dict:
    """
    Morphic এর মতো AI-powered answer তৈরির simulation
    (বাস্তবে Tavily API + OpenAI ব্যবহার হয়)
    """
    # Simulate করা search results
    formatted_results = "\n".join([
        f"Source {i+1}: {result['title']}\n{result['snippet']}"
        for i, result in enumerate(search_results)
    ])
    
    return {
        "question": question,
        "sources": search_results,
        "formatted_context": formatted_results,
        "prompt_for_ai": f"""
        Based on the following search results, answer this question:
        Question: {question}
        
        Search Results:
        {formatted_results}
        
        Provide a comprehensive answer with citations [1], [2], etc.
        """
    }

# -------------------------------------------------------
# PART 2: Simulated Example
# -------------------------------------------------------
question = "What is the best programming language for AI?"

fake_search_results = [
    {
        "title": "Python dominates AI development",
        "url": "https://example.com/python-ai",
        "snippet": "Python is the most popular language for AI due to its extensive libraries like TensorFlow, PyTorch, and scikit-learn."
    },
    {
        "title": "Rust growing in AI space",
        "url": "https://example.com/rust-ai",
        "snippet": "Rust is gaining popularity for AI infrastructure due to its performance and safety guarantees."
    },
    {
        "title": "Julia for scientific computing",
        "url": "https://example.com/julia-ai",
        "snippet": "Julia offers high performance for numerical computing and is used in scientific AI research."
    }
]

result = morphic_like_search(question, fake_search_results)
print("\n=== Morphic-like Search Result ===")
print(f"Question: {result['question']}")
print(f"\nSources found: {len(result['sources'])}")
for i, source in enumerate(result['sources'], 1):
    print(f"  [{i}] {source['title']}")

print(f"\nAI Prompt prepared: {len(result['prompt_for_ai'])} chars")

# -------------------------------------------------------
# PART 3: Morphic এর Features
# -------------------------------------------------------
print("\n=== Morphic এর Main Features ===")
features = {
    "AI Search": "Question করো → Web search করে → AI answer দেয়",
    "Citations": "সব answer এ source link দেওয়া থাকে",
    "Streaming": "Answer টাইপ হতে হতে দেখা যায়",
    "History": "Previous searches save থাকে",
    "Share": "Search result share করা যায়",
    "Self-hosted": "নিজের server এ deploy করা যায়",
    "Open Source": "Free, নিজের মতো customize করা যায়",
}
for feature, description in features.items():
    print(f"✅ {feature}: {description}")

# -------------------------------------------------------
# PART 4: Python দিয়ে Similar Tool বানানো
# (Tavily + OpenAI দিয়ে)
# -------------------------------------------------------
print("\n=== Python দিয়ে Morphic-like Tool বানানো ===")
example_code = '''
# pip install tavily-python openai

from tavily import TavilyClient
from openai import OpenAI

tavily = TavilyClient(api_key="YOUR_TAVILY_KEY")
openai_client = OpenAI(api_key="YOUR_OPENAI_KEY")

def ai_search(question: str) -> str:
    # Step 1: Web Search
    search_results = tavily.search(query=question, max_results=3)
    
    # Step 2: Format results
    context = "\\n".join([
        f"[{i+1}] {r['title']}: {r['content']}"
        for i, r in enumerate(search_results["results"])
    ])
    
    # Step 3: AI Answer
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer based on search results."},
            {"role": "user", "content": f"Question: {question}\\n\\nContext: {context}"}
        ]
    )
    
    return response.choices[0].message.content

# ব্যবহার করো:
answer = ai_search("Bangladesh GDP 2024")
print(answer)
'''
print(example_code)

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# Morphic = Self-hosted Perplexity AI (Open Source)
# Web search করে + AI দিয়ে সুন্দর answer দেয়
# Next.js app, নিজের server এ চালাতে পারো
# Python দিয়ে similar কাজ করতে Tavily + OpenAI ব্যবহার করো
# -------------------------------------------------------
