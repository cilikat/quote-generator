import random

def load_quotes(path="quotes/quotes.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    quotes = load_quotes()
    quote = random.choice(quotes)
    print("\n💬 Random Crypto Quote:\n")
    print(f"“{quote}”\n")

if __name__ == "__main__":
    main()
