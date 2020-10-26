public class Node {


  private int minne;
  private int antPros;
  //private int paakrevdMinne;

// konstruktøren har 2 param.
  public Node(int minne, int antPros){
    this.minne = minne;
    this.antPros = antPros;
  }

// Returnerer antall prosessorer i noden
  public int antProsessorer() {
    return antPros;
  }

//If-test som sjekker om noden har nok minne
  public boolean nokMinne(int paakrevdMinne) {
    if (minne >= paakrevdMinne){
      return true;
    } else {
      return false;
    }
  }

}
