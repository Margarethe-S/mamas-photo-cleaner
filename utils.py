import os
import sys
import json


def load_language(lang_code):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    lang_path = os.path.join(base_path, "language", f"{lang_code}.json")
    try:
        with open(lang_path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Language file not found: {lang_path}")
        print(e)
        return {}
