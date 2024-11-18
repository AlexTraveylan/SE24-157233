from creature.factory import CreatureFactory


def main():
    print("Hello from correction-tp-factory!")

    while True:
        CreatureFactory.display_creatures()
        creature_type = input("Enter the type of creature you want to create: (or 'q' to quit) ")

        creature_type = creature_type.lower()

        if creature_type == 'q':
            print("Goodbye!")
            break

        try:
            creature = CreatureFactory.create_creature(creature_type)
            print("Creation Success!")
            print(creature.get_description())

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
