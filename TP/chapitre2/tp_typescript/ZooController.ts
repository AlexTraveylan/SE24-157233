export class ZooController {
  private static instance: ZooController;

  private constructor() {}

  public static getInstance(): ZooController {
    if (!ZooController.instance) {
      ZooController.instance = new ZooController();
    }
    return ZooController.instance;
  }

  public hello() {
    console.log("Hello");
  }
}
