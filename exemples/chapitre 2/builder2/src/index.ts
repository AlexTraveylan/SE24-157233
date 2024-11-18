import { Director } from "./director";

const director = new Director();
director.setVoitureBuilder();

const voiture = director.buildFullVoiture();
console.log(voiture.toString());
