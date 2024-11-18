export class Vehicule {
  constructor(
    public nbSeats: number | null = null,
    public engine: string | null = null,
    public color: string | null = null
  ) {}

  public toString(): string {
    return `Voiture: ${this.nbSeats} ${this.engine} ${this.color}`;
  }
}

export class Voiture extends Vehicule {
  public toString(): string {
    return `Voiture: ${this.nbSeats} ${this.engine} ${this.color}`;
  }
}

export class RaceVoiture extends Vehicule {
  public toString(): string {
    return `RaceVoiture: ${this.nbSeats} ${this.engine} ${this.color}`;
  }
}
