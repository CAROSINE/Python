# ============================================================
# 🚀 6. FastMCP - AI এর জন্য MCP Server বানানোর Tool
# ============================================================
# Install: pip install fastmcp
#
# কী করে? AI (Claude, GPT) কে custom tools দেওয়ার জন্য
# MCP Server বানায়। যেমন: Claude কে বলো "weather দেখো"
# এবং সে তোমার বানানো weather tool ব্যবহার করবে।
#
# MCP = Model Context Protocol (AI এর জন্য USB port এর মতো)
# কে বানিয়েছে? Prefect (Open Source, ১ মিলিয়ন+ downloads/day)
# ============================================================

from fastmcp import FastMCP
 
# -------------------------------------------------------
# PART 1: সবচেয়ে সহজ MCP Server বানানো
# -------------------------------------------------------

# Server তৈরি করো
mcp = FastMCP("আমার প্রথম MCP Server 🚀")

# -------------------------------------------------------
# PART 2: Tools বানানো (@mcp.tool decorator দিয়ে)
# -------------------------------------------------------
# @mcp.tool দিলে AI এই function টি ব্যবহার করতে পারবে

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """দুটো সংখ্যা যোগ করো"""
    return a + b

@mcp.tool
def greet_person(name: str, language: str = "english") -> str:
    """
    কাউকে সালাম দাও বিভিন্ন ভাষায়।
    
    Args:
        name: ব্যক্তির নাম
        language: ভাষা (english, bangla, arabic)
    """
    greetings = {
        "english": f"Hello, {name}! How are you?",
        "bangla": f"আস্সালামু আলাইকুম {name}! কেমন আছেন?",
        "arabic": f"السلام عليكم {name}!",
    }
    return greetings.get(language, f"Hello, {name}!")

@mcp.tool
def calculate_area(shape: str, dimension1: float, dimension2: float = 0) -> str:
    """
    বিভিন্ন shape এর area calculate করো।
    
    Args:
        shape: shape এর ধরন (rectangle, triangle, circle)
        dimension1: প্রথম মাপ (দৈর্ঘ্য বা radius)
        dimension2: দ্বিতীয় মাপ (প্রস্থ বা উচ্চতা)
    """
    import math
    
    if shape == "rectangle":
        area = dimension1 * dimension2
        return f"Rectangle Area: {dimension1} × {dimension2} = {area} sq units"
    elif shape == "triangle":
        area = 0.5 * dimension1 * dimension2
        return f"Triangle Area: ½ × {dimension1} × {dimension2} = {area} sq units"
    elif shape == "circle":
        area = math.pi * dimension1 ** 2
        return f"Circle Area: π × {dimension1}² = {area:.2f} sq units"
    else:
        return f"Unknown shape: {shape}"

@mcp.tool
def check_weather(city: str) -> str:
    """
    শহরের আবহাওয়া দেখাও (Mock data)।
    
    Args:
        city: শহরের নাম
    """
    # বাস্তবে এখানে weather API call হবে
    weather_data = {
        "Dhaka": "☀️ Sunny, 32°C, Humidity: 75%",
        "Chittagong": "⛅ Partly Cloudy, 30°C, Humidity: 80%",
        "Sylhet": "🌧️ Rainy, 25°C, Humidity: 90%",
        "Rajshahi": "🌤️ Clear, 35°C, Humidity: 60%",
    }
    return weather_data.get(city, f"Weather data not available for {city}")

# -------------------------------------------------------
# PART 3: Resources বানানো (Read-only data)
# -------------------------------------------------------
# Resource = AI যে data পড়তে পারে কিন্তু execute করে না

@mcp.resource("data://config")
def get_app_config() -> dict:
    """App configuration data"""
    return {
        "version": "1.0",
        "app_name": "My Awesome App",
        "max_users": 100,
        "supported_languages": ["english", "bangla", "arabic"],
    }

@mcp.resource("data://cities/{city_name}")
def get_city_info(city_name: str) -> dict:
    """শহরের তথ্য দাও"""
    cities = {
        "dhaka": {"population": "22 million", "area": "360 sq km", "capital": True},
        "chittagong": {"population": "8 million", "area": "168 sq km", "capital": False},
        "sylhet": {"population": "3.5 million", "area": "26 sq km", "capital": False},
    }
    return cities.get(city_name.lower(), {"error": "City not found"})

# -------------------------------------------------------
# PART 4: Prompts বানানো (Reusable templates)
# -------------------------------------------------------

@mcp.prompt
def generate_report(topic: str, language: str = "english") -> str:
    """একটা report generate করার template"""
    return f"""
    Please write a comprehensive report about: {topic}
    Language: {language}
    Include: Introduction, Main Points, Conclusion
    Keep it professional and concise.
    """

# -------------------------------------------------------
# PART 5: Tools সরাসরি test করা
# -------------------------------------------------------
print("=== Tools সরাসরি test করা ===")
print(add_numbers(5, 3))
print(greet_person("Rahim", "bangla"))
print(calculate_area("rectangle", 10, 5))
print(calculate_area("circle", 7))
print(check_weather("Dhaka"))
print(check_weather("Sylhet"))

# -------------------------------------------------------
# PART 6: Server চালানো
# -------------------------------------------------------
# Server run করতে:
# if __name__ == "__main__":
#     mcp.run()   # default: stdio transport

# বা HTTP transport দিয়ে:
# mcp.run(transport="streamable-http")
# তারপর http://localhost:8000 এ access করো

# Claude Desktop এ add করতে:
# claude_desktop_config.json এ এটা যোগ করো:
# {
#   "mcpServers": {
#     "my-server": {
#       "command": "python",
#       "args": ["path/to/this/file.py"]
#     }
#   }
# }

print("\n=== Server Info ===")
print("Server Name:", mcp.name)
print("MCP server বানানো হয়ে গেছে!")
print("Run করতে: mcp.run() বা python filename.py")

# -------------------------------------------------------
# 🧠 সহজ কথায়:
# FastMCP = AI কে custom tools দেওয়ার উপায়
# @mcp.tool → AI যে functions ব্যবহার করতে পারবে
# @mcp.resource → AI যে data পড়তে পারবে
# @mcp.prompt → Reusable prompt templates
# mcp.run() → Server শুরু করো
# Claude, GPT এরপর এই tools automatically ব্যবহার করতে পারবে
# -------------------------------------------------------
