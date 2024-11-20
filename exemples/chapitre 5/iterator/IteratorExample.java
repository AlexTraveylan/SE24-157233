import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.ArrayList;

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

// Itérateur
class LivreIterator implements Iterator<Livre> {
    private final ArrayList<Livre> livres;
    private int position = 0;

    public LivreIterator(ArrayList<Livre> livres) {
        this.livres = livres;
    }

    @Override
    public boolean hasNext() {
        return position < livres.size();
    }

    @Override
    public Livre next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        return livres.get(position++);
    }
}

// Collection personnalisée de livres
class CollectionLivre implements Iterable<Livre> {
    private ArrayList<Livre> livres;

    public CollectionLivre() {
        livres = new ArrayList<>();
    }

    public void ajouterLivre(Livre livre) {
        livres.add(livre);
    }

    public void retirerLivre(Livre livre) {
        livres.remove(livre);
    }

    public void retirerLivre(int index) {
        livres.remove(index);
    }

    @Override
    public Iterator<Livre> iterator() {
        return new LivreIterator(livres);
    }
}

public class IteratorExample {
    public static void main(String[] args) {
        CollectionLivre collection = new CollectionLivre();
        collection.ajouterLivre(new Livre("Design Patterns"));
        collection.ajouterLivre(new Livre("Effective Java"));
        collection.ajouterLivre(new Livre("Clean Code"));

        // On peut maintenant ajouter autant de livres que l'on veut
        collection.ajouterLivre(new Livre("Java Concurrency in Practice"));

        for (Livre livre : collection) {
            System.out.println(livre.getTitre());
        }
    }
}