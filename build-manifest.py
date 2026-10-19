#!/usr/bin/env python3
"""Regenerate quizzes/index.json from the quiz files in quizzes/<block>/*.json.

Run from the repo root after adding, removing or renaming a quiz:
    python3 build-manifest.py
"""
import json
from pathlib import Path

root = Path(__file__).parent
quizzes_dir = root / "quizzes"
blocks = []

for block_dir in sorted(p for p in quizzes_dir.iterdir() if p.is_dir()):
    items = []
    for f in sorted(block_dir.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        items.append({
            "title": data.get("title", f.stem),
            "description": data.get("description", ""),
            "count": len(data["questions"]),
            "file": f.relative_to(root).as_posix(),
        })
    if items:
        blocks.append({"name": block_dir.name, "quizzes": items})

out = quizzes_dir / "index.json"
out.write_text(json.dumps({"blocks": blocks}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {out.relative_to(root)}: {sum(len(b['quizzes']) for b in blocks)} quizzes in {len(blocks)} blocks")
