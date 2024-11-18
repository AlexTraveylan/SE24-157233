class Database {
  private static instance: Database;
  private readonly id: string;

  private constructor() {
    this.id = Math.random().toString(36).substring(2, 15);
  }

  public static getInstance(): Database {
    if (!Database.instance) {
      Database.instance = new Database();
    }
    return Database.instance;
  }

  public getID(): string {
    return this.id;
  }

  public query(sql: string): void {
    console.log(`Executing query: ${sql}`);
  }
}

const db1 = Database.getInstance();
const db2 = Database.getInstance();

console.log(db1.getID());
console.log(db2.getID());
console.log(db1 === db2);

db1.query("SELECT * FROM users");
