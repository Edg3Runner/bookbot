def main():
        book_path = "books/frankenstein.txt"
        file_contents = get_book(book_path) 
        count_words = get_count_words(file_contents) #Done
        count_chars = get_count_char(file_contents) #Done
        aggregate_chars = aggregate(count_chars) #Done
        print_report(book_path, count_words,aggregate_chars)

def get_book(book_path):
    with open(book_path) as f:
        return f.read()
        
def get_count_words(text):
    words = text.split()
    return len(words)

def get_count_char(text):
    char_count = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Will be used as reference on which key to sort
def sort_on(dict):
    return dict["value"]

def aggregate(dict):
    list_dict = []
    for key,value in dict.items():
        if key.isalpha():
            list_dict.append({"key": key, "value": value})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def print_report(book_path, count_words, aggregate_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")
    print()
    for item in aggregate_chars:
        print(f"the '{item['key']}' character was found {item['value']} times")
    print("--- End report ---")

main()
