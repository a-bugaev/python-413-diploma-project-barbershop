"""
zip project for handing it in
"""

import os
import fnmatch
import zipfile

# from pprint import pprint

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

ZIP_PATH = os.path.join(PROJECT_ROOT, "hw_39.zip")


def get_gitignore():
    """
    get list of patters
    """
    with open("./.gitignore", "r", encoding="utf-8") as f:
        text = f.read()
    return text.split("\n")


PATTERNS_GITIGNORE = get_gitignore()

PATTERS_TO_EXCLUDE_FROM_GITIGNORE = ["notes.txt", "gitrepo.txt"]

PATTERNS_TO_ADD_TO_GITIGNORE = [
    ".git",
    "PYTHON413 HW №39.md",
    ".vscode" "test",
    ".djlint*",
    "zip.py",
]

FINAL_PATTERNS = [
    x for x in PATTERNS_GITIGNORE if x not in PATTERS_TO_EXCLUDE_FROM_GITIGNORE
] + PATTERNS_TO_ADD_TO_GITIGNORE


def parse_gitignore():
    """
    filters project through gitignore
    returns list of relative to project root paths to passed files
    """

    for root, dirs, files in os.walk(PROJECT_ROOT):
        # override os.walk context to filter dirs to prevent yielding gitignored content farther
        dirs[:] = [
            d for d in dirs if not any(fnmatch.fnmatch(d, pattern) for pattern in FINAL_PATTERNS)
        ]
        # yield rel filepath if it mot matches with any pattern
        for file in files:
            if not any(fnmatch.fnmatch(file, pattern) for pattern in FINAL_PATTERNS):
                yield os.path.join(root, file)


def get_abs_paths(items):
    """
    get list of absolute paths from project root
    """
    return [os.path.join(PROJECT_ROOT, item) for item in items]


REL_PATHS_TO_ZIP_GEN = parse_gitignore()
PATHS_TO_ZIPPING = get_abs_paths([i for i in REL_PATHS_TO_ZIP_GEN])


def zip_list_of_paths(paths_to_zip, output_filename):
    """
    Zips filtered project
    """
    with zipfile.ZipFile(output_filename, "w") as zip_file:
        for file in paths_to_zip:
            rel_path = os.path.relpath(file, PROJECT_ROOT)
            zip_file.write(file, rel_path)


zip_list_of_paths(PATHS_TO_ZIPPING, ZIP_PATH)
# pprint(PATHS_TO_ZIPPING)
