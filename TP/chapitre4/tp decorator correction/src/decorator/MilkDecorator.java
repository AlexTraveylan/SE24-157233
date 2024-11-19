package decorator;

import beverage.IBeverage;

public class MilkDecorator extends ICondimentDecorator {

    public MilkDecorator(IBeverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public String getDescription() {
        return beverage.getDescription() + ", Milk";
    }

    @Override
    public double cost() {
        return beverage.cost() + 0.10;
    }
}
