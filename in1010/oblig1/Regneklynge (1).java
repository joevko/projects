import java.util.ArrayList;
import java.util.Scanner;
import java.io.*; //imports all the classes that are defined in java.io package to your file

public class Regneklynge {

  private File tekstfil;
  int noderPerRack;
  private ArrayList<Rack> rackListe;

  public Regneklynge(String filnavn) {
    tekstfil = new File(filnavn);
    Scanner innlesing = null;
    try { //kode som kan feile
      innlesing = new Scanner(tekstfil);
    } catch(FileNotFoundException e) {
      System.out.println("Kan ikke åpne denne filen."); // printer ut beskjeden hvis det ikke gaar aa aapne filen
      System.exit(0);
    }


if (innlesing.hasNext()){
  String line = innlesing.nextLine();
  this.noderPerRack = Integer.parseInt(line);
}
  rackListe = new ArrayList<Rack>();
  Rack rack = new Rack();
  rackListe.add(rack);


  while (innlesing.hasNext()) {
    String linje = innlesing.nextLine();
    String [] splitted = linje.split(" ");
    int antNoder = Integer.parseInt(splitted[0]);
    int minne = Integer.parseInt(splitted [1]);
    int prosessorer = Integer.parseInt(splitted[2]);

    for (int i=0; i<antNoder; i++){
      Node node = new Node(minne, prosessorer);
      this.settInnNode(node);
    }
  }
}
//plasserer en node inn i et rack med ledig plass, eller i et nytt rackk
  public void settInnNode(Node node) {
    //finner siste element i racklisten
    Rack sisteElement = rackListe.get(rackListe.size()-1);

    //nå sjekker jeg om sisteElement i rackListe inneholder færre noder enn noderPerRack
    // Hvis True- legges noden inn i racket.
    //Hvis False- lages det et bytt rack
    if(sisteElement.getAntNoder() < noderPerRack) {
      sisteElement.settInn(node);
    }else{
      Rack rack = new Rack();
      rackListe.add(rack); //legger til nytt racket i rackListe
      rack.settInn(node);//legger til noden i racket
    }
  }
  //Beregner totalt antall prosessorer i hele regneklyngen

  public int antProsessorer(){
    int teller = 0;
    for(int i = 0; i<rackListe.size();i++) {
      teller += rackListe.get(i).antProsessorer();
    }
    return teller;
  }

  //beregner antall noder i regneklyngen men minne over angitt grense

  public int noderMedNokMinne(int paakrevdMinne) {
    int teller = 0;
    for(int i = 0; i<rackListe.size(); i++) {
      teller += rackListe.get(i).noderMedNokMinne(paakrevdMinne);
    }
    return teller;
  }
  //Henter antall racks i regneklyngen
  public int antRacks() {
    return rackListe.size();
  }
}
