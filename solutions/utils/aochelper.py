from pathlib import Path

def text_to_string(day):
    return Path(get_input_path(day, ".txt")).read_text()

def get_input_path(day, ext):
    return (f"inputs/day{str(day).zfill(3)}{ext}")

