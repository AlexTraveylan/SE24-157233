import beverage.Espresso;
import beverage.IBeverage;
import decorator.MilkDecorator;
import decorator.MochaDecorator;

public class CafeSimulator {

    public static void main(String[] args) {
        IBeverage beverage = new Espresso();

        IBeverage milkBeverage = new MilkDecorator(beverage);
        IBeverage mochaBeverage = new MochaDecorator(milkBeverage);
        IBeverage mochaMilkBeverage = new MochaDecorator(mochaBeverage);

        System.out.println(mochaMilkBeverage.getDescription() + " $" + mochaMilkBeverage.cost());
    }
}
