interface Target {
    String request();
}

class Adaptee {
    public String specific_request() {
        return ".ecnatsiseru tekcollet A";
    }
}

class Adapter implements Target {
    private Adaptee adaptee;

    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

    @Override
    public String request() {
        return "Adapter: (TRANSLATED) " + new StringBuilder(adaptee.specific_request()).reverse().toString();
    }
}

public class AdapterExemple {
    public static void main(String[] args) {
        Adaptee adaptee = new Adaptee();
        Target target = new Adapter(adaptee);

        System.out.println(target.request());
    }
}
