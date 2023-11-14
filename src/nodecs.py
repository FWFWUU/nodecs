import nodetype

ERROR_INVALID_CHAR = 0
ERROR_NODE_NOT_EXISTS = 1

class NodECS:
	LINE_CREATE_NEW_NODE = 0
	LINE_SET_NODE_META = 1

	def __init__(self):
		self.nodes = []

	@staticmethod
	def _parse_line(base, _line: str, current_node, last_node) -> {}:
		res = {}

		

		return res

	@staticmethod
	def load(filename: str):
		file = open(file=filename)
		lines = file.readlines()

		root = NodECS()

		current_node = None
		last_node = None

		for idx in range(len(lines)):
			_line = lines[idx]

			for i in range(len(_line)):
				_char = _line[i]

				if _char == "[":
					_node_name = ""

					for index_of_name in range(i + 1, len(_line)):
						_char = _line[index_of_name]

						if _char == "\n":
							_node_ = nodetype.NodeType(_node_name)

							if current_node:
								if not last_node:
									last_node = current_node
								
								last_node.add_child(_node_)
							
							current_node = _node_
							root.nodes.append(current_node)	

							break

						if _char == " ":
							return ERROR_INVALID_CHAR

						_node_name += _char
				
				if _char == "]":
					if current_node:
						current_node = None
					else:
						if last_node:
							last_node = None
					
					continue

				if _char == ":":
					if not current_node:
						return ERROR_NODE_NOT_EXISTS
				
					_meta_name = ""
					_meta_type = ""

					renaming = True

					for index_of_meta in range(i + 1, len(_line)):
						_char = _line[index_of_meta]

						if _char == " " or _char == "\t":
							continue
						
						if _char == "@":
							renaming = False
							continue

						if renaming:
							_meta_name += _char
						else:
							if _char == "=":
								_value = ""
								values = []
								_is_str = False

								for index_of_value in range(index_of_meta + 1, len(_line)):
									_char = _line[index_of_value]
									
									if _char == '"':
										if not _is_str:
											_is_str = True
										else:
											_is_str = False
									
									if not _is_str and _char == "," or _char == "\n":
										values.append(_value)
										value = ""
										_is_str = False

									_value += _char

								for index_of_items in range(len(values)):
									_new_value = ""
									is_string = False

									for index_of_item in range(len(values[index_of_items])):
										_char = values[index_of_items][index_of_item]

										if _meta_type == nodetype.NodeType.META_TYPES[nodetype.NodeType.META_STRING]:
											if _char == '"':
												if not is_string:
													is_string = True
													continue
												else:
													values[index_of_items] = _new_value
													break
										
										if is_string == False and not _char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
											continue
										
										_new_value += _char

										if _meta_type == nodetype.NodeType.META_TYPES[nodetype.NodeType.META_NUMBER]:
											if index_of_item == len(values[index_of_items]) - 1:
												values[index_of_items] = float(_new_value)
												
												break
										

								current_node.set_meta(_meta_name, values)

								break
							
							_meta_type += _char

		return root
