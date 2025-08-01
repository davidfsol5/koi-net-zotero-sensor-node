# MyElligot's Pond Development Notebook

## Work plan for Version 1
1. Design/Create Zotero sensor node
3. Create MIME-to-text mutation node
4. Create text chunker decomposition node
5. Create chunk embedder composition node
6. Design internal world model sub net

## Process followed to create Zotero sensor node

(2025-07-30) Process is modified from BlockScience koi-net-node-template to work on my dev machine (DFS03).

### Created davidfsol5/koi-net-zotero-sensor-node repo from  BlockScience koi-net-node-template repo using github.com web UI's "Use this template" button.

### Cloned remote davidfsol5/koi-net-zotero-sensor-node repo to my local development machine, DFS03, from a PowerShell command line.

```
PS %UserProfile%\Code> git clone https://github.com/davidfsol5/koi-net-zotero-sensor-node.git
```

### Set up Virtual Environment in clone folder from command line.

```
PS %UserProfile%\Code> cd koi-net-zotero-sensor-node
PS %UserProfile%\Code\koi-net-zotero-sensor-node> python -m venv .venv
```

Modified from koi-net-node-template readme. I had to explicitly pass the ENV_DIR parameter for Windows venv module. Without it, I received the following error message:

```
PS %UserProfile%\Code\koi-net-zotero-sensor-node> python -m venv
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear] [--upgrade] [--without-pip]
            [--prompt PROMPT] [--upgrade-deps]
            ENV_DIR [ENV_DIR ...]
venv: error: the following arguments are required: ENV_DIR
```

### Activate Virtual Environment in clone folder from command line.

```
PS %UserProfile%\Code> .venv\Scripts\activate
```

### Install dependencies into Virtual Environment

```
(.venv) PS %UserProfile%\Code\koi-net-zotero-sensor-node> pip install -r requirements.txt
```

### Run server node [to test installation]

```
(.venv) PS %UserProfile%\Code\koi-net-zotero-sensor-node> python -m node
INFO:     Started server process [24620]
INFO:     Waiting for application startup.
2025-07-30 13:47:38 INFO     koi_net.core - Starting processor worker thread                              core.py:74
                    INFO    Koi_net.processor.interface - Writing to cache: <KObj                      interface.py:207
                            'orn:koi-net.node:my-node-name+946990e2-4474-4473-b64e-121c750241fb' event
                            type: 'None' -> 'NEW', source: 'INTERNAL'>
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
Pressed CTRL+C

```
INFO:     Shutting down
INFO:     Waiting for application shutdown.
2025-07-30 13:49:12 INFO     koi_net.core - Stopping node...                                                 core.py:118
                    INFO     koi_net.core - Waiting for kobj queue to empty (0 tasks remaining)              core.py:121
INFO:     Application shutdown complete.
INFO:     Finished server process [24620]
```

## Branded raw template clone repo for koi-net-zotero-sensor-node
