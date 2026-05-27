#!/usr/bin/env python3
"""
Rewrite stateDiagram-v2 blocks: one-line `note right of X : ...` with `;` breaks Mermaid
(statement separator). Convert those notes to `note` / `end note` blocks.
Replace literal \\n in transition labels with <br/>.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

NOTE_LINE = re.compile(r"^(\s*)note right of (\w+) : (.*)$")
MERMAID_BLOCK = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL)


def fix_state_block(body: str) -> str:
    lines = body.split("\n")
    out: list[str] = []
    for line in lines:
        m = NOTE_LINE.match(line)
        if m:
            indent, state, rest = m.groups()
            segments = [s.strip() for s in rest.split("\\n")]
            parts: list[str] = []
            for seg in segments:
                if not seg:
                    continue
                parts.append(seg.rstrip(";").strip())
            joined = " · ".join(p for p in parts if p)
            out.append(f"{indent}note right of {state}")
            out.append(f"{indent}    {joined}")
            out.append(f"{indent}end note")
            continue
        if "-->" in line and "\\n" in line:
            line = line.replace("\\n", "<br/>")
        out.append(line)
    return "\n".join(out)


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False

    def repl(m: re.Match[str]) -> str:
        nonlocal changed
        block = m.group(1)
        if not block.strip().startswith("stateDiagram-v2"):
            return m.group(0)
        new_block = fix_state_block(block)
        if new_block != block:
            changed = True
            return "```mermaid\n" + new_block + "```"
        return m.group(0)

    new_text = MERMAID_BLOCK.sub(repl, text)
    if changed:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> None:
    for p in sys.argv[1:]:
        path = Path(p)
        if fix_file(path):
            print(f"updated {path}")
        else:
            print(f"(no changes) {path}")


if __name__ == "__main__":
    main()
