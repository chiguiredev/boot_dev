def main():
    print("=====================================")
    print("Printing vs returning")
    print("=====================================")

    def get_title(first_name: str, last_name: str, job: str):
        title = first_name + " " + last_name + " the " + job
        return title

    def test(first_name: str, last_name: str, job: str):
        title = get_title(first_name, last_name, job)
        print("First name:", first_name)
        print("Last name:", last_name)
        print("Job:", job)
        print("Title:", title)
        print("=====================================")

    test("Frodo", "Baggins", "warrior")
    test("Bilbo", "Baggins", "thief")
    test("Gandalf", "The Grey", "wizard")
    test("Aragorn", "Son of Arathorn", "ranger")


if __name__ == "__main__":
    main()
