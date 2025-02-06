def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    char_list = get_num_characters(text)
    for char_data in char_list:
        print(f"The '{char_data['char']}' character was found {char_data['num']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    char_dict = {}
    text_lowered = text.lower()
    for char in text_lowered:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        else:
            pass
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(key=sort_on, reverse = True)
    return char_list
    

def sort_on(dict):
    return dict["num"]


main()