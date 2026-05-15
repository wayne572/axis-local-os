# GitHub Setup For Axis Local OS

Status: setup helper
Date: 2026-05-15

## Recommended Repository Setting

Create the GitHub repository as **private**.

This workspace contains business strategy, client delivery material, governance notes, and system memory files. Do not make it public unless a separate public-safe version is created.

## Local Repository

Run from:

```powershell
D:\Axis AI - ChatGPT OS\AXIS_OS_CODEX_CURRENT
```

Useful commands:

```powershell
git status
git add .
git commit -m "Initial Axis Local OS foundation"
```

## GitHub Web Setup

1. Go to `https://github.com`.
2. Sign in or create an account.
3. Create a new repository.
4. Name it `axis-local-os`.
5. Set visibility to **Private**.
6. Do not add a README, license, or `.gitignore` on GitHub because this folder already has them.
7. Copy the repository URL.

Then connect this local folder:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/axis-local-os.git
git branch -M main
git push -u origin main
```

## GitHub CLI Option

If GitHub CLI is installed later:

```powershell
gh auth login
gh repo create axis-local-os --private --source . --remote origin --push
```

## Safety Rules

- Keep the main repository private.
- Do not commit `.kb/` or `.axis/` runtime state.
- Do not commit `.env` files or keys.
- Treat PDFs and ZIP exports as generated delivery artifacts unless there is a clear reason to version them.
- Use a separate public repo later for sanitized examples, marketing material, or open-source code.

