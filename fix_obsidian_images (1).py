#!/usr/bin/env python3
"""
Make image links in Obsidian notes render on GitHub.

Handles:
  ![[Pasted image 2026.png|622]]        Obsidian embeds
  ![298](Pasted%20image%202026.png)     Markdown links with a wrong path, or a
                                        size stuck in the alt text

Every image is found by file name anywhere in the repo, linked with a path
relative to the note, and spaces are URL-encoded. A size becomes an <img> tag
with that width. Links that already work are left alone. Links to images that
aren't in the repo are listed.

Usage (run from the repo root, after committing so you can review the diff):
    python fix_obsidian_images.py            # preview only, changes nothing
    python fix_obsidian_images.py --apply    # rewrite the files
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}
WIKI = re.compile(r"!\[\[([^\]|#]+?)(?:\|(\d+)(?:x\d+)?)?\]\]")
MD = re.compile(r"!\[([^\]]*)\]\(\s*<?([^)>]+?)>?\s*\)")

root = Path(".").resolve()
apply = "--apply" in sys.argv

images = {}
for p in root.rglob("*"):
    if ".git" in p.parts or p.suffix.lower() not in IMAGE_EXTS:
        continue
    images.setdefault(p.name, []).append(p)

missing, changed_files = [], 0


def build(md, target, width, alt=None):
    """Return the GitHub-friendly link, or None if the image isn't in the repo."""
    name = Path(unquote(target)).name
    candidates = images.get(name)
    if not candidates:
        return None
    rel = Path(os.path.relpath(candidates[0], md.parent)).as_posix()
    url = quote(rel, safe="/")
    if width:
        return f'<img src="{url}" width="{width}">'
    return f"![{alt if alt is not None else Path(name).stem}]({url})"


for md in root.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")

    def fix_wiki(m):
        out = build(md, m.group(1).strip(), m.group(2))
        if out is None:
            missing.append(f"{md.relative_to(root)}: {m.group(1)}")
            return m.group(0)
        return out

    def fix_md(m):
        alt, target = m.group(1), m.group(2).strip()
        if target.startswith(("http://", "https://", "data:")):
            return m.group(0)
        if Path(unquote(target)).suffix.lower() not in IMAGE_EXTS:
            return m.group(0)
        width = alt if alt.isdigit() else None
        if width is None and (md.parent / unquote(target)).is_file() and " " not in target:
            return m.group(0)  # already fine
        out = build(md, target, width, None if width else alt)
        if out is None:
            missing.append(f"{md.relative_to(root)}: {target}")
            return m.group(0)
        return out

    new = MD.sub(fix_md, WIKI.sub(fix_wiki, text))
    if new != text:
        changed_files += 1
        print(f"{'Updated' if apply else 'Would update'}: {md.relative_to(root)}")
        if apply:
            md.write_text(new, encoding="utf-8")

print(f"\n{changed_files} note(s) {'updated' if apply else 'would change'}.")
if missing:
    print("\nImages NOT found in the repo:")
    for line in missing:
        print("  " + line)
if not apply:
    print("\nPreview only. Run with --apply to write the changes.")
