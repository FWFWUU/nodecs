# NodECS

## Structure data with more weight!

### Workflow
- [< Name >[Parent]
- - - :< Name >[Meta] @ < String >[type] = {value, [...]}
- - [< Name >[Child]]
- ]

```js
[Human
	:Name @ String = "Test"
	:Age @ Number = 0
	
	[Child
		:Name@String = "Junior"
		:Debuffs@String = "1", "2", "3"
		]
	]

[Mesh
	:Name@String = "Mesh Name"
	
	[Surface
		:Vertices@String = "0,0,0", "0,1,0", "1,1,0", "0,0,1"
		:Name@String = "CubeSurface"
		]
	]

```

```python
import nodecs.NodECS
root = NodECS.load("tests/examples.necs")

for child in root.nodes:
	print(child.name)
	print("\t", child.meta)

	if child.parent:
		print("\tParent::", child.parent.name)

```

Preview:

```
Human
         {'Name': ['Test'], 'Age': [0.0]}
Child
         {'Name': ['Junior'], 'Debuffs': ['1', '1', '1']}
        Parent:: Human
Mesh
         {'Name': ['Mesh Name']}
Surface
         {'Vertices': ['0,0,0', '0,0,0', '0,0,0', '0,0,0'], 'Name': ['CubeSurface']}
        Parent:: Mesh
```
