import pandas as pd

ALPH = "[abcdefghijklmnopqrstuvwxyz]"

def load_words():
    df = pd.read_csv("words.txt")
    return df.word

#def load_frequ_words():
#    df = pd.read_csv("unigram_freq.csv")
#    df = df[df.word.str.len() == 5]
#    def only_once(s):
#        return len(set(s)) == 5
#    mask = df.word.apply(only_once)
#    df = df[mask].word
#    return df

def word_has_n(word, char, n):
    return len([c for c in word if c == char]) >= n

def word_has_one_of_each(word):
    return len(set(word)) == len(word)

def solve(df, word=None):

    print(f"word: {word}\n---\n")
    _df = df.copy()
    pattern = [ALPH]*5

    ooe = _df[_df.apply(word_has_one_of_each)]
    start_df = ooe[ooe.str.match("[etainos]"*5)]
    print(start_df)
    guess_word = start_df.sample(1).values[0]

    resample_idx = 0
    for _ in range(5):
        while True:
            _guess_word = input(f"Guess: {guess_word}: ")
            if _guess_word == "!":
                guess_word = _df.values[resample_idx]
                resample_idx += 1
            elif len(_guess_word) == 5:
                guess_word = _guess_word
                break
            elif _guess_word == "":
                break
            else:
                guess_word = _df.sample(1).values[0]

        contains = []
        colors = input("(b)lack, (g)reen, (y)ellow: ")
        for i, (guess_char, color) in enumerate(zip(guess_word, colors), 0):
            color = color.lower()
            try:
                if color == "g":
                    pattern[i] = guess_char
                elif color == "y":
                    pattern[i] = pattern[i].replace(guess_char, '')
                    contains += guess_char
                elif color == "b":
                    # added if statement to top from removing conirmed chars
                    # ie:
                    # TRUST
                    # ggggb
                    # without the if would remove the fist t from the pattern
                    for idx, pat in enumerate(pattern):
                        if pat != guess_char:
                            pattern[idx] = pattern[idx].replace(guess_char, "")
            except Exception as e:
                breakpoint()
                print("-")

        for char in set(contains):
            char_count = len([c for c in contains if c == char])
            _df = _df[_df.apply(lambda w: word_has_n(w, char, char_count))]

        _pattern = "".join(pattern)
        _df = _df[ _df.str.match(_pattern)]
        guess_word = _df.sample(1).values[0]
        resample_idx = 0
        print(_df)


solve(load_words())
