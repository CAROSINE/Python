# ============================================================
# 📄 1. MarkItDown - Microsoft এর File to Markdown Converter
# ============================================================
# Install: pip install markitdown
#
# কী করে? PDF, Word, Excel, PowerPoint, Image, URL যেকোনো
# কিছুকে Markdown text-এ convert করে।
# কে বানিয়েছে? Microsoft
# ============================================================

from markitdown import MarkItDown

# Step 1: MarkItDown object তৈরি করো
md = MarkItDown()

# -------------------------------------------------------
# Example 1: সাধারণ text file convert করা
# -------------------------------------------------------
# result = md.convert("my_document.pdf")
# print(result.text_content)

# -------------------------------------------------------
# Example 2: Word file (.docx) convert করা
# -------------------------------------------------------
# result = md.convert("report.docx")
# print(result.text_content)

# -------------------------------------------------------
# Example 3: Excel file convert করা
# -------------------------------------------------------
# result = md.convert("data.xlsx")
# print(result.text_content)

# -------------------------------------------------------
# Example 4: Website URL থেকে Markdown বানানো (চলবে)
# -------------------------------------------------------
result = md.convert("https://en.wikipedia.org/wiki/Python_(programming_language)")

# result.text_content এ পুরো markdown text থাকে
markdown_text = result.text_content

# প্রথম 300 character print করো
print("=== Wikipedia থেকে Markdown (প্রথম 300 character) ===")
print(markdown_text[:300])

# -------------------------------------------------------
# Example 5: Result একটা .md file এ save করা
# -------------------------------------------------------
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)

print("\n✅ output.md file এ save হয়ে গেছে!")

# -------------------------------------------------------
# Example 6: AI দিয়ে Image describe করা (OpenAI লাগবে)
# -------------------------------------------------------
# from openai import OpenAI
# client = OpenAI()
# md = MarkItDown(llm_client=client, llm_model="gpt-4o")
# result = md.convert("photo.jpg")  # Image এর description দেবে
# print(result.text_content)

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# md.convert("যেকোনো file বা URL") → result
# result.text_content → Markdown text পাবে
# -------------------------------------------------------
