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
    