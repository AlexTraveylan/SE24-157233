package observateur;

public class PanneauExterieur implements Observateur {

    @Override
    public void update(float temperature, float humidite, float pression) {
        System.out.println("PanneauExterieur: " + temperature + "°C et " + humidite + "% humidité" + pression + "Pa");
    }
}
