public class Zoo {

    public static void main(String[] args) {
        System.out.println("=== Bienvenue au zoo ===");

        ZooControler zooControler = ZooControler.getInstance();
        ZooControler zooControler2 = ZooControler.getInstance();

        System.out.println("zooControler == zooControler2 : " + (zooControler == zooControler2));

        zooControler.addAnimal();
        zooControler.addAnimal();
        zooControler.addAnimal();
        zooControler.addAnimal();

        zooControler.openZoo();

        zooControler.addVisitor();
        zooControler.addVisitor();

        zooControler.getInfo();
    }
}
