import sys
from pathlib import Path
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

BATAS_BARIS = 30
SKIP = {"venv", ".venv", ".git", "node_modules", "__pycache__"}

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')
Q_FUNC = Query(PY, "(function_definition name: (identifier) @nama) @fungsi")


def cari_error(node):
    """Cari node ERROR/MISSING paling awal (DFS, urut sesuai posisi)."""
    if node.is_error or node.is_missing:
        return node
    for anak in node.children:
        if anak.has_error or anak.is_missing:
            hasil = cari_error(anak)
            if hasil is not None:
                return hasil
    return None


def cek_file(path):
    tree = parser.parse(path.read_bytes())
    root = tree.root_node

    # Fitur 1: komentar TODO/FIXME
    for node in QueryCursor(Q_TODO).captures(root).get("c", []):
        teks = node.text.decode(errors="replace").strip()
        print(f"{path}:{node.start_point[0] + 1}: {teks}")

    # Fitur 2: fungsi lebih dari 30 baris
    for _, cap in QueryCursor(Q_FUNC).matches(root):
        fungsi = cap["fungsi"][0]
        nama = cap["nama"][0].text.decode(errors="replace")
        baris = fungsi.end_point[0] - fungsi.start_point[0] + 1
        if baris > BATAS_BARIS:
            print(f"{path}:{fungsi.start_point[0] + 1}: fungsi {nama} panjang ({baris} baris)")

    # Fitur 3: file yang pohonnya mengandung error
    if root.has_error:
        err = cari_error(root)
        if err is not None:
            jenis = "MISSING" if err.is_missing else "ERROR"
            print(f"{path}:{err.start_point[0] + 1}: sintaks bermasalah ({jenis})")
        else:
            print(f"{path}: sintaks bermasalah")


if len(sys.argv) != 2:
    sys.exit("Pemakaian: python cek.py <folder>")

for path in sorted(Path(sys.argv[1]).rglob("*.py")):
    if SKIP & set(path.parts):
        continue
    cek_file(path)
