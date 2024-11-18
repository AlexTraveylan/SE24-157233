import type { CreatureType } from "./creature/factory";
import { CreatureFactory } from "./creature/factory";

while (true) {
  CreatureFactory.display_creatures();
  const creatureType = prompt(
    "Enter the type of creature you want to create: (or 'q' to quit) "
  )?.toLowerCase() as CreatureType | "q";

  if (creatureType === "q") {
    console.log("Quitting...");
    break;
  }

  try {
    const creature = CreatureFactory.create_creature(creatureType);
    console.log("Creation successful!");
    console.log(creature.getDescription());
  } catch (error) {
    console.error(`Error creating creature: ${error}`);
  }
}
