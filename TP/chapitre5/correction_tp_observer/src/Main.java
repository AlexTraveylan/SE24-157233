import observateur.AffichageNumerique;
import observateur.PanneauExterieur;
import observateur.Smartphone;
import sujet.StationMeteo;

public class Main {
    public static void main(String[] args) {

        StationMeteo stationMeteo = new StationMeteo();

        // On crée les observateurs
        AffichageNumerique affichageNumerique = new AffichageNumerique();
        PanneauExterieur panneauExterieur = new PanneauExterieur();
        Smartphone smartphone = new Smartphone();

        // On enregistre les observateurs
        stationMeteo.registerObserver(affichageNumerique);
        stationMeteo.registerObserver(panneauExterieur);
        stationMeteo.registerObserver(smartphone);

        // On change les conditions météo
        stationMeteo.setConditionsMeteo(20, 65, 1013);

        System.out.println();

        // On supprime un observateur
        stationMeteo.removeObserver(affichageNumerique);
        System.out.println("AffichageNumerique supprimé");
        stationMeteo.removeObserver(panneauExterieur);
        System.out.println("PanneauExterieur supprimé");

        System.out.println();

        // On change les conditions météo
        stationMeteo.setConditionsMeteo(22, 70, 1015);
    }
}
