n = ["Michael", "Lieberman"]

def join_strings(words):
    result = ""
    for word in words:
        result = result + word
    return result

print(join_strings(n))