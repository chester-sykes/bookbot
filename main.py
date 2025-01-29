def main():
    with open ('books/frankenstein.txt')  as f:
        file_contents = f.read()
        counts = get_counts_of_chars(file_contents)
        dict_counts = []

        for key in counts:
            dict_counts.append({'name': key, 'num': counts[key]})

        dict_counts.sort(reverse=True, key=sort_on)

        count_of_words = count_words(file_contents)
        print('--- Begin report of books/frankenstein.txt ---')
        print(f"{count_of_words} words found in the document")

        for value in dict_counts:
            name = value['name']
            num = value['num']
            if name != ' ' and name != '.' and name != '#':
                print(f"The '{name}' character was found {num} times")
            
        print('--- End report ---')


def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_counts_of_chars(file_contents):
    file_contents = file_contents.lower()
    char_count = {}
    for char in file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

main()

