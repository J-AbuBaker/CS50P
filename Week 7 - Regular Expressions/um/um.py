import re

def main():
    print(count(input("Text: ")))

def count(txt):
    match = re.findall(r'\bum\b', txt, re.IGNORECASE)
    return len(match)

if __name__ == "__main__":
    main()
