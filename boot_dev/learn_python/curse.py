def main():
    print("=====================================")
    print("Curse")
    print("=====================================")

    def curse(weapon_damage: int) -> tuple[int, int]:
        lesser_cursed: int = int(weapon_damage * 0.25)
        greater_cursed: int = int(weapon_damage * 0.50)

        return lesser_cursed, greater_cursed

    def test(weapon_damage: int):
        print("Weapon's base damage:", weapon_damage)
        print("Cursing...")

        lesser_cursed, greater_cursed = curse(weapon_damage)

        print("With lesser curse the damage is:", lesser_cursed, "damage.")
        print("With greater curse the damage is:", greater_cursed, "damage.")
        print("=====================================")

    test(100)
    test(500)
    test(1000)


if __name__ == "__main__":
    main()
