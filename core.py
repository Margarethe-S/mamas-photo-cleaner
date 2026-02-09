import os
import hashlib
from collections import defaultdict

def hash_file(path, chunk_size=8192):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(chunk_size):
                h.update(chunk)
    except Exception:
        return None
    return h.hexdigest()

def find_duplicate_groups(folders):
    hash_map = defaultdict(list)

    for folder in folders:
        for root, _, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                h = hash_file(full_path)
                if h:
                    hash_map[h].append(full_path)

    result = []
    for paths in hash_map.values():
        if len(paths) > 1:
            result.append(paths)
    return result

def classify_duplicates(duplicate_groups):
    structured = {}
    for group in duplicate_groups:
        original = group[0]
        structured.setdefault(os.path.dirname(original), []).append((original, "original"))

        for dup in group[1:]:
            folder = os.path.dirname(dup)
            if folder == os.path.dirname(original):
                structured.setdefault(folder, []).append((dup, "blue"))
            else:
                structured.setdefault(folder, []).append((dup, "yellow"))
    return structured
