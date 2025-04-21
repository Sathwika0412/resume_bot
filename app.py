
---

### `resume_bot.py`
```python
import re

# Define sample role requirements
ROLE_KEYWORDS = {
    "python": 2,
    "nlp": 2,
    "tensorflow": 1,
    "prompt engineering": 3,
    "machine learning": 2,
    "generative ai": 3
}

def analyze_resume(resume_text):
    resume_text = resume_text.lower()
    score = 0
    feedback = []

    for keyword, weight in ROLE_KEYWORDS.items():
        if keyword in resume_text:
            score += weight
            feedback.append(f"✅ Contains '{keyword}'")
        else:
            feedback.append(f"❌ Missing '{keyword}'")

    return score, feedback

# Example run
if __name__ == "__main__":
    resume_input = input("Paste your resume text:\n")
    score, tips = analyze_resume(resume_input)
    print(f"\nYour Role-Fit Score: {score}/15\n")
    print("Feedback:")
    for line in tips:
        print(line)
