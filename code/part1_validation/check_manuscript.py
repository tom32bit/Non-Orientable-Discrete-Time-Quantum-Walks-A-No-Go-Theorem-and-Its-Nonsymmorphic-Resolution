"""Mechanical validation of paper/main.tex (no TeX installation needed):
balanced environments, citation keys vs refs.bib, ref/label consistency,
figure files present, math-delimiter and brace balance, TODO inventory,
abstract word count. Run from repository root or paper/."""

import os
import re
import sys
from collections import Counter

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(here))
tex = open(os.path.join(root, "paper", "main.tex"), encoding="utf-8").read()
bib = open(os.path.join(root, "paper", "refs.bib"), encoding="utf-8").read()
issues = []

envs = Counter(re.findall(r"\\begin\{(\w+\*?)\}", tex))
ends = Counter(re.findall(r"\\end\{(\w+\*?)\}", tex))
for env in set(envs) | set(ends):
    if envs[env] != ends[env]:
        issues.append(f"environment mismatch: {env} begin={envs[env]} end={ends[env]}")

bibkeys = set(re.findall(r"@\w+\{([^,]+),", bib))
cited = set()
for m in re.findall(r"\\cite\{([^}]+)\}", tex):
    cited.update(k.strip() for k in m.split(","))
for k in sorted(cited - bibkeys):
    issues.append(f"citation key missing from refs.bib: {k}")
unused = bibkeys - cited
print(f"cited: {len(cited)} keys; uncited bib entries: "
      f"{sorted(unused) if unused else 'none'}")

labels = set(re.findall(r"\\label\{([^}]+)\}", tex))
refs = set(re.findall(r"\\(?:eq)?ref\{([^}]+)\}", tex))
for r in sorted(refs - labels):
    issues.append(f"ref to undefined label: {r}")
for lab in sorted(labels - refs):
    print(f"note: label defined but never referenced: {lab}")

# graphicspath search dirs, resolved relative to paper/ (mirrors the .tex)
gpaths = re.findall(r"\\graphicspath\{((?:\{[^}]*\})+)\}", tex)
searchdirs = re.findall(r"\{([^}]*)\}", gpaths[0]) if gpaths else ["figures/"]
for g in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", tex):
    found = any(os.path.exists(os.path.join(root, "paper", d, g))
                for d in searchdirs)
    if not found:
        issues.append(f"figure file missing on graphicspath: {g}")

ndollar = len(re.findall(r"(?<!\\)\$", tex))
if ndollar % 2:
    issues.append(f"odd number of $ delimiters: {ndollar}")
if tex.count("{") != tex.count("}"):
    issues.append(f"brace mismatch: open={tex.count('{')} close={tex.count('}')}")

todos = [line.strip() for line in tex.splitlines() if "TODO" in line]
print(f"TODO lines (expected 1, the email placeholder): {todos}")
if len(todos) != 1:
    issues.append(f"unexpected TODO count: {len(todos)}")

m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
words = re.sub(r"\\[a-zA-Z]+|\$[^$]*\$|[{}$~]", " ", m.group(1)).split()
print(f"abstract word count: {len(words)} (target <= 250)")
if len(words) > 250:
    issues.append(f"abstract too long: {len(words)} words")

print()
if issues:
    print("ISSUES:")
    for i in issues:
        print(" -", i)
    sys.exit(1)
print("MECHANICAL CHECKS PASS")
