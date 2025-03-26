# Creating Python virtual environment

1. Install virtualenv (considering it isn't already installed).
```
pip install virtualenv
```

2. Create the Virtual Environment
```
python -m venv my_env
```

venv is a built-in Python tool for creating and managing virtual environments.

In order to create the virtual environment you should run the previous command inside the directory where is your current project.

3. Activate the environment
```
cd env/Scripts
./activate
```

After activating the environment you're ready to install the Manim library and run it inside your project.

4. Install dependences
```
cd ..
pip install manim
```

5. Check dependences installation
```
pip freeze
```

6. Select Python Interpreter (For VSCode users)
```
Press Ctr+Shift+P
Search for >Python Interpreter
Select Python3.XX.X ('env': venv) .\env\Scripts\python.exe
```

7. Installing ffmpeg (For Windows users)

Open the CMD and run:
```
iwr -useb get.scoop.sh | iex
```

After installing Scoop, it is time to install ffmpeg
```
scoop install ffmpeg
```

8. Install MiKTeX

Open the CMD and run:
```
scoop install miktex
```

Verify miktex version before proceding by running:
```
miktex --version
```

8. Rendering Animation With Manim

```
manim -pqh file_name.py DirName
```

After running the command, a directory called "DirName" should be created containing a mp4 file with the rendered result.
