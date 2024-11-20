const anExampleVariable = ">>>>>>>>>>>>>>Début";
console.log(anExampleVariable);

class Item {
  private id: number = 0;
  private name: string = "";
  private price: number = 0;
  private quantity: number = 0;

  constructor(id: number, name: string, price: number, quantity: number) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }

  public toString(): string {
    return (
      "Item{" +
      "id=" +
      this.id +
      ", name='" +
      this.name +
      "'" +
      ", price=" +
      this.price +
      ", quantity=" +
      this.quantity +
      "}"
    );
  }

  public getId(): number {
    return this.id;
  }

  public getName(): string {
    return this.name;
  }

  public getPrice(): number {
    return this.price;
  }

  public getQuantity(): number {
    return this.quantity;
  }
}

class FakeDb {
  private items!: Map<number, Item>;

  constructor() {
    this.items = new Map();
  }

  public loadData(): void {
    this.items.set(1, new Item(1, "Item 1", 100, 10));
    this.items.set(2, new Item(2, "Item 2", 200, 20));
    this.items.set(3, new Item(3, "Item 3", 300, 30));
    this.items.set(4, new Item(4, "Item 4", 400, 40));
    this.items.set(5, new Item(5, "Item 5", 500, 50));
    console.log("Data loaded");
  }

  public getItems(): Map<number, Item> {
    return this.items;
  }
}

class ItemDao {
  private readonly fakeDb: FakeDb = new FakeDb();

  constructor() {
    this.fakeDb.loadData();
  }

  public getItems(): Map<number, Item> {
    return this.fakeDb.getItems();
  }

  public getItemById(id: number): Item | undefined {
    return this.fakeDb.getItems().get(id);
  }

  public addItem(item: Item): void {
    this.fakeDb.getItems().set(item.getId(), item);
  }
}

//IMPLEMENTATION
const itemDao = new ItemDao();
const items: Map<number, Item> = itemDao.getItems();
console.log(items);

const newItem: Item = new Item(6, "Item 6", 600, 60);
itemDao.addItem(newItem);
console.log(itemDao.getItems());

const anExampleVariableFin = ">>>>>>>>>>>>>>FIN";
console.log(anExampleVariableFin);
