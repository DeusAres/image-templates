from sys import argv

def main(text, splitter, terminator):
    with open(text, 'r', 'utf-8') as f:
        quotes = f.readlines()

    if splitter:
        quotes = [each.split(splitter) for each in quotes]
    
    if terminator:
        quotes = quotes.split(terminator)

if __name__ == '__main__':
    main(argv[1:])