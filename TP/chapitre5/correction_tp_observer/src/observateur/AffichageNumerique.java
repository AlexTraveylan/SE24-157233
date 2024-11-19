package observateur;

public class AffichageNumerique implements Observateur {

    @Override
    public void update(float temperature, float humidite, float pression) {
        System.out.println("AffichageNumerique: " + temperature + "°C et " + humidite + "% humidité" + pression + "Pa");
    }
}
