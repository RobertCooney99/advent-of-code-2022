from pathlib import Path

def txtToString(day):
    return Path(getInputPath(day, ".txt")).read_text()

def getInputPath(day, ext):
    return (f"inputs/day{str(day).zfill(3)}{ext}")

