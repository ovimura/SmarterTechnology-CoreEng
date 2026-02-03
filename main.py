def sort(width, height, length, mass):
    """
    Determines the stack for a package based on its dimensions and mass.

    Args:
        width (float): Width of the package in cm.
        height (float): Height of the package in cm.
        length (float): Length of the package in cm.
        mass (float): Mass of the package in kg.

    Returns:
        str: The stack name: "STANDARD", "SPECIAL", or "REJECTED".
    """

    # Compute volume
    volume = width * height * length

    # Determine if package is bulky
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150

    # Determine if package is heavy
    heavy = mass >= 20

    # Determine stack
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# Example test cases
if __name__ == "__main__":
    test_packages = [
        (50, 50, 50, 10),    # Standard package
        (200, 50, 50, 10),   # Bulky, but not heavy
        (50, 50, 50, 25),    # Heavy, but not bulky
        (200, 100, 50, 25),  # Both bulky and heavy
        (100, 100, 100, 10), # Exactly 1,000,000 cm³ volume (bulky)
        (150, 20, 20, 19),   # One dimension >= 150 (bulky)
    ]

    for w, h, l, m in test_packages:
        print(f"Package ({w}x{h}x{l}, {m}kg) -> {sort(w,h,l,m)}")
