# ============================================
# MarkItDown - File to Markdown Converter
# ============================================
# Install: pip install markitdown

from markitdown import MarkItDown

# MarkItDown object তৈরি করো
md = MarkItDown()

# --- Example 1: PDF file convert করা ---
# result = md.convert("my_document.pdf")
# print(result.text_content)

# --- Example 2: Word file (.docx) convert করা ---
# result = md.convert("my_word_file.docx")
# print(result.text_content)

# --- Example 3: Excel file convert করা ---
# result = md.convert("data.xlsx")
# print(result.text_content)

# --- Example 4: Website URL থেকে Markdown বানানো ---
result = md.convert("https://en.wikipedia.org/wiki/Python_(programming_language)")

# result.text_content এ পুরো markdown text থাকে
markdown_text = result.text_content

# প্রথম 500 character দেখাও
print("=== Converted Markdown (first 500 chars) ===")
print(markdown_text[:500])

# --- Example 5: Result একটা .md file এ save করা ---
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)

print("\n✅ File saved as output.md")

# --- Example 6: AI দিয়ে file analyze করা (OpenAI) ---
# from markitdown import MarkItDown
# from openai import OpenAI
#
# client = OpenAI()
# md = MarkItDown(llm_client=client, llm_model="gpt-4o")
#
# # Image file এর ক্ষেত্রে AI description দেবে
# result = md.convert("photo.jpg")
# print(result.text_content)
