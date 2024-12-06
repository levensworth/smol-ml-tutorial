# SMOL ML Tutorial

This repo is meant as a tutorial to cover the basics of putting ML models in production as a service.

## Set-up

We'll use VS Code as our editor and `poetry` as our dependency management.

1. Clone the repo
2. cd to the root of the repository and run the following command from a terminal.
    ```bash
    poetry install
    ```
3. once installed, you should be able to run the API by using this command:
    ```
    fastapi dev src/main.py --app app
    ```
if everything goes well, you can open a browser directed to `http://127.0.0.1:8000/docs` and be grated by a swagger interface.

4. To make it easy for you, try setting up the VS Code debugger. Open or create the file `.vscode/launch.json` and past the following content:

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "FastAPI Debugger",
            "type": "debugpy",
            "request": "launch",
            "module": "fastapi",
            "args": [
                "dev",
                "src/main.py",
                "--port",
                "8000"
            ]
        },
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

you can test the debugger with the IDE built-in debug tab and hitting run.


## Structure:

The repository follows a familiar application folder structure which resembles the `ml-trails` structure ;)

te `src` folder contains the main application code while `data` and `notebooks` will contain non deployable scripts or files which.
 