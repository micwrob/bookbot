def main():
    path_to_book = "books/frankenstein.txt"
    printed_book = read_book(path_to_book)
    words_count = count_words(printed_book)
    letter_count = count_letter(printed_book)
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{words_count} words found in the document")
    print()
    count_occurences(letter_count)
    print("--- End report ---")
    
    


def read_book(path_to_book):
    with open(path_to_book) as f:
        book_content = f.read()
    return book_content

def count_words(text):
    splited_text = text.split()
    return len(splited_text)

def count_letter(text):
    dict = {}
    for c in text:
        c = c.lower()
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict

def sort_on(dict):
    for key in dict:
        return dict[key]
    
def count_occurences(dict):
    dict_alpha = {}
    for items in dict:
        if items.isalpha():
            dict_alpha[items] = dict[items]
    new_list = [{key: dict_alpha[key]} for key in dict_alpha]
    new_list.sort(reverse=True, key=sort_on)
    for i in range(0, len(new_list)):
        for key in new_list[i]:
            print(f"The '{key}' character was found {new_list[i][key]} times")


main()