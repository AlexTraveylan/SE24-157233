export abstract class Creature {
  public name: string;

  public constructor(name: string) {
    this.name = name;
  }

  public abstract getDescription(): string;
}
