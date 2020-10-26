import java.util.ArrayList;

public class Rack {

  private ArrayList<Node> nodeListe;

  // private Node[] nodeliste;
  // int nodelisteLengde;

  public Rack(){
    nodeListe = new ArrayList<Node>();
  }

//Plassere en ny node inn i racket
  public void settInn(Node node){
    nodeListe.add(node);
  }
//Henter antall noder i racket
  public int getAntNoder() {
    return nodeListe.size();
  }
//Beregner sammenlagt antall prosessorer i nodene i et rack
  public int antProsessorer(){
    int teller = 0;
    for (int i = 0; i < nodeListe.size(); i++){
      teller += nodeListe.get(i).antProsessorer();
    }
    return teller;
  }
//beregner antall noder i racket med minne over gitt grense
  public int noderMedNokMinne(int paakrevdMinne) {
    int teller = 0;
    for (int i = 0; i<nodeListe.size(); i++){
      if(nodeListe.get(i).nokMinne(paakrevdMinne)){
        teller +=1;
      }

    }
    return teller;
  }

}
