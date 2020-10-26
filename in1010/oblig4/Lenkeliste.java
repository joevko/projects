import java.util.Iterator;
import java.lang.Iterable;

public class Lenkeliste <T> implements Liste<T> {
  protected Node start;
  protected Node neste;
  protected int stoerrelse;


  protected class Node {
    T element;
    Node neste;

    Node(T x) {
      neste = null;
      element = x;
    }
  }
   protected class LenkelisteIterator implements Iterator <T> {
    private Node nodeToGiveNext = start.neste;

    @Override
    public boolean hasNext() {
        return nodeToGiveNext != null;
    }

    @Override
    public T next() {
      T verdi = nodeToGiveNext.element;
      nodeToGiveNext = nodeToGiveNext.neste;
      return verdi;
    }
  }

  public Lenkeliste() {
    start = new Node(null);
    //slutt = new Node(null);
    // slutt.forrige = neste;
    stoerrelse = 0;
  }

  @Override
  public int stoerrelse() {
    return stoerrelse;
  }

  @Override
  public void leggTil(T x){
    Node n = new Node(x); // noden som skal legges til
    Node p = start; // hjelpe-noden som vi bruker til å iterere gjennom liste
    while (p.neste != null){
      p = p.neste;
    }
    p.neste = n;

    stoerrelse++;
 }

 @Override
 public void leggTil(int pos, T x){

   //exception-test
   if(pos >= 0 && pos <= stoerrelse){

     Node n = new Node(x);
     Node p = start;

     int teller = 0;
     while (teller != pos){
       p = p.neste;
       teller++;
     }
     n.neste = p.neste;
     p.neste = n;

     stoerrelse++;
   }else{
     throw new UgyldigListeIndeks(pos);
   }

 }

  @Override
  public T hent(int pos) {
    if (pos >= 0 && pos < stoerrelse){
      Node n = start.neste;
      for (int i = 0; i < pos; i++){
        n = n.neste;
      }
      return n.element;
    }else{
      throw new UgyldigListeIndeks(pos);
    }
  }

  @Override //fjerner og returnerer elementet på starten av listen
  public T fjern() {
    if (stoerrelse == 0){
      throw new UgyldigListeIndeks(-1);
    }
    Node f = start.neste;
    start.neste = start.neste.neste;
    stoerrelse--;
    return f.element;

}

  @Override
  public T fjern(int pos){
    if (stoerrelse == 0){
      throw new UgyldigListeIndeks(-1);
    }
    if(pos >= 0 && pos < stoerrelse){
      Node p = start;

      int teller = 0;
      while (teller != pos){
        p = p.neste;
        teller++;
      }
      Node f = p.neste;
      p.neste = p.neste.neste;
      stoerrelse--;
      return f.element;
    }else{
      throw new UgyldigListeIndeks(pos);
    }
  }

  @Override
  public void sett(int pos, T x){
    if (pos >= 0 && pos < stoerrelse){
      Node n = new Node(x);
      Node p = start;

      int teller = 0;
      while (teller != pos){
        p = p.neste;
        teller++;
      }
      n.neste = p.neste.neste;
      p.neste = n;
    }else{
    throw new UgyldigListeIndeks(pos);
    }
  }

  public Iterator<T> iterator(){
    return new LenkelisteIterator();
  }
}
