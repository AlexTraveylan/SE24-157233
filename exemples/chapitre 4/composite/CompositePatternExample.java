import java.util.ArrayList;
import java.util.List;

// Interface commune pour les composants simples et composites
interface Employee {
    void showDetails();
}

// Classe feuille représentant un simple employé
class Developer implements Employee {
    private String name;
    private String position;

    public Developer(String name, String position) {
        this.name = name;
        this.position = position;
    }

    @Override
    public void showDetails() {
        System.out.println(name + " works as " + position);
    }
}

// Classe composite représentant un manager supervisant des employés
class Manager implements Employee {
    private List<Employee> subordinates = new ArrayList<>();
    private String name;
    private String position;

    public Manager(String name, String position) {
        this.name = name;
        this.position = position;
    }

    public void addEmployee(Employee emp) {
        subordinates.add(emp);
    }

    public void removeEmployee(Employee emp) {
        subordinates.remove(emp);
    }

    @Override
    public void showDetails() {
        System.out.println(name + " is the " + position);
        for (Employee emp : subordinates) {
            emp.showDetails();
        }
    }
}

// Exemple d'utilisation
public class CompositePatternExample {
    public static void main(String[] args) {
        Developer dev1 = new Developer("John Doe", "Backend Developer");
        Developer dev2 = new Developer("Jane Smith", "Frontend Developer");

        Manager manager = new Manager("Alice Johnson", "Project Manager");
        manager.addEmployee(dev1);
        manager.addEmployee(dev2);

        Manager manager2 = new Manager("Bob Brown", "Project Manager");
        Developer dev3 = new Developer("Charlie Davis", "Frontend Developer");
        Developer dev4 = new Developer("David Wilson", "Frontend Developer");
        Developer dev5 = new Developer("Eve White", "Frontend Developer");

        manager2.addEmployee(dev3);
        manager2.addEmployee(dev4);
        manager2.addEmployee(dev5);

        Manager generalManager = new Manager("Doc Brown", "General Manager");
        generalManager.addEmployee(manager);
        generalManager.addEmployee(manager2);

        // Affichage des détails de la structure
        generalManager.showDetails();
    }
}