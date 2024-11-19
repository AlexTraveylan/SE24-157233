package beverage;

public class FilterCaffe implements IBeverage {

    @Override
    public String getDescription() {
        return "Filter Caffe";
    }

    @Override
    public double cost() {
        return 1.55;
    }
}
