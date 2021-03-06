## Yolo v3 demo image classification

### Task 5 instructions

#### Web demo
In folder yolo_demo, you can find `web.py` script, which contains web demo.
To run, install package (use local version from `dist` directory)
and then use command `streamlit run web.py` in folder `yolo_demo`.
Streamlit app will work at `localhost:8501`.

You can choose jpg image from your own or use mine from
`yolo_demo/data/cat.jpg`

#### Docker build
To create docker image, install Docker to your system. Then use the command:

`docker build -t yolo ./`

After building, use command 

`docker run -p 8501:8501 yolo`

and you'll see web demo at `localhost:8501`
### Task 4 instructions
In this task. I add tests: regression test and test for big and small images.

To run tests, use this command:

```python -m pytest```

To check CI part of the task, follow the link:

https://github.com/AngryFennec/ml-cv/actions

CI check flake, pytest and then make build and push it to the Artifacts.

To check artifacts, select job in Actions, for example:

https://github.com/AngryFennec/ml-cv/actions/runs/2247140778

In the bottom you can see Artifacts and download package:

![img.png](img.png)


### Task 3 instructions
In this task, I add some styling tools (`flake8` and `black`).
Also, `pre-commit` tool for using styling tools during commit.
Just run `poetry install` to install all requirements.

Configs are in `pyproject.toml` and in `.pre-commit-config.yaml`

To check, you can make some changes, then type 

```git add -A```

```git commit -m "some changes"```

and watch, how these tools are work. If there are some errors in the project - `black` tool
automatically fix them, and `flake8` tool print error log in console.
After fixing errors, you need to make git commands again.

To check file before commit, use commands:

```black demo.py```

```flake8 demo.py```


### Task 2 instructions

#### Building package
1. If you don't have `build` package - firstly, let's install it. Just use `python3 -m pip install build` on Unix/Max or `python -m pip install build` on Windows
2. Run build command: `python3 -m build` on Unix/Max or `python -m build` on Windows
3. The `dist` folder appears, there are two package files inside: `.tar.gz` and `.wheel`
4. Switch to `dist` folder with `cd dist`
5. Use command `pip install yolo_demo-0.11.0.tar.gz` to install package
6. After installation, you can use command `yolo_demo` in console to watch demo OR change directory to `yolo_demo` and run `python demo.py`

#### Install from git
Use command `pip install git+https://github.com/AngryFennec/ml-cv.git@task2`

### Task 1 instructions (not actual right now)

Virtual environment created using poetry

To run, follow these steps:
1. switch to `yolo-demo` directory: `cd yolo-demo`
2. install dependencies using poetry: `poetry install`. If you don't have poetry on your system, you'll need to install it first with this doc: https://python-poetry.org/docs/#installation. During my work, I also installed pyenv to switch global python version.
3. switch to `yolo_demo` directory: `cd yolo_demo`
4. use `poetry shell` to run shell
5. inside the shell, run `python demo.py` on Windows or `python3 demo.py` on nix systems

After these steps, you'll see cat image with detected and classified cat

To leave poetry shell, use `exit` command.
