#!/usr/bin/env python3
"""
Convert Obsidian image embeds to GitHub-compatible links.

  ![[Pasted image 20261017204521.png|622]]
    -> <img src="attachments/Pasted%20image%2020261017204521.png" width="622">
  ![[topology.png]]
    -> ![topology](attachments/topology.png)

Paths are computed relative to each note, and spaces are URL-encoded.
Embeds whose image can't be found inside the repo are left unchanged and listed,
so you know which images still need to be moved into the repo.

Usage (run from the repo root, after committing so you can review the diff):
    python fix_obsidian_images.py            # preview only, changes nothing
    python fix_obsidian_images.py --apply    # rewrite the files
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}
EMBED = re.compile(r"!\[\[([^\]|#]+?)(?:\|(\d+)(?:x\d+)?)?\]\]")

root = Path(".").resolve()
apply = "--apply" in sys.argv

# Index every image in the repo by its file name.
images = {}
for p in root.rglob("*"):
    if ".git" in p.parts or p.suffix.lower() not in IMAGE_EXTS:
        continue
    images.setdefault(p.name, []).append(p)

missing, changed_files = [], 0

for md in root.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")

    def convert(m):
        target, width = m.group(1).strip(), m.group(2)
        name = Path(target).name
        candidates = images.get(name, [])
        if not candidates:
            missing.append(f"{md.relative_to(root)}: {target}")
            return m.group(0)
        img = candidates[0]
        rel = Path(os.path.relpath(img, md.parent)).as_posix()
        url = quote(rel, safe="/")
        if width:
            return f'<img src="{url}" width="{width}">'
        return f"![{Path(name).stem}]({url})"

    new = EMBED.sub(convert, text)
    if new != text:
        changed_files += 1
        print(f"{'Updated' if apply else 'Would update'}: {md.relative_to(root)}")
        if apply:
            md.write_text(new, encoding="utf-8")

print(f"\n{changed_files} note(s) {'updated' if apply else 'would change'}.")
if missing:
    print("\nImages NOT found in the repo (move them in, then run again):")
    for line in missing:
        print("  " + line)
if not apply:
    print("\nPreview only. Run with --apply to write the changes.")
