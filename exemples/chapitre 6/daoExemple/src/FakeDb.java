import java.util.HashMap;
import java.util.Map;

public class FakeDb {

    private Map<Integer, Item> items;

    public FakeDb() {
        this.items = new HashMap<>();
    }

    public void loadData() {
        items.put(1, new Item(1, "Item 1", 100, 10));
        items.put(2, new Item(2, "Item 2", 200, 20));
        items.put(3, new Item(3, "Item 3", 300, 30));
        items.put(4, new Item(4, "Item 4", 400, 40));
        items.put(5, new Item(5, "Item 5", 500, 50));
        System.out.println("Data loaded");
    }

    public Map<Integer, Item> getItems() {
        return items;
    }
}
