some_words = ["potatoes", "shallow", "voice", "conversation",
            "more", "myself", "thirty", "certainly",
            "needle", "learn"]

def contains_i(words):
    for word in words:
        if "i" in word:
            yield word

gen_ob = contains_i(some_words)

# convert tpye 
print(list(gen_ob))
print(set(contains_i(some_words)))
print(tuple(contains_i(some_words)))