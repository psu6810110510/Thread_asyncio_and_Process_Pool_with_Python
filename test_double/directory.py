import pathlib


def create_directory(name=1):
    """
    xxx
    """
    path = pathlib.Path(name)
    if not check_directory(path):
        path.mkdir(parents=True)

    return path


def check_directory(path):
    return path.exists()


if __name__ == "__main__":
    dir_name = "test/new"
    path = create_directory(dir_name)
    print(f"file -> {dir_name} is {path}")

    result = check_directory(path)
    print(f"diretory -> {path} is {result}")
