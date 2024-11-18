import { RaceVoiture, Vehicule, Voiture } from "./voiture";

export interface Builder {
  reset(): void;
  buildNbSeats(nbSeats: number): Builder;
  buildEngine(engine: string): Builder;
  buildColor(color: string): Builder;
  build(): Vehicule;
}

export class VoitureBuilder implements Builder {
  private vehicule: Vehicule;

  public constructor() {
    this.vehicule = new Voiture();
  }

  reset(): void {
    this.vehicule = new Voiture();
  }

  buildNbSeats(nbSeats: number): VoitureBuilder {
    this.vehicule.nbSeats = nbSeats;
    return this;
  }

  buildEngine(engine: string): VoitureBuilder {
    this.vehicule.engine = engine;
    return this;
  }

  buildColor(color: string): VoitureBuilder {
    this.vehicule.color = color;
    return this;
  }

  build(): Vehicule {
    return this.vehicule;
  }
}

export class RaceVoitureBuilder implements Builder {
  private vehicule: Vehicule;

  constructor() {
    this.vehicule = new RaceVoiture();
  }

  reset(): void {
    this.vehicule = new RaceVoiture();
  }

  buildNbSeats(nbSeats: number): RaceVoitureBuilder {
    this.vehicule.nbSeats = nbSeats;
    return this;
  }

  buildEngine(engine: string): RaceVoitureBuilder {
    this.vehicule.engine = engine;
    return this;
  }

  buildColor(color: string): RaceVoitureBuilder {
    this.vehicule.color = color;
    return this;
  }

  build(): Vehicule {
    return this.vehicule;
  }
}
