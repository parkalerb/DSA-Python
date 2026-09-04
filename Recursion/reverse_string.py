def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


text = "python"

result = reverse_string(text)

print("Original string:", text)
print("Reversed string:", result)