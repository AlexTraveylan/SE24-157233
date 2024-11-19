
import java.util.List;
import java.util.ArrayList;

// Concrete Subject
class WeatherStation {
    private float temperature;
    private List<Observer> observers;

    public WeatherStation() {
        observers = new ArrayList<>();
    }

    public void setTemperature(float temperature) {
        this.temperature = temperature;
        notifyObservers();
    }

    public void registerObserver(Observer o) {
        observers.add(o);
    }

    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(temperature);
        }
    }
}

// Interface Observer
interface Observer {
    void update(float temperature);
}

// Concrete Observer
class TemperatureDisplay implements Observer {
    private String displayId;

    public TemperatureDisplay(String displayId) {
        this.displayId = displayId;
    }

    @Override
    public void update(float temperature) {
        System.out.println("Display " + displayId + " - Température mise à jour : " + temperature + "°C");
    }
}

// Utilisation du pattern Observer
public class ObserverExample {
    public static void main(String[] args) {
        WeatherStation weatherStation = new WeatherStation();

        TemperatureDisplay display1 = new TemperatureDisplay("1");
        TemperatureDisplay display2 = new TemperatureDisplay("2");

        weatherStation.registerObserver(display1);
        weatherStation.registerObserver(display2);

        // Changement de température
        weatherStation.setTemperature(25.5f);

        // Suppression d'un affichage
        weatherStation.removeObserver(display1);

        // Nouveau changement de température
        weatherStation.setTemperature(27.0f);
    }
}