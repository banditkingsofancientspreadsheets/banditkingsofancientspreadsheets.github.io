import os


# Find the path to the project directory
def find_project_root(marker="banditkings"):
    current_dir = os.path.abspath(os.path.dirname(__file__))

    while current_dir != os.path.dirname(current_dir):
        if marker in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)

    raise FileNotFoundError(f"Project root marker '{marker}' not found.")


def data_pathfinder(marker="banditkings"):
    """
    Create a dictionary of paths to directories within a project's data folder,
    excluding the 'archive' directory, where directory names start with two digits.

    Parameters
    ----------
    marker : str, optional
        A marker used to find the project root directory.
        Default is "banditkings".

    Returns
    -------
    dict
        A dictionary where keys are directory names without the numbers
        and underscores, and values are the corresponding paths.
        Includes a key 'project' with the project root directory path.
    """
    paths = {}
    _proj_path = find_project_root(marker=marker)
    paths["project"] = _proj_path
    datapath = os.path.join(_proj_path, "data")
    directories = os.listdir(datapath)

    for dir in directories:
        if dir[:2].isdigit():
            key = dir[3:]
            paths[key] = os.path.join(datapath, dir)

    return paths


if __name__ == "__main__":
    print(data_pathfinder(marker="banditkings"))
