CONST_C = 300000000


def energy(mass: int) -> int:
    return mass * (CONST_C**2)


if __name__ == "__main__":
    user_input: int = int(input("Please enter mass (KG): "))
    print(f"E: {energy(user_input):,}")
