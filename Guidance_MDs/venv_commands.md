# Python Virtual Environment Commands

This file provides the specific commands to create and activate a Python virtual environment named `.venv` across different command-line shells.

## 1. Create the Virtual Environment

This command is the same for Bash, CMD, and PowerShell. Run it from your project's root directory.

```bash
python -m venv .venv
```

## 2. Activate the Virtual Environment

The activation command is different for each shell.

### Bash (Linux, macOS, Git Bash on Windows)

```bash
source .venv/scripts/activate
```

### Windows Command Prompt (CMD)

```bat
.\.venv\Scripts\activate.bat
```

### Windows PowerShell (PWSH)

```powershell
.\.venv\Scripts\Activate.ps1
```

> **Note for PowerShell:** If you get a security error about the script not being digitally signed, you may need to adjust the execution policy for your current terminal session by running this command first, then trying the activation command again:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> ```

After successful activation, your terminal prompt should be prefixed with `(.venv)`.
