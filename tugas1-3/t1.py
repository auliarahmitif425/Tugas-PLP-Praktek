import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

potongan = {
    "fungsi": b"def sapa(nama):\n    return nama\n",
    "if/else": b"if x > 0:\n    y = 1\nelse:\n    y = 2\n",
    "kelas": b"class Kucing:\n    def mengeong(self):\n        return 'meong'\n",
    "rusak (tanpa :)": b"def sapa(nama)\n    return nama\n",
}

for nama, kode in potongan.items():
    tree = parser.parse(kode)
    print("==", nama)
    print(tree.root_node)
    print("has_error =", tree.root_node.has_error)

    print("anak langsung node pertama:")
    for c in tree.root_node.children[0].children:
        print(" ", c.type, "bernama" if c.is_named else "anonim")
    print()