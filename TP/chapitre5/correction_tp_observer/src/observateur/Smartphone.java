package observateur;

public class Smartphone implements Observateur {

    @Override
    public void update(float temperature, float humidite, float pression) {
        System.out.println("Smartphone: " + temperature + "°C");
    }
}
