class Pizza {
  constructor(
    public sauce: string | null = null,
    public pasta: string | null = null,
    public size: string | null = null,
    public toppings: string[] = []
  ) {}

  toString() {
    return `Pizza with ${this.sauce} sauce, ${this.pasta} pasta, ${this.size} size, ${this.toppings.join(", ")} toppings`
  }
}

export class PizzaBuilder {
  private pizza: Pizza

  constructor() {
    this.pizza = new Pizza()
    return this
  }

  reset() {
    this.pizza = new Pizza()
    return this
  }

  buildSauce(sauce: string) {
    this.pizza.sauce = sauce
    return this
  }

  buildPasta(pasta: string) {
    this.pizza.pasta = pasta
    return this
  }

  buildSize(size: string) {
    this.pizza.size = size
    return this
  }

  buildToppings(toppings: string[]) {
    this.pizza.toppings = toppings
    return this
  }

  build() {
    return this.pizza
  }
}
