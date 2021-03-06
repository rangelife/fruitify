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
    universe = "ðððððððððððððĨ­ððĨĨðĨðððĨðĨðķð―ð°ðĨððĨĶðĨŽðĨð§ð§ðĨð ðĨðĨŊððĨðĨĻð§ðĨðģð§ðĨð§ðĨðĨĐðððĶīð­ððððĨŠðĨð§ðŪðŊðĨðĨðĨŦðððēððĢðąðĨðĶŠðĪððððĨðĨ ðĨŪðĒðĄð§ðĻðĶðĨ§ð§ð°ððŪð­ðŽðŦðŋðĐðŠðŊðĨðžâïļðĩð§ðĨĪðķðšðŧðĨð·ðĨðļðđð§ðūð§ðĨðīð―ðĨĢðĨĄðĨĒð§"
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
