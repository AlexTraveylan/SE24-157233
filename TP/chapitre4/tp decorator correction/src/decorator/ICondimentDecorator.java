package decorator;

import beverage.IBeverage;

public abstract class ICondimentDecorator implements IBeverage {
    protected IBeverage beverage;

    public String getDescription() {
        throw new UnsupportedOperationException();
    }

    public double cost() {
        throw new UnsupportedOperationException();
    }
}
