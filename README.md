# csfs

`csfs` is a Python module to detect whether the current file system is case-sensitive. This can be useful for developers working with file systems where case sensitivity might affect application behavior or file management.

## Features

- Simple and lightweight.
- Determines case sensitivity by creating and analyzing temporary files.
- Returns a boolean result indicating the file system’s case sensitivity.

## Installation

`csfs` is a standalone Python script. You can download or copy the code from the repository to your project.

It will be published on PyPi soon.

## Usage

Import and use the `is_filesystem_case_sensitive` function in your Python code:

```python
from csfs import is_filesystem_case_sensitive

if is_filesystem_case_sensitive():
    print("This filesystem is case-sensitive.")
else:
    print("This filesystem is case-insensitive.")
```

Or execute the script directly to display the result:

```bash
python csfs.py
```

### Output:

- **Case-sensitive filesystems:**
  ```
  This filesystem is case-sensitive.
  ```

- **Case-insensitive filesystems:**
  ```
  This filesystem is case-insensitive.
  ```

## How It Works

The function `is_filesystem_case_sensitive`:

1. Creates a temporary directory.
2. Writes two files to the directory: one named `a` and the other named `A`.
3. Checks the directory listing:
   - If both files exist, the file system is case-sensitive.
   - If only one file exists, the file system is case-insensitive.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

## Author

Developed by Divine Afam-Ifediogor.  
Copyright (c) 2024.

