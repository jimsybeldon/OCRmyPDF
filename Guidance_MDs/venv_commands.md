# Python Virtual Environment Commands

This file provides the specific commands to create and activate a Python virtual environment named `.venv` across different command-line shells.

## 1. Create the Virtual Environment

Run this command from your project's root directory.

rm -rf .venv

> **Note:** The command below assumes you want to use your system's default `python` interpreter. If you have multiple Python versions installed and want to create an environment with a specific version (e.g., 3.11), it is more reliable to use the `py` launcher on Windows:
> `py -3.11 -m venv .venv`
> Or on Linux/macOS, specify the version directly:
> `python3.11 -m venv .venv`

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


* xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Python Virtual Environments and Version Mismatches

It sounds like you're running into a common and sometimes confusing situation with Python virtual environments, especially when you have multiple Python versions installed. This guide explains what's happening and how to fix it.

## The Problem

You are trying to create a virtual environment with **Python 3.11**, but the environment that gets created is always **Python 3.13.7**, even though your "global" Python might be a different version (e.g., 3.14).

## Why is this happening?

When you run a command like `python -m venv .venv`, your operating system's command shell (like CMD or PowerShell) looks for an executable named `python.exe` in the directories listed in your system's `PATH` environment variable. It uses the *first one it finds* to create the virtual environment. The new virtual environment will then be a copy of that specific Python version.

The behavior you're seeing indicates that the `python` command is pointing to your Python 3.13.7 installation. This can happen for a few reasons:

* **The `PATH` order:** The directory containing Python 3.13.7 is listed *before* other Python versions in your `PATH` environment variable.
* **IDE Configuration:** If you're using an IDE like VS Code or PyCharm to create the virtual environment, it might be configured to use a specific Python interpreter (in this case, 3.13.7) by default for new workspaces.
* **Shell Alias:** It's less common on Windows, but a shell alias could be redirecting the `python` command.

## How to Create a Virtual Environment with the Correct Version

The most reliable way to create a virtual environment with a specific version of Python is to explicitly tell the system which one to use.

On Windows, you can use the **Python Launcher for Windows (`py.exe`)**, which is the standard way to manage multiple Python installations.

### 1. List Your Installed Python Versions

Open your command prompt (CMD or PowerShell) and run:

```shell
py --list

