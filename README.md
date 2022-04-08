## Yolo v3 demo image classification

### Task 2 instructions

#### Building package
0. Remove `dist` folder, if you want to check my work fully. Or you just can use my build and start from step 5
1. If you don't have `build` package - firstly, let's install it. Just use `python3 -m pip install build` on Unix/Max or `python -m pip install build` on Windows
2. Change directory to yolo-demo: `cd yolo-demo`
3. Run build command: `python 3 -m build` on Unix/Max or `python -m build` on Windows
4. The `dist` folder appears, there are two package files inside: `.tar.gz` and `.wheel`
5. Switch to `dist` folder with `cd dist`
6. Use command `pip install yolo_demo-0.1.0.tar.gz` to install package
7. After installation, you can use command `yolo-demo` in console to watch demo

#### Install from git
Use command `pip install git+https://github.com/AngryFennec/ml-cv.git@0.11.0`

Or check `https://github.com/AngryFennec/ml-cv/tags` tags list and use custom tag number in the command above

### Task 1 instructions

Virtual environment created using poetry

To run, follow these steps:
1. switch to `yolo-demo` directory: `cd yolo-demo`
2. install dependencies using poetry: `poetry install`. If you don't have poetry on your system, you'll need to install it first with this doc: https://python-poetry.org/docs/#installation. During my work, I also installed pyenv to switch global python version.
3. switch to `yolo_demo` directory: `cd yolo_demo`
4. use `poetry shell` to run shell
5. inside the shell, run `python demo.py` on Windows or `python3 demo.py` on nix systems

After these steps, you'll see cat image with detected and classified cat

To leave poetry shell, use `exit` command.