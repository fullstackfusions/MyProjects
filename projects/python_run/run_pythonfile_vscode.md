using `launch.json` from .vscode

### example `launch.json` for normal file:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "cwd": "${workspaceFolder}",
      "python": "${workspaceFolder}/venv/bin/python",
      "envFile": "${workspaceFolder}/.env",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/src"
      },
      "jinja": true,
      "justMyCode": false
    }
  ]
}
```

### example `launch.json` for module:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Module",
      "type": "debugpy",
      "request": "launch",
      "module": "app", // app is assumed that your code scripts and __main__.py are resides in app directory
      "cwd": "${workspaceFolder}",
      "python": "${workspaceFolder}/venv/bin/python",
      "envFile": "${workspaceFolder}/.env",
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
        // if you don't define PYTHONPATH then default value would be cwd
      },
      "args": ["argument 1", "argument 2"],
      "jinja": true,
      "justMyCode": false
    }
  ]
}
```

### example `launch.json` for fastapi:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "cwd": "${workspaceFolder}",
      "python": "${workspaceFolder}/venv/bin/python",
      "envFile": "${workspaceFolder}/.env",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/src"
      },
      "args": ["main:app", "--reload"],
      "jinja": true,
      "justMyCode": false
    }
  ]
}
```

### example `launch.json` for PYTEST:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: PYTEST",
      "type": "debugpy",
      "request": "launch",
      "module": "pytest",
      "cwd": "${workspaceFolder}",
      "python": "${workspaceFolder}/venv/bin/python",
      "envFile": "${workspaceFolder}/.test-env",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/src"
      },
      "args": ["tests/unit"],
      "jinja": true,
      "justMyCode": false
    }
  ]
}
```

### example `launch.json` for Docker Debug from vscode:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Docker Debug",
      "type": "docker",
      "request": "launch",
      "preLaunchTask": "some prelauch task name", // match this name from taks.json file
      "python": "${workspaceFolder}/venv/bin/python",
      "pathMappings": [
        {
          "remoteRoot": "/app/src/module-1/",
          "localRoot": "${workspaceFolder}/src/module-1"
        },
        {
          "remoteRoot": "/app/src/module-2/",
          "localRoot": "${workspaceFolder}/src/module-2"
        }
      ],
      "jinja": true,
      "justMyCode": false
    }
  ]
}
```

### example `tasks.json` for Docker Debug from vscode:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "docker-run",
      "label": "some prelauch task name", // this should match in launch.json
      "dependsOn": ["docker-build"],
      "dockerRun": {
        "containerName": "module-1-debug",
        "image": "module-1:latest",
        "volumes": [
          {
            "containerPath": "/app",
            "localPath": "${workspaceFolder}/"
          }
        ],
        "envFiles": [
          ".env",
          ".env.module1" // assuming there's other env file specific to module1
        ],
        "env": {
          "SOME_ENV_VARIABLE": "ENV_VALUE"
        },
        "ports": [
          {
            "containerPort": 7272,
            "hostPort": 7272,
            "protocol": "tcp"
          }
        ],
        "remove": true
      },
      "options": {
        "cwd": "${workspaceFolder}"
      },
      "python": {
        "module": "module-1"
      }
    },
    {
      "label": "docker-build",
      "type": "docker-build",
      "dockerBuild": {
        "platform": "linux/x86_64",
        "pull": true,
        "context": "${workspaceFolder}",
        "dockerfile": "${workspaceFolder}/Dockerfile",
        "buildArgs": {
          "USERNAME": "${USERNAME}",
          "PASSWORD": "${PASSWORD}"
        } // Assuming that build arguments are username and password and required inside Dockerfile
      }
    }
  ]
}
```
