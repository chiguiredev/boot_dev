def main():
    def chapter_start_printer(number: int, lesson_name: str):
        print(
            "============================================================================"
        )
        print(f"Chapter {number}, lesson {lesson_name}\n")

    def chapter_end_printer():
        print(
            "============================================================================\n\n"
        )

    chapter_start_printer(2, "Function practice - degrees")

    def to_celsius(f: int) -> float:
        c = 5 / 9 * (f - 32)
        return c

    def test(f: int) -> None:
        c = round(to_celsius(f), 2)
        print(f, "degrees fahrenheit is", c, "degrees celsius")

    test(100)
    test(88)
    test(104)
    test(112)

    chapter_end_printer()

    chapter_start_printer(2, "Hours to seconds")

    def hours_to_seconds(hours: int) -> int:
        return hours * 3600

    def test_hours_seconds(hours):
        secs = hours_to_seconds(hours)
        print(f"hours {hours} is {secs:,} seconds")

    test_hours_seconds(10)
    test_hours_seconds(1)
    test_hours_seconds(25)
    test_hours_seconds(100)
    test_hours_seconds(33)

    chapter_end_printer()

    chapter_start_printer(2, "Multiple return values")

    def become_warrior(first_name, last_name, power): ...

    def test(first_name, last_name, power):
        title, new_power = become_warrior(first_name, last_name, power)
        print(title, "has a power level of:", new_power)

    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)

    chapter_end_printer()


if __name__ == "__main__":
    main()
