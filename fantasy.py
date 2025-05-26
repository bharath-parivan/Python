inventory = {'rope': 1,'torch': 6,'gold coin': 42,'dagger': 1,'arrow': 12}

def display_inventory(inv):
    print("Inventory:")
    total_items = 0
    for item, count in inv.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}")

def add_to_inventory(inv, loot):
    for item in loot:
        inv[item] = inv.get(item, 0) + 1