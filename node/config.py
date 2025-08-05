from pydantic import Field
from koi_net.config import NodeConfig, KoiNetConfig
from koi_net.protocol.node import NodeProfile, NodeProvides, NodeType

class ZoteroSensorNodeConfig(NodeConfig):
    koi_net: KoiNetConfig | None = Field(default_factory = lambda:
        KoiNetConfig(
            node_name="myelligots-pond-zotero-sensor",   # human readable name for your node
            node_profile=NodeProfile(
                node_type=NodeType.FULL,
                provides=NodeProvides(
                    event=[],   # RID types of provided events
                    state=[]    # RID types of provided state
                )
            )
        )
    )