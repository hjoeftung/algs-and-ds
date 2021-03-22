import shutil
from pathlib import Path


arab_to_roman = {"1": "I", "2": "II", "3": "III",
                 "4": "IV", "5": "V", "6": "VI", "7": "VII"}


def replace_arabic_with_roman(root_dir: Path):
    for directory in root_dir.rglob("[0-9]_*"):
        dir_name = directory.name
        new_dir_name = dir_name.replace(dir_name[0], arab_to_roman[dir_name[0]])
        new_dir_absolute = str(directory.absolute()).replace(
            dir_name, new_dir_name)
        directory.rename(new_dir_absolute)


def remove_non_relevant_files(dir_: Path):
    for directory in dir_.iterdir():
        py_files = directory.rglob("*.py")
        if py_files:
            for file in py_files:
                dest = directory / file.name
                try:
                    shutil.copy(file, dest)
                except shutil.SameFileError:
                    pass

        for subdir in directory.iterdir():
            if subdir.name.startswith("I") or subdir.name.startswith("V"):
                shutil.rmtree(subdir)


if __name__ == '__main__':
    replace_arabic_with_roman(Path.cwd())
    remove_non_relevant_files(Path.cwd() / "algs")
