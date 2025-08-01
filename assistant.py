#!/usr/bin/env python3

import os
import google.generativeai as genai
import subprocess
import time

# Load Gemini API key from environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5 pro")

def load_html(filepath):
    with open(filepath, "r") as file:
        return file.read()

def save_html(filepath, content):
    with open(filepath, "w") as file:
        file.write(content)

def edit_html_with_gemini(html_content, instruction):
    prompt = f"""
You are a helpful HTML assistant.
Here is the HTML code:
---
{html_content}
---
Task: {instruction}

Return the full updated HTML.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def open_editor(filepath):
    subprocess.run(["nano", filepath])

def main():
    print("\n🧠 Gemini HTML Assistant\n")
    filepath = input("Enter the path to your .html file: ").strip()

    if not filepath.endswith(".html"):
        print("❌ Only .html files are supported.")
        return

    if not os.path.exists(filepath):
        print("❌ File does not exist.")
        return

    while True:
        print("\nOptions:")
        print("1. Fix HTML formatting")
        print("2. Insert an image")
        print("3. Update text (e.g., pricing/description)")
        print("4. Open file in nano")
        print("5. Quit")

        choice = input("Choose an option (1–5): ").strip()

        if choice == "5":
            break

        html = load_html(filepath)

        if choice == "1":
            instruction = "Fix all HTML indentation and formatting."
        elif choice == "2":
            img_url = input("Image URL: ").strip()
            alt_text = input("Alt text: ").strip()
            instruction = f"Insert this image <img src='{img_url}' alt='{alt_text}'> inside the HTML appropriately."
        elif choice == "3":
            edit_text = input("What text should be updated? (e.g. 'Change price to R20')\n> ")
            instruction = f"Update the HTML based on this instruction: {edit_text}"
        elif choice == "4":
            open_editor(filepath)
            continue
        else:
            print("❌ Invalid option.")
            continue

        print("⏳ Sending to Gemini...")
        updated_html = edit_html_with_gemini(html, instruction)
        save_html(filepath, updated_html)
        print(f"✅ File updated: {filepath}")

if __name__ == "__main__":
    main()
