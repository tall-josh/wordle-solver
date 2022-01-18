# Super Dumb Wordle Solver

![screenshot](screenshot.png)

---

[Wordle](https://www.powerlanguage.co.uk/wordle/) is word puzzle humans seem to like for some reason. Fuck knows why, word puzzles fuck with my brain. So I wrote this to help me look smart on ~~Facebook~~ Meta because we all know looking smart on social media is where it's at!.

1. `poetry run python solve.py`
2. By default will start with with *note* as the first suggestion. *Note* is a common word that contains common letters.
  - You can override it if you wish by typing a 5 letter world and hitting *enter*
3. Input score `(b)lack, (y)ellow, (g)reen` ie: bbyyg *enter*
4. The next suggestion will be the most common word after filtering.
  - Hit *enter* to accept
  - Use *!* to select the next most common word, or
  - select from the list proveded and enter it manually then hit *enter*.
5. Repeat

# Requirements

- [PyPoetry](https://python-poetry.org/)

# Insall

`poetry install`

# Limitations

- Only words without duplicate charaters are user
- Many of the less common words are not accepted by Wordle but if you stick with the common words it seems to be ok

# References

- CSV data from [Rachael Tatman](https://www.kaggle.com/rtatman) on [Kaggle](https://www.kaggle.com/rtatman/english-word-frequency)
