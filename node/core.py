from koi_net import NodeInterface
from .config import MyNodeConfig

node = NodeInterface(
    config=MyNodeConfig.load_from_yaml("config.yaml"),
    use_kobj_processor_thread=True
)

from . import handlers