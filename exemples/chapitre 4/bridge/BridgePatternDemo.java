// Abstraction
abstract class Shape {
    protected Color color;

    protected Shape(Color color) {
        this.color = color;
    }

    abstract void draw();
}

// Refined Abstraction
class Circle extends Shape {
    public Circle(Color color) {
        super(color);
    }

    @Override
    void draw() {
        System.out.print("Drawing Circle in ");
        color.applyColor();
    }
}

class Square extends Shape {
    public Square(Color color) {
        super(color);
    }

    @Override
    void draw() {
        System.out.print("Drawing Square in ");
        color.applyColor();
    }
}

// Implementor
interface Color {
    void applyColor();
}

// Concrete Implementor
class RedColor implements Color {
    @Override
    public void applyColor() {
        System.out.println("Red.");
    }
}

// Concrete Implementor
class BlueColor implements Color {
    @Override
    public void applyColor() {
        System.out.println("Blue.");
    }
}

class GreenColor implements Color {
    @Override
    public void applyColor() {
        System.out.println("Green.");
    }
}

// Client code to test the pattern
public class BridgePatternDemo {
    public static void main(String[] args) {
        Shape redCircle = new Circle(new RedColor());
        Shape blueCircle = new Circle(new BlueColor());

        Shape redSquare = new Square(new RedColor());
        Shape greenSquare = new Square(new GreenColor());

        redCircle.draw(); // Output: Drawing Circle in Red.
        blueCircle.draw(); // Output: Drawing Circle in Blue.
        redSquare.draw(); // Output: Drawing Square in Red.
        greenSquare.draw(); // Output: Drawing Square in Green.
    }
}