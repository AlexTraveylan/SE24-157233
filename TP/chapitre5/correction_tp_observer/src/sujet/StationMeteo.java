package sujet;

import observateur.Observateur;

import java.util.ArrayList;
import java.util.List;

public class StationMeteo {
    private float temperature;
    private float humidite;
    private float pression;

    private List<Observateur> observers;

    public StationMeteo() {
        observers = new ArrayList<>();
    }

    public void setConditionsMeteo(float temperature, float humidite, float pression) {
        this.temperature = temperature;
        this.humidite = humidite;
        this.pression = pression;
        notifyObservers();
    }

    public void registerObserver(Observateur o) {
        observers.add(o);
    }

    public void removeObserver(Observateur o) {
        observers.remove(o);
    }

    private void notifyObservers() {
        for (Observateur observer : observers) {
            observer.update(temperature, humidite, pression);
        }
    }

}
