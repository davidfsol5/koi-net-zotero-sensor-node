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

```bash
PS %UserProfile%\Code> git clone https://github.com/davidfsol5/koi-net-zotero-sensor-node.git
```

### Set up Virtual Environment in clone folder from command line.

```bash
PS %UserProfile%\Code> cd koi-net-zotero-sensor-node
PS %UserProfile%\Code\koi-net-zotero-sensor-node> python -m venv .venv
```

Modified from koi-net-node-template readme. I had to explicitly pass the ENV_DIR parameter for Windows venv module. Without it, I received the following error message:

```bash
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

```bash
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

```bash
INFO:     Shutting down
INFO:     Waiting for application shutdown.
2025-07-30 13:49:12 INFO     koi_net.core - Stopping node...                                                 core.py:118
                    INFO     koi_net.core - Waiting for kobj queue to empty (0 tasks remaining)              core.py:121
INFO:     Application shutdown complete.
INFO:     Finished server process [24620]
```

Resulting config.yaml file:

```yaml
server:
  host: 127.0.0.1
  port: 8000
  path: /koi-net
koi_net:
  node_name: my-node-name
  node_rid: orn:koi-net.node:my-node-name+946990e2-4474-4473-b64e-121c750241fb
  node_profile:
    base_url: http://127.0.0.1:8000/koi-net
    node_type: FULL
    provides:
      event: []
      state: []
  cache_directory_path: .rid_cache
  event_queues_path: event_queues.json
  first_contact:
```

## Branded raw template clone repo for koi-net-zotero-sensor-node

### 1. Create rid_type classes in rid_types.py

orn:zotero.citable_item:<zotero_library>/<item_id>

- Manifest includes citation metadata
- Bundle includes publication if locally available

```python
from rid_lib.core import ORN

class ZoteroCitableItem(ORN):
    namespace = "zotero.citable_item"
    
    def __init__(self, item_id: str):
        self.item_id = item_id
        
    @property
    def reference(self):
        return self.item_id
    
    @classmethod
    def from_reference(cls, reference):
        return cls(reference)    
```

### 2. Edit config.py

1. Rename ```class MyNodeConfig``` to ```class ZoteroSensorNodeConfig```
2. Change class property ```node_name``` value from ```"my-node-name"``` to ```"myelligots-pond-zotero-sensor"```
3. Keep class property ```node_type``` value as ```"FULL"```

---

## Deadends

### Edit config.yaml (Deprecated from branding section 2025-08-05 in favor of editing config.py)

1. Change ```koi_net/node_name``` from ```my-node-name``` to ```koi-net-zotero-node-sensor```
2. Delete ```koi_net/node_rid```
3. Rerun server node to generate new unique ```node_rid```

Resulting config.yaml file:

```
server:
  host: 127.0.0.1
  port: 8000
  path: /koi-net
koi_net:
  node_name: koi-net-zotero-sensor-node
  node_rid: 
    orn:koi-net.node:koi-net-zotero-sensor-node+986fc686-fe42-40c8-854f-976e86e62fc9
  node_profile:
    base_url: http://127.0.0.1:8000/koi-net
    node_type: FULL
    provides:
      event: []
      state: []
  cache_directory_path: .rid_cache
  event_queues_path: event_queues.json
  first_contact:
```
