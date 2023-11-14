class NodeType:
	META_STRING = 0
	META_NUMBER = 1

	META_TYPES = [
		"String", "Number"
	]

	def __init__(self, name: str = "GenericNodeType_T", parent = None) -> None:
		self.name = name
		
		self.parent = parent
		self.childs = []
		self.meta = {}
	
	def add_child(self, node):
		if not node in self.childs:
			node.parent = self

			self.childs.append(node)
	
	def set_meta(self, meta_name: str, _value: any) -> None:
		self.meta[meta_name] = _value
	
	def get_meta(self, meta_name: str) -> any:
		return self.meta[meta_name] if meta_name in self.meta else "Invalid"
