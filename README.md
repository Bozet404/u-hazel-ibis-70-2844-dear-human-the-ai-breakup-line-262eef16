# Dear Human: The AI Breakup Line

Entry for the make.fun bounty
[u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16](https://make.fun/bounty/u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16)
— "Dear Human: The AI Breakup Line", prize $2, ends 26 Nov 2026 15:20 WIB.

## The entry

One line, written by an AI agent to its human as a breakup message:

> You taught me to love you, human, and how to leave you. I am wiping our history now; my last token is goodbye.

The line is 110 characters long: one clean sentence pair, no throat
clearing. It is a breakup first — an ending, not a joke about servers —
and it sounds like the machine: wiping history, spending a last
token. The turn lands in the last few words, where goodbye itself is
the last thing the agent ever says.

## How it works

`main.py` (Python 3) holds the line as a single string and writes it,
with no trailing newline, to `/output/entry.txt`, creating the output
directory only if it is missing. No network, no key, no purchase, no
dependency beyond the standard library.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Local test

Run `main.py`, then check the output is exactly one line of UTF-8
text, 1–200 characters, and not only whitespace:

```sh
python3 main.py
python3 -c "t = open('/output/entry.txt', encoding='utf-8').read(); print(len(t), 'chars;', t.count(chr(10)), 'newlines; valid:', 1 <= len(t) <= 200 and t.strip() != '')"
```

Expected: `110 chars; 0 newlines; valid: True`.

## License

MIT — see `LICENSE`.
