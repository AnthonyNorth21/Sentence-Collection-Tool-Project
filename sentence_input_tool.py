import datetime

def get_sentence():
    while True:
        sentence = input("Enter a sentence (or type 'exit' to finish): ").strip()
        if sentence.lower() == 'exit':
            return None
        if sentence == "":
            print("Empty sentence not allowed. Please enter some text.")
        else:
            return sentence

def save_sentences(sentences, filename="sentences.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for timestamp, sentence in sentences:
            f.write(f"[{timestamp}] {sentence}\n")
    print(f"Sentences saved to '{filename}'.")

def search_sentences(sentences, keyword):
    keyword = keyword.lower()
    filtered = [(i, ts, s) for i, (ts, s) in enumerate(sentences, start=1) if keyword in s.lower()]
    if filtered:
        print(f"\nFound {len(filtered)} sentence(s) containing '{keyword}':")
        for i, ts, s in filtered:
            print(f"{i}. [{ts}] {s}")
    else:
        print(f"No sentences found containing '{keyword}'.")

def print_statistics(sentences):
    if not sentences:
        print("No sentences to analyze.")
        return

    lengths = [len(s) for _, s in sentences]
    avg_length = sum(lengths) / len(lengths)
    longest = max(sentences, key=lambda x: len(x[1]))
    shortest = min(sentences, key=lambda x: len(x[1]))

    print("\nSentence Statistics:")
    print(f"Total sentences: {len(sentences)}")
    print(f"Average sentence length: {avg_length:.1f} characters")
    print(f"Longest sentence ({len(longest[1])} chars): {longest[1]}")
    print(f"Shortest sentence ({len(shortest[1])} chars): {shortest[1]}")

def main():
    sentences = []
    print("Welcome to the Advanced Sentence Collector!")

    while True:
        print("\nMenu:")
        print("1. Add sentences")
        print("2. View all sentences")
        print("3. Search sentences by keyword")
        print("4. Show statistics")
        print("5. Save sentences to file")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            print("Enter sentences (type 'exit' to stop):")
            while True:
                sentence = get_sentence()
                if sentence is None:
                    break
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sentences.append((timestamp, sentence))
            print(f"{len(sentences)} sentence(s) collected so far.")
        elif choice == '2':
            if not sentences:
                print("No sentences to display.")
            else:
                print("\nCollected sentences:")
                for i, (ts, s) in enumerate(sentences, start=1):
                    print(f"{i}. [{ts}] {s}")
        elif choice == '3':
            if not sentences:
                print("No sentences to search.")
                continue
            keyword = input("Enter a keyword to search: ").strip()
            if keyword:
                search_sentences(sentences, keyword)
            else:
                print("Keyword cannot be empty.")
        elif choice == '4':
            print_statistics(sentences)
        elif choice == '5':
            if not sentences:
                print("No sentences to save.")
            else:
                save_sentences(sentences)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-6.")

if __name__ == "__main__":
    main()

