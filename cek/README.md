# cek.py

CLI kecil untuk memeriksa file Python dengan tree-sitter.

## Fitur

1. Melaporkan komentar yang berisi `TODO` atau `FIXME` beserta file dan barisnya.
2. Melaporkan fungsi yang panjangnya lebih dari 30 baris. Semua fungsi dihitung,
   termasuk method di dalam kelas dan fungsi bersarang.
3. Melaporkan file yang pohonnya mengandung error sintaks, beserta baris
   pertama yang bermasalah.

Folder `venv/`, `.venv/`, `.git/`, `node_modules/`, dan `__pycache__/` dilewati.

## Pemasangan

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Cara menjalankan

    python cek.py <folder>

Contoh pada folder uji:

    python cek.py uji/

## Contoh output

Pada folder `uji/`:

    uji/panjang.py:1: fungsi terlalu_besar panjang (36 baris)
    uji/rusak.py:1: sintaks bermasalah (MISSING)
    uji/todo.py:2: # TODO: perbaiki ini
    uji/todo.py:3: # FIXME nanti

Pada repo nyata (`pallets/itsdangerous`), hasil lengkapnya ada di
`hasil-repo-nyata.txt`. Dua file dicocokkan manual dengan `grep` dan hitungan
baris:

- `timed.py`: TODO di baris 182 (cocok).
- `signer.py`: `__init__` 45 baris dan `derive_key` 32 baris (cocok).
