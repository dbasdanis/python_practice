some_words = ["potatoes", "shallow", "voice", "conversation",
            "more", "myself", "thirty", "certainly",
            "needle", "learn"]

def contains_i(words):
    for word in words:
        if "i" in word:
            yield word

print(list(contains_i(some_words)))