package decorator;

import beverage.IBeverage;

public class MochaDecorator extends ICondimentDecorator {

    public MochaDecorator(IBeverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public String getDescription() {
        return beverage.getDescription() + ", Mocha";
    }

    @Override
    public double cost() {
        return beverage.cost() + 0.20;
    }
}
