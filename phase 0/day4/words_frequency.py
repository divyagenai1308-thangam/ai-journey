sentence = input("Enter your sentence here: ")

counts = {}

for word in sentence.lower().split():
    counts[word] = counts.get(word, 0)+1

for word, count in counts.items():
    print(f"{word}: {count}")