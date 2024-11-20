import java.util.Map;

class ItemDao {

    private final FakeDb fakeDb = new FakeDb();

    public ItemDao() {
        fakeDb.loadData();
    }

    public Map<Integer, Item> getItems() {
        return fakeDb.getItems();
    }

    public Item getItemById(int id) {
        return fakeDb.getItems().get(id);
    }

    public void addItem(Item item) {
        fakeDb.getItems().put(item.getId(), item);
    }
}
