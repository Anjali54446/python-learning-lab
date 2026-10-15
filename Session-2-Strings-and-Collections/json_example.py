# Session 2 Example 7: JSON
# JSON is often used to exchange structured data with APIs and AI tools.

import json

prompt_record = {
    "task": "summarize",
    "text": "Python dictionaries store key-value pairs.",
    "max_words": 20,
    "include_bullets": True,
    "tags": ["Python", "beginner"]
}

json_text = json.dumps(prompt_record, indent=2)
print("JSON text:")
print(json_text)

restored_record = json.loads(json_text)
print("Task:", restored_record["task"])
print("First tag:", restored_record["tags"][0])
