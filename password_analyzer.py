import tkinter as tk
from tkinter import messagebox
import hashlib
import string
import math

# Function to analyze password strength
def analyze_password():
    password = entry.get()
    strength_score = 0
    feedback = []
    
    # Criteria for password strength
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Scoring system
    if length >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if has_upper:
        strength_score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if has_lower:
        strength_score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    if has_digit:
        strength_score += 1
    else:
        feedback.append("Include at least one number.")
    
    if has_special:
        strength_score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")
    
    # Entropy calculation
    char_space = 0
    if has_lower:
        char_space += 26
    if has_upper:
        char_space += 26
    if has_digit:
        char_space += 10
    if has_special:
        char_space += len(string.punctuation)
    
    entropy = math.log2(char_space ** length) if char_space > 0 else 0
    
    # Strength rating
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Hash the password (for demonstration purposes, not storing it)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Show result
    result_label.config(text=f"Strength: {strength}\nEntropy: {entropy:.2f} bits")
    feedback_label.config(text="\n".join(feedback))
    hash_label.config(text=f"SHA-256 Hash: {hashed_password[:20]}...")

# GUI setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x300")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=analyze_password).pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

feedback_label = tk.Label(root, text="", fg="red")
feedback_label.pack(pady=5)

hash_label = tk.Label(root, text="")
hash_label.pack(pady=5)

root.mainloop()
