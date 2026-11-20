import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

kode = open(sys.argv[1], "rb").read()
pola = open(sys.argv[2]).read()
mode = sys.argv[3] if len(sys.argv) > 3 else "captures"
tree = parser.parse(kode)
cursor = QueryCursor(Query(PY, pola))

if mode == "matches":
    for _, cap in cursor.matches(tree.root_node):
        nama = cap["nama"][0].text.decode()
        params = cap.get("params", [])
        jumlah = params[0].named_child_count if params else 0
        print(f"{nama}  ({jumlah} parameter)")
else:
    for nama, nodes in cursor.captures(tree.root_node).items():
        for n in nodes:
            print(f"@{nama}  baris {n.start_point[0] + 1}: {n.text.decode()}")