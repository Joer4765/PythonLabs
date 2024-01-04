for i in range(10, 0, -1):
    print()
    print("\n".join([
        f"{i} green bottle{'s' if i - 1 != 0 else ''} hanging on the wall,",
        f"{i} green bottle{'s' if i - 1 != 0 else ''} hanging on the wall,",
        f"There'll be {i - 1} bottles hanging on the wall."
    ]))
