import sys
import re
import json

with open(sys.argv[1]) as f:
    text = f.read()

if len(sys.argv) > 2:
    with open(sys.argv[2]) as f:
        lookup_spec = json.load(f)
        universe = lookup_spec["universe"]
        lookups = lookup_spec["lookups"]
else:
    # defaults
    universe = "🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🥭🍍🥥🥝🍅🍆🥑🥒🌶🌽🌰🥜🍄🥦🥬🥕🧄🧅🥔🍠🥐🥯🍞🥖🥨🧀🧀🥚🍳🧈🥞🧇🥓🥩🍗🍖🦴🌭🍔🍟🍕🥪🥙🧆🌮🌯🥗🥘🥫🍝🍜🍲🍛🍣🍱🥟🦪🍤🍙🍚🍘🍥🥠🥮🍢🍡🍧🍨🍦🥧🧁🍰🎂🍮🍭🍬🍫🍿🍩🍪🍯🥛🍼☕️🍵🧃🥤🍶🍺🍻🥂🍷🥃🍸🍹🧉🍾🧊🥄🍴🍽🥣🥡🥢🧂"
    lookups = {}

print(f"universe:  {universe}")

remaining_universe = universe
for l in lookups:
    remaining_universe = remaining_universe.replace(lookups[l], "")

print(f"remaining: {remaining_universe}")


nstep = 0


def show(t, step_name):
    global nstep
    print(f"\n\n===\n\nAfter step {nstep} - {step_name}:\n\n{t}\n")
    nstep = nstep + 1


# lowercase
# split lines
# split words
# lookup and replace
# rejoin words
# show key

show(text, "original")

text = text.lower()
show(text, "lowercase")

r = re.compile("\n")
text = r.sub(" NEWLINE ", text)
lookups["NEWLINE"] = "NEWLINE"
show(text, "split lines")

word_tokens = text.split()
show(word_tokens, "split words")

emoji_tokens = []
for t in word_tokens:
    if not t in lookups:
        lookups[t] = remaining_universe[0]
        remaining_universe = remaining_universe[1:]
    emoji_tokens.append(lookups[t])
show(emoji_tokens, "lookup&replace")

result = " ".join(emoji_tokens)
result = (result + " ").replace("NEWLINE ", "\n")
show(result, "rejoin")


# show key

print("===\n\nKey:")
del lookups["NEWLINE"]
for l in sorted(lookups):
    print(f"{lookups[l]} - {l}")
