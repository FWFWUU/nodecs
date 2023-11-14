import sys
sys.path.append('./src/')
sys.path.append('./tests/')

from nodecs import NodECS

root = NodECS.load("tests/examples.necs")

for child in root.nodes:
	print(child.name)
	print("\t", child.meta)

	if child.parent:
		print("\tParent::", child.parent.name)