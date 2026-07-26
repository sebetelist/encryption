from pathlib import Path
from itertools import count

def get_unique_file(base_name, extension):
    folder = "files"
    if not Path(folder).exists():
        Path(folder).mkdir(parents=True, exist_ok=True)

    counter = count(1)
    while True:
        num = next(counter)
        file_path = Path(folder) / f"{base_name}-{num}{extension}"

        if not file_path.exists():
            return file_path
  






