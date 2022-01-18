import pandas as pd

ALPH = "[abcdefghijklmnopqrstuvwxyz]"

def load_frequ_words():
    df = pd.read_csv("unigram_freq.csv")
    df = df[df.word.str.len() == 5]
    def only_once(s):
        return len(set(s)) == 5
    mask = df.word.apply(only_once)
    df = df[mask].word
    return df

def solve(df, word=None):
    print(f"word: {word}\n---\n")
    _df = df.copy()
    pattern = [ALPH]*5

    sampled_word = _df[_df.str.match("[etainos]"*5)].values[0]
    _c = 0
    for _ in range(5):
        while True:
            _sampled_word = input(f"Guess: {sampled_word}: ")
            if _sampled_word == "!":
                sampled_word = _df.values[_c]
                _c += 1
            elif len(_sampled_word) == 5:
                sampled_word = _sampled_word
                break
            elif _sampled_word == "":
                break
            else:
                sampled_word = _df.sample(1).values[0]

        contains = []
        score = input("(b)lack, (g)reen, (y)ellow: ")
        for i, (guess_char, s) in enumerate(zip(sampled_word, score), 0):
            try:
                if s.lower() == "g":
                    pattern[i] = guess_char
                elif s.lower() == "y":
                    pattern[i] = pattern[i].replace(guess_char, '')
                    _df = _df[_df.str.contains(guess_char)]
                elif s.lower() == "b":
                    pattern = [p.replace(guess_char, '') for p in pattern]
            except:
                breakpoint()
                print("-")

        _pattern = "".join(pattern)
        _df = _df[ _df.str.match(_pattern)]
        sampled_word = _df.values[0]
        _c = 0
        print(_df)


solve(load_frequ_words())
