import java.util.Map;

public class Main {
    public static void main(String[] args) {
        ItemDao itemDao = new ItemDao();

        Map<Integer, Item> items = itemDao.getItems();
        System.out.println(items);

        Item item = itemDao.getItemById(1);
        System.out.println(item);

        Item newItem = new Item(6, "Item 6", 600, 60);
        itemDao.addItem(newItem);
        System.out.println(itemDao.getItems());
    }
}
