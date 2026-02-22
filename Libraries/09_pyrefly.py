# ============================================================
# 🦋 9. Pyrefly - Meta এর Python Type Checker (Ultra Fast!)
# ============================================================
# Install: pip install pyrefly
# VSCode Extension: "Pyrefly" marketplace থেকে
#
# কী করে? Python code এ type errors খুঁজে বের করে —
# code run করার আগেই! Rust দিয়ে বানানো, তাই অনেক fast।
# 1.8 million lines of code per second check করতে পারে।
#
# কে বানিয়েছে? Meta (Instagram এ ব্যবহার হয়) - Open Source
# ============================================================

# ⚠️ Pyrefly একটা CLI tool এবং VSCode Extension।
# Python code এ import করে ব্যবহার করার library না।
# তবে এর concept (Type Hints) বোঝাতে code দেখাচ্ছি।

# -------------------------------------------------------
# Terminal এ কিভাবে ব্যবহার করবে:
# -------------------------------------------------------
print("=== Pyrefly ব্যবহার করার উপায় ===")
print("1. pip install pyrefly")
print("2. pyrefly check your_file.py   → একটা file check")
print("3. pyrefly check .              → পুরো folder check")
print("4. VSCode Extension install করো → typing করার সময়ই error দেখাবে")

# -------------------------------------------------------
# PART 1: Type Hints ছাড়া code (Pyrefly কিছু ধরবে না)
# -------------------------------------------------------
def add_without_types(a, b):
    return a + b

# এটা চলবে কিন্তু ভুল হতে পারে:
result1 = add_without_types(5, 3)       # সঠিক: 8
result2 = add_without_types("5", "3")  # ভুল হতে পারে কিন্তু error নেই
print(f"\nType ছাড়া: {result1}, {result2}")

# -------------------------------------------------------
# PART 2: Type Hints সহ code (Pyrefly check করবে)
# -------------------------------------------------------
def add_with_types(a: int, b: int) -> int:
    """দুটো integer যোগ করো"""
    return a + b

def greet(name: str, times: int = 1) -> str:
    """কাউকে greet করো"""
    return f"Hello, {name}! " * times

def calculate_discount(price: float, discount_percent: float) -> float:
    """Discount calculate করো"""
    return price * (1 - discount_percent / 100)

print("\n=== Type-safe Functions ===")
print(add_with_types(5, 3))
print(greet("Rahim"))
print(greet("Karim", 2))
print(f"Price after discount: {calculate_discount(1000, 20)}")

# -------------------------------------------------------
# PART 3: Pyrefly যেসব Error ধরে (Examples)
# -------------------------------------------------------
print("\n=== Pyrefly যেসব Error ধরতে পারে ===")

# Error Type 1: Wrong type দেওয়া
def multiply(a: int, b: int) -> int:
    return a * b

# multiply("hello", 3)  # ← Pyrefly এটাকে ERROR বলবে!
# কারণ: "hello" is str, কিন্তু int চাওয়া হয়েছে

# Error Type 2: None হতে পারে এমন value ব্যবহার
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Rahim", 2: "Karim"}
    return users.get(user_id)  # None হতে পারে

user = find_user(999)
# user.upper()  # ← Pyrefly বলবে: user can be None!

# সঠিক উপায়:
if user is not None:
    print(f"User found: {user.upper()}")
else:
    print("User not found")

# Error Type 3: Return type mismatch
def get_age() -> int:
    return 25  # সঠিক: int

# def get_name() -> int:
#     return "Rahim"  # ← Pyrefly বলবে: str কিন্তু int দরকার!

# -------------------------------------------------------
# PART 4: Class এ Type Hints
# -------------------------------------------------------
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    name: str
    age: int
    grades: List[float]
    is_active: bool = True
    
    def average_grade(self) -> float:
        """Average grade calculate করো"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def promote(self) -> str:
        avg = self.average_grade()
        if avg >= 60:
            return f"{self.name} promoted! (Average: {avg:.1f})"
        else:
            return f"{self.name} needs improvement. (Average: {avg:.1f})"

print("\n=== Type-safe Class Example ===")
student1 = Student("Rahim", 20, [75.0, 80.0, 90.0, 85.0])
student2 = Student("Karim", 21, [45.0, 50.0, 40.0, 55.0])

print(student1.promote())
print(student2.promote())

# -------------------------------------------------------
# PART 5: Pyrefly vs অন্য Type Checkers
# -------------------------------------------------------
print("\n=== Pyrefly vs অন্যদের তুলনা ===")
comparison = {
    "Pyrefly (Meta)": "🚀 Fastest, 1.8M lines/sec, IDE-first, Rust দিয়ে",
    "MyPy (Python)":  "🐌 Original, slow, widely used",
    "Pyright (MS)":   "⚡ Fast, VS Code এ ব্যবহার হয়",
    "Ty (Astral)":    "🦀 New, also Rust, uv-এর team বানিয়েছে",
}
for tool, description in comparison.items():
    print(f"  {tool}: {description}")

# -------------------------------------------------------
# PART 6: Pyrefly কনফিগ করা
# -------------------------------------------------------
print("\n=== pyrefly.toml configuration (উদাহরণ) ===")
config_example = """
# pyrefly.toml ফাইলে এই settings দেওয়া যায়:

[project]
include = ["src/**/*.py"]
exclude = ["tests/**"]

[check]
strict = true       # সব type check করো
python_version = "3.12"
"""
print(config_example)

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# Pyrefly = Python code এর type checker (error finder)
# Run করার আগেই বলে দেয় code এ type ভুল আছে কিনা
# Meta বানিয়েছে, Instagram এ ব্যবহার হয়
# অনেক fast (Rust দিয়ে বানানো)
# def foo(x: int) → এই ধরনের type hints লেখলে সে check করে
# -------------------------------------------------------
