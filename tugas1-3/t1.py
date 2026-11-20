import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

kode = b"if x > 0:\n    y = 1\nelse:\n    y = 2\n"
tree = parser.parse(kode)
print(tree.root_node)