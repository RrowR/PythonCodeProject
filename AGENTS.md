# PROJECT KNOWLEDGE BASE

**Generated:** 2026-06-10
**Commit:** dd498b5
**Branch:** master

## OVERVIEW

31-day Python learning course. Standalone scripts per day covering basics → OOP → file I/O (Excel/Word/PDF) → image processing → standard library. Python 3.14, no packaging.

## STRUCTURE

```
./
├── 001_day/    # Basics: I/O, variables, strings, arrays
├── 002_day/    # Control flow: conditionals, loops, dicts
├── 003-009/    # Intermediate basics
├── 010_day/    # Tuples
├── 011-016/    # Functions (basic → advanced)
├── 017-019/    # OOP foundations
├── 020_day/    # OOP application (wage system)
├── 021-023/    # JSON, file I/O
├── 024_day/    # Excel (openpyxl): read/write/format
├── 025_day/    # More file operations
├── 026_day/    # Word docs (python-docx): templates, generation
├── 027_day/    # PDF (PyPDF2/ReportLab): create, watermark, encrypt
│   └── fonts/  # CJK fonts for PDF rendering
├── 028_day/    # Pillow: image processing & drawing
├── 029_day/    # SMS sending (API integration)
├── 030_day/    # Network/concurrency
└── 031_day/    # Stdlib deep dive: heapq, itertools, collections
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Python basics (variables, types, I/O) | `001_day/`, `002_day/` | 14 files each, most content |
| Control flow & operators | `002_day/`, `005_day/` | Conditionals, loops, match-case |
| Functions | `011-016_day/` | 1 file per day, progressive |
| OOP | `017-020_day/` | Capstone: `020_day/工资结算系统.py` |
| Excel manipulation | `024_day/` | openpyxl, read/write/format, .xls data files |
| Word document generation | `026_day/` | python-docx, templates, mail-merge style |
| PDF operations | `027_day/` | Create, watermark, encrypt, extract text |
| Image processing | `028_day/` | Pillow, has .png test data |
| SMS / API integration | `029_day/` | Uses `if __name__ == '__main__'` guard |
| Stdlib advanced | `031_day/` | heapq, itertools, collections |
| Test example | `005_day/testedCodes/` | Only test-like file in project |

## CONVENTIONS

- **Chinese filenames**: ~90% of `.py` files use Chinese names (e.g., `变量和类型.py`). Not importable as Python modules due to non-ASCII paths.
- **Standalone scripts**: No `__init__.py` anywhere. Every file runs independently. No inter-module imports.
- **No `if __name__ == '__main__'`**: Only 2/115 files use this guard (`027_day/`, `029_day/`). All others execute at import time.
- **Data files mixed with code**: `.xls`, `.xlsx`, `.docx`, `.pdf`, `.png`, `.jpg`, `.csv`, `.json` files sit alongside `.py` scripts in day dirs.
- **No packaging**: No `pyproject.toml`, `setup.py`, `requirements.txt`, or dependency manifest. Third-party deps (openpyxl, python-docx, PyPDF2, Pillow) are implicit.

## ANTI-PATTERNS (THIS PROJECT)

- **No `__main__` guard on 113/115 scripts** — running `import` on any non-guarded file executes everything
- **`.idea/` not gitignored** — `.gitignore` line 163 has `#.idea/` commented out; IDE config not excluded from tracking
- **Non-ASCII filenames** — cannot `import` these as Python modules; breaks some tooling
- **Data blobs in git** — `.docx`, `.pdf`, `.xls` binary files committed; bloats repo history

## COMMANDS

```bash
# Run any day's script directly
python 001_day/helloworld.py
python 024_day/读Excel文件.py

# No test/build/install/lint commands exist
```

## NOTES

- Day numbering is sequential (001-031) following a course curriculum, not module boundaries
- Files increase in complexity: days 1-9 = basics, 10-23 = intermediate, 24-31 = practical applications
- `005_day/testedCodes/TestMyCode.py` is the only test-adjacent file
- `027_day/fonts/` contains CJK font files needed for PDF generation
- No CI/CD, no linter, no formatter, no type checker configured
