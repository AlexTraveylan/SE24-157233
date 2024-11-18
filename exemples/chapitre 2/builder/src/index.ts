import { PizzaBuilder } from "./pizza"

const pizzaBuilder = new PizzaBuilder()
const pizza = pizzaBuilder.buildSauce("tomato").buildPasta("thin").buildSize("large").buildToppings(["mozzarella", "parmesan", "oregano"]).build()

pizzaBuilder.reset()
const pizza2 = pizzaBuilder.buildSauce("tomato").buildSize("small").build()

console.log(pizza.toString())
console.log(pizza2.toString())
