# Windows File System Dynamic Analysis

A lightweight Python tool to monitor a directory in real-time, detecting newly created and deleted files or folders.

---

## Features

- Real-time directory monitoring
- Detects created files and directories
- Detects deleted files and directories
- Recursive tracking (monitors all subfolders)
- Zero external dependencies (uses Python standard libraries)

---

## Requirements

- Python 3.8 or higher
- Windows (also compatible with Linux / macOS)

---

## Usage

1. Run the script:
```bash
python WindowsFileSystemDynamicAnalysis.py
```

2. Enter the path of the directory you want to monitor:
```text
Enter the path to analyze: C:\Users\Username\TargetFolder
```

3. Any file activity inside the directory will be printed in real time:
```text
[+] New File: test.txt
[+] New Folder: Logs
[-] Deleted: test.txt
```

---

## Contact

- Dev: Lunair
- Discord: `7vmr`
- Website: https://lunair.fun
