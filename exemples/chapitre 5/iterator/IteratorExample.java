import java.util.ArrayList;
import java.util.Iterator;
import java.util.NoSuchElementException;

// Classe représentant un livre
class Livre {
    private String titre;

    public Livre(String titre) {
        this.titre = titre;
    }

    public String getTitre() {
        return titre;
    }
}

interface Iterator<T> {
    boolean hasNext();

    T next();
}

// Collection personnalisée de livres
class CollectionLivre implements Iterable<Livre> {
    private ArrayList<Livre> livres;
    private int index = 0;

    public CollectionLivre(int taille) {
        livres = new ArrayList<>();
    }

    public void ajouterLivre(Livre livre) {
        livres.add(livre);
    }

    @Override
    public Iterator<Livre> iterator() {
        return new LivreIterator();
    }
}

public class IteratorExample {
    public static void main(String[] args) {
        CollectionLivre collection = new CollectionLivre(3);
        collection.ajouterLivre(new Livre("Design Patterns"));
        collection.ajouterLivre(new Livre("Effective Java"));
        collection.ajouterLivre(new Livre("Clean Code"));

        for (Livre livre : collection) {
            System.out.println(livre.getTitre());
        }
    }
}