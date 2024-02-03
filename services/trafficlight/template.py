import os
from pathlib import Path
from typing import List


def create_directory(filepath: Path) -> None:
    """
    Create directory if not exists
    :param filepath: the path of the file
    :return:
    """
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)


def create_file(filepath: Path) -> None:
    """
    Create file if not exists
    :param filepath: the path of the file
    :return:
    """
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass


def create_project_structure(list_of_files: List[str]) -> None:
    """
    Create project structure
    :param list_of_files: list of files to be created
    :return:
    """
    for filepath in list_of_files:
        filepath = Path(filepath)
        create_directory(filepath)
        create_file(filepath)


if __name__ == '__main__':
    project_name = "src"

    list_of_files = [
        f'.github/workflows/main.yaml',
        f'config/config.yaml',
        f'config/config.ini',
        f'{project_name}/__init__.py',
        f'{project_name}/api/__init__.py',
        f'{project_name}/entity/__init__.py',
        f'{project_name}/pipeline/__init__.py',
        f'{project_name}/services/__init__.py',
        f'{project_name}/utils/__init__.py',
        'logs/log_details.log',
        'notebooks/notebook.ipynb',
        'reports/reports.pdf',
        '.gitignore',
        'params.yaml',
        'test.py',
        'Dockerfile',
        'template.py',
        'requirements.txt',
        'setup.py',
        'main.py',
        'README.md',
    ]
    create_project_structure(list_of_files)
