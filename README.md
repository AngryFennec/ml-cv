## Yolo v3 demo image classification

Virtual environment created using poetry

To run, follow these steps:
1. switch to `yolo-demo` directory: `cd yolo-demo`
2. install dependencies using poetry: `poetry install`. If you don't have poetry on your system, you'll need to install it first with this doc: https://python-poetry.org/docs/#installation. During my work, I also installed pyenv to switch global python version.
3. use `poetry shell` to run shell
4. inside the shell, run `python demo.py` on Windows or `python3 demo.py` on nix systems

After these steps, you'll see cat image with detected and classified cat

To leave poetry shell, use `exit` command.