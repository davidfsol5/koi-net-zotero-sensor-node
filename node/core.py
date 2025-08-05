from koi_net import NodeInterface
from .config import ZoteroSensorNodeConfig

node = NodeInterface(
    config=ZoteroSensorNodeConfig.load_from_yaml("config.yaml"),
    use_kobj_processor_thread=True
)

from . import handlers