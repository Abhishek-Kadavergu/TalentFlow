from pathlib import Path

ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".java",
    ".md",
    ".json",
}

IGNORE_FOLDERS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    "venv",
}


def load_repository(repo_path: str) -> str:
    content = []
    print("started")

    for file in Path(repo_path).rglob("*"):

        if any(folder in file.parts for folder in IGNORE_FOLDERS):
            continue

        if file.is_file() and file.suffix in ALLOWED_EXTENSIONS:

            try:
                text = file.read_text(encoding="utf-8")

                content.append(
                    f"\n\n===== FILE: {file.relative_to(repo_path)} =====\n{text}"
                )

            except:
                pass


    return "\n".join(content)