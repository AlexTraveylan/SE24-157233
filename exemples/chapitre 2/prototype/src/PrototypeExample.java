
interface Prototype {
    Prototype clone();
}

class Shape implements Prototype {
    private String type;

    public Shape(String type) {
        this.type = type;
    }

    @Override
    public Prototype clone() {
        return new Shape(type);
    }
}

public class PrototypeExample {
    public static void main(String[] args) {
        Shape circle = new Shape("Circle");
        Shape circleClone = (Shape) circle.clone();

        System.out.println("is circle clone equal to circle? " + circle.equals(circleClone));
    }
}
