def reverse_word_order(string):
    words = string.split(" ")
    if len(words) == 1:
        print(words[0])
    else:
        reverse_words = []
        for x in range(1, len(words)+1):
            reverse_words.append(words[-x])
        reverse_string = " ".join(reverse_words)
        print(reverse_string)


reverse_word_order(input("Write a sentence you'd like to reverse: "))


