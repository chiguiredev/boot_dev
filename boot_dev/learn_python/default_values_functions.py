def main():
    print("=====================================")
    print("default function values")
    print("=====================================")

    PUNCH_DAMAGE: int = 50
    SLASH_DAMAGE: int = 100

    def get_punched(health: int, armor: int = 0):
        final_damage: int = PUNCH_DAMAGE
        final_damage = final_damage - armor
        return health - final_damage

    def get_slashed(health: int, armor: int = 0):
        final_damage: int = SLASH_DAMAGE
        final_damage = final_damage - armor
        return health - final_damage

    def test(health, armor):
        print(f"Health: {health}, Armor: {armor}")
        print(f"Health after punch: {get_punched(health, armor)}")
        print("=====================================")
        print(f"Health: {health}, Armor: {armor}")
        print(f"Health after slash: {get_slashed(health, armor)}\n")
        print("=====================================")
        print(f"Health: {health}, Armor: no armor!")
        print(f"Health after slash: {get_slashed(health)}\n")
        print("=====================================")
        print(f"Health: {health}, Armor: no armor!")
        print(f"Health after punch: {get_punched(health)}")
        print("=====================================")

    test(400, 5)
    test(300, 3)
    test(200, 1)


if __name__ == "__main__":
    main()
