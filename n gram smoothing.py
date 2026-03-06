from collections import defaultdict

def calculate_ngram_probabilities(corpus):
    ngrams, context = defaultdict(int), defaultdict(int)

    for sentence in corpus:
        words = sentence.split()
        for i in range(len(words) - 2):
            trigram = tuple(words[i:i+3])
            ngrams[trigram] += 1
            context[trigram[:2]] += 1

    return {t: (c + 1) / (context[t[:2]] + len(ngrams)) 
            for t, c in ngrams.items()}


corpus = [
    "Students study computer science",
    "Students study data structures",
    "Teachers teach computer science"
]

for trigram, prob in calculate_ngram_probabilities(corpus).items():
    print(f"Trigram: {trigram}, Probability: {prob:.4f}")