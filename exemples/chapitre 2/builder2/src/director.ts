import { RaceVoitureBuilder, VoitureBuilder, type Builder } from "./builder";
import type { Vehicule } from "./voiture";

export class Director {
  private builder!: Builder;

  public constructor() {}

  public setVoitureBuilder(): void {
    this.builder = new VoitureBuilder();
  }

  public setRaceVoitureBuilder(): void {
    this.builder = new RaceVoitureBuilder();
  }

  public buildMinimalVoiture(): Vehicule {
    this.builder.reset();
    return this.builder
      .buildNbSeats(2)
      .buildEngine("1.0L")
      .buildColor("red")
      .build();
  }

  public buildFullVoiture(): Vehicule {
    this.builder.reset();
    return this.builder
      .buildNbSeats(5)
      .buildEngine("V8")
      .buildColor("blue")
      .build();
  }
}
