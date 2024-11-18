
public class ZooControler {

    private static ZooControler instance;
    private int nbVisitors;
    private int nbAnimals;
    private boolean isOpen;

    private ZooControler() {
        this.nbVisitors = 0;
        this.nbAnimals = 0;
    }

    public static ZooControler getInstance() {
        if (instance == null) {
            instance = new ZooControler();
        }
        return instance;
    }

    public int getNbVisitors() {
        return nbVisitors;
    }

    public int getNbAnimals() {
        return nbAnimals;
    }

    public boolean isOpen() {
        return isOpen;
    }

    public void getInfo() {
        System.out.println("Nombre de visiteurs : " + nbVisitors);
        System.out.println("Nombre d'animaux : " + nbAnimals);
        System.out.println("Le zoo est-il ouvert ? " + isOpen);
    }

    public void openZoo() {
        if (isOpen) {
            System.out.println("Le zoo est déjà ouvert");
            return;
        }
        isOpen = true;
    }

    public void closeZoo() {
        if (!isOpen) {
            System.out.println("Le zoo est déjà fermé");
            return;
        }
        isOpen = false;
        nbVisitors = 0;
    }

    public void addVisitor() {
        if (!isOpen) {
            System.out.println("Le zoo est fermé");
            return;
        }
        ++nbVisitors;
    }

    public void removeVisitor() {
        if (nbVisitors == 0) {
            System.out.println("Il n'y a pas de visiteurs dans le zoo");
            return;
        }
        --nbVisitors;
    }

    public void addAnimal() {
        ++nbAnimals;
    }

    public void removeAnimal() {
        if (nbAnimals == 0) {
            System.out.println("Il n'y a pas d'animaux dans le zoo");
            return;
        }
        --nbAnimals;
    }
}
