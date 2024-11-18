interface Clonable {
  clone(): Clonable;
}

class SuperHero implements Clonable {
  constructor(
    public name: string,
    public pouvoirs: string[],
    public experience: number,
    public equipe: string
  ) {
    this.name = name;
    this.pouvoirs = pouvoirs;
    this.experience = experience;
    this.equipe = equipe;
  }

  clone(): SuperHero {
    return new SuperHero(
      this.name,
      this.pouvoirs,
      this.experience,
      this.equipe
    );
  }

  afficherCaracteristiques(): void {
    console.log(`
        Nom: ${this.name}
        Pouvoirs: ${this.pouvoirs}
        Expérience: ${this.experience}
        Equipe: ${this.equipe}
    `);
  }

  changerEquipe(equipe: string): void {
    this.equipe = equipe;
  }
}

const ironMan = new SuperHero(
  "Iron Man",
  ["Force", "Résistance", "Vol"],
  10,
  "Avengers"
);

ironMan.afficherCaracteristiques();
const warMachine = ironMan.clone();
warMachine.changerEquipe("Armure");
warMachine.name = "War Machine";
warMachine.afficherCaracteristiques();
