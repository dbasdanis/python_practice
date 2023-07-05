words = [
    "able lost darkness learn",
    "road older goes",
    "basic",
    "must seed laid itself hot must",
    "compound decide",
    "trap active paragraph hair review stay written",
    "facing smile vowel chose other",
    "occur shop box metal equal mouse some city"
]

# most = max((len(string.split(" ")) for string in words))
ind_words = (string.split(" ") for string in words)
word_length = (len(lst) for lst in ind_words)
most = max(word_length)
print(most)