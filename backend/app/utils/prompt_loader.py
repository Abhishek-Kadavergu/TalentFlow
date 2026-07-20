from pathlib import Path


PROMPT_DIR = Path("app/prompts")


def load_prompt(filename: str) -> str:
    path = PROMPT_DIR / filename
    return path.read_text(encoding="utf-8")