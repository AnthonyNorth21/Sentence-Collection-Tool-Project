
# Sentence Collection Tool

A command-line Python program to collect, store, search, and analyze sentences entered by the user. Sentences are timestamped and can be saved to a text file for later reference.

## Features

* Add multiple sentences with automatic timestamps
* View all collected sentences with timestamps
* Search sentences containing a specific keyword (case-insensitive)
* Display statistics including total sentences, average length, longest and shortest sentences
* Save collected sentences to a file (`sentences.txt`)
* Interactive menu-driven interface
* Input validation with user-friendly messages

## How It Works

* The program presents a menu with options to add, view, search, analyze, save, or exit
* When adding sentences, the user can input as many as they want until they type `exit`
* Sentences are stored internally along with the current timestamp
* The search function looks for sentences containing the user’s keyword, ignoring case
* Statistics provide insight into the collection’s size and sentence lengths
* Saved sentences are written to a plain text file with timestamps for easy reference

## Sample Interaction

Menu:

1. Add sentences
2. View all sentences
3. Search sentences by keyword
4. Show statistics
5. Save sentences to file
6. Exit

Select an option (1-6): 1
Enter sentences (type 'exit' to stop):

> The quick brown fox.
> Jumps over the lazy dog.
> exit
> 2 sentence(s) collected so far.

Select an option (1-6): 3
Enter a keyword to search: fox

Found 1 sentence(s) containing 'fox':

1. \[2025-08-24 15:34:00] The quick brown fox.

Select an option (1-6): 4

Sentence Statistics:
Total sentences: 2
Average sentence length: 22.5 characters
Longest sentence (25 chars): Jumps over the lazy dog.
Shortest sentence (20 chars): The quick brown fox.

Select an option (1-6): 5
Sentences saved to 'sentences.txt'.

Select an option (1-6): 6
Exiting program. Goodbye!

## Code Overview

**get\_sentence()**
Prompts the user for a sentence, enforcing non-empty input or 'exit' to stop.

**save\_sentences(sentences, filename)**
Writes all collected sentences with timestamps to a specified text file.

**search\_sentences(sentences, keyword)**
Filters and displays sentences containing the keyword.

**print\_statistics(sentences)**
Calculates and displays total count, average length, longest and shortest sentences.

**main()**
Manages the interactive menu and controls program flow.

