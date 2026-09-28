"""Tavern Ledger: a tiny inventory tool for the Rusty Flagon tavern.

This is the sandbox project for the course. It has a few bugs and gaps
on purpose. Quests will ask you to direct an agent to find and fix them.

Usage:
    python tavern.py list
    python tavern.py add <item> <qty> <price>
    python tavern.py sell <item> <qty>
    python tavern.py total
"""

import json
import sys
from pathlib import Path

LEDGER = Path(__file__).parent / "ledger.json"


def load():
    if not LEDGER.exists():
        return {}
    return json.loads(LEDGER.read_text())


def save(data):
    LEDGER.write_text(json.dumps(data, indent=2))


def add(data, item, qty, price):
    if item in data:
        data[item]["qty"] += qty
    else:
        data[item] = {"qty": qty, "price": price}


def sell(data, item, qty):
    data[item]["qty"] -= qty


def total(data):
    return sum(entry["qty"] * entry["price"] for entry in data.values())


def main(argv):
    data = load()
    cmd = argv[1] if len(argv) > 1 else "list"

    if cmd == "list":
        for item, entry in data.items():
            print(f"{item:<12} x{entry['qty']:<4} @ {entry['price']}g")
    elif cmd == "add":
        add(data, argv[2], int(argv[3]), float(argv[4]))
        save(data)
    elif cmd == "sell":
        sell(data, argv[2], int(argv[3]))
        save(data)
    elif cmd == "total":
        print(f"Stock value: {total(data)}g")
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
