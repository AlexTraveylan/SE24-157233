import { Creature } from "./abstract";
import { Dragon, Griffin, Phoenix } from "./implementation";

export type CreatureType = "dragon" | "phoenix" | "griffin";

export class CreatureFactory {
  private static creatures: Record<CreatureType, () => Creature> = {
    dragon: () => new Dragon(),
    phoenix: () => new Phoenix(),
    griffin: () => new Griffin(),
  };

  public static display_creatures(): void {
    console.log("Available creatures:");
    Object.keys(CreatureFactory.creatures).forEach((creature) => {
      console.log(
        ` - ${creature.slice(0, 1).toUpperCase()}${creature.slice(1)}`
      );
    });
  }

  public static create_creature(creature_type: CreatureType): Creature {
    if (!(creature_type in CreatureFactory.creatures)) {
      throw new Error(`Invalid creature type: ${creature_type}`);
    }

    return CreatureFactory.creatures[creature_type]();
  }
}
