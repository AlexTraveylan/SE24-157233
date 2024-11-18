import { Creature } from "./abstract";

export class Dragon extends Creature {
  public static readonly WINGSPAN = 10;
  public static readonly ELEMENT = "Fire";

  constructor() {
    super("Dragon");
  }

  getDescription(): string {
    return `A ${Dragon.ELEMENT} ${this.name} with a wingspan of ${Dragon.WINGSPAN} meters.`;
  }
}

export class Phoenix extends Creature {
  public static readonly REGENERATION_CYCLE = 500;

  constructor() {
    super("Phoenix");
  }

  getDescription(): string {
    return `A ${this.name} with a regeneration cycle of ${Phoenix.REGENERATION_CYCLE} days.`;
  }
}

export class Griffin extends Creature {
  public static readonly HEAD_TYPE = "Aigle";
  public static readonly BODY_TYPE = "Lion";

  constructor() {
    super("Griffin");
  }

  getDescription(): string {
    return `A ${this.name} with a ${Griffin.HEAD_TYPE} head and a ${Griffin.BODY_TYPE} body.`;
  }
}
