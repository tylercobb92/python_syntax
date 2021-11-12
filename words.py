def print_upper_words(words):
   """Given a list of words, print each word in all caps
   
   For example: 
        print_upper_words(['apple', 'orange', 'banana'])

    Should print:
        APPLE
        ORANGE
        BANANA
   """
   
   for word in words:
        x = word.upper()
        print(x)


def print_e_words(words):
    """Given a list of words, print each word that starts with e or E in all caps
    
    For example:
        print_e_words(['eggs','apple','banana','Eggplant'])

    Should print:
        EGGS
        EGGPLANT
    """

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            x = word.upper()
            print(x)


def print_upper_words2(words, starts_with):
    """Given a list of words and a list of letters, print each word beginning with a letter from start_with in all caps

        For example:
            print_upper_words2(['orange','apple','banana','artichoke','peach'], ['a','b'])

        Should print:
            APPLE
            BANANA
            ARTICHOKE
    """
    
    for word in words:
        for letter in starts_with:
            if word.startswith(letter) or word.startswith(letter.upper()):
                x=word.upper()
                print(x)







