"""
csfs

A module to detect case-sensitive file systems.

MIT License

Copyright (c) 2024 - Divine Afam-Ifediogor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = "0.1.0"

from tempfile import TemporaryDirectory
from pathlib import Path
from os import listdir
from functools import lru_cache


@lru_cache
def is_filesystem_case_sensitive():
    """
    Determine if the current file system is case-sensitive.

    :rtype: bool
    :return: True if the current file system is case-sensitive, False otherwise.
    """
    with TemporaryDirectory(prefix="csfs_") as _temp_dir:
        temp_dir = Path(_temp_dir)
        (temp_dir / "a").touch()
        (temp_dir / "A").touch()
        return len(listdir(temp_dir)) == 2


if __name__ == "__main__":
    if is_filesystem_case_sensitive():
        print("This filesystem is case-sensitive.")
    else:
        print("This filesystem is case-insensitive.")
