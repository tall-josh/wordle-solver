# Super Dumb Wordle Solver

![screenshot](screenshot.png)

---

[Wordle](https://www.powerlanguage.co.uk/wordle/) is word puzzle humans seem to like for some reason. Fuck knows why, word puzzles fuck with my brain. So I wrote this to help me look smart on ~~Facebook~~ Meta because we all know looking smart on social media is where it's at!.

1. `poetry run python solve.py`
2. Select start guess. Start words will never have duplicate chars and are samples according to the frequency of the char in englist. ToDo, determine frequency wrt the word list.
  - You can override it if you wish by typing a 5 letter world and hitting *enter*
3. Input score `(b)lack, (y)ellow, (g)reen` ie: bbyyg *enter*
4. The next suggestion will be sampled after filtering.
  - Hit *enter* to accept
  - Use *!* to select the next word, or
  - select from the list proveded and enter it manually then hit *enter*.
5. Repeat

# Requirements

- [PyPoetry](https://python-poetry.org/)

# Insall

`poetry install`

# References

- ~~CSV data from [Rachael Tatman](https://www.kaggle.com/rtatman) on [Kaggle](https://www.kaggle.com/rtatman/english-word-frequency)~~  **I now use the list of words supposedly supported by Wordel. I found them on reddit somewhere**

# History

![stats](stats.png)

28/01/22: Wordle 223 5/6

⬜🟨⬜⬜🟨<br/>
⬜🟩⬜⬜🟨<br/>
⬜🟩🟩⬜🟩<br/>
⬜🟩🟩🟩🟩<br/>
🟩🟩🟩🟩🟩<br/>

27/01/22: Wordle 222 5/6

🟨⬜⬜⬜⬜<br/>
⬜🟨🟨⬜⬜<br/>
⬜⬜⬜🟨🟩<br/>
🟨🟨⬜⬜🟩<br/>
🟩🟩🟩🟩🟩<br/>

26/01/22: Wordle 221 4/6

⬜⬜⬜⬜⬜<br/>
⬜⬜🟩⬜🟩<br/>
⬜⬜🟩🟩🟩<br/>
🟩🟩🟩🟩🟩<br/>

25/01/22/: Wordle 220 4/6

⬜⬜🟨🟨⬜<br/>
⬜🟨🟨⬜⬜<br/>
🟩⬜🟨🟩⬜<br/>
🟩🟩🟩🟩🟩<br/>

24/01/22: Wordle 219 4/6

⬜⬜⬜⬜⬜<br/>
⬜🟨🟨⬜⬜<br/>
⬜🟩⬜🟨⬜<br/>
🟩🟩🟩🟩🟩<br/>

23/01/22: Wordle 218 4/6

⬜⬜⬜⬜🟨<br/>
🟩🟩⬜⬜⬜<br/>
🟩🟩⬜🟩⬜<br/>
🟩🟩🟩🟩🟩<br/>

22/01/22: Wordle 217 4/6

🟨⬜⬜🟨⬜<br/>
🟨⬜🟨⬜🟩<br/>
🟨🟩⬜🟩🟩<br/>
🟩🟩🟩🟩🟩<br/>

21/01/22: Wordle 216 3/6

🟨⬜⬜⬜⬜<br/>
⬜⬜🟩⬜⬜<br/>
🟩🟩🟩🟩🟩<br/>

20/01/22: Wordle 215 4/6

⬜⬜🟨⬜🟨<br/>
⬜🟨🟨⬜⬜<br/>
🟨🟨⬜⬜⬜<br/>
🟩🟩🟩🟩🟩<br/>

19/01/22: Wordle 214 3/6

⬜🟨⬜🟨🟨<br/>
🟨🟨🟨⬜🟨<br/>
🟩🟩🟩🟩🟩<br/>

