course = {
    "title": "Python Interactive",
    "type": "Course",
    "lesson": 58
}

print(course.keys())
print(course.values())
print(course.items())

course.update({"batch": 17})  # update for update the course dictionary with new key-value pair. It will add the new key-value pair to the dictionary if the key is not already present. If the key is already present, it will update the value of the existing key.
print(course)