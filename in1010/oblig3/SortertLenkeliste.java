public class SortertLenkeliste <T extends Comparable<T>> extends Lenkeliste<T>{
  public SortertLenkeliste(){
    super();
  }
  //klassen kommer ikke gjennom alle testene(24 av 31 - ok)
  //jeg synes at problemet ligger her et sted... dessverre klarte jeg ikke å løse det.

  @Override
  public void leggTil(T x){
    Node n = new Node(x); // noden som skal legges til
    Node p = start; // hjelpe-noden som vi bruker til å iterere gjennom listen
    if (this.stoerrelse == 0) {
      super.leggTil(x);
    } else {
      while (p.neste != null) {
        if (n.element.compareTo(p.neste.element) < 0) {
          break;
        } else {
          p = p.neste;
        }
      }

      n.neste = p.neste;
      p.neste = n;
      stoerrelse++;

    }

  }

  @Override
  public T fjern() {
    if (stoerrelse == 0){
      throw new UgyldigListeIndeks(-1);
    }
    Node p = start;
    while (p.neste.neste != null){
      p = p.neste;
    }
    Node f = p.neste;
    p.neste = null;
    stoerrelse--;
    return f.element;
  }

  @Override
  public void sett(int pos, T x){
    throw new UnsupportedOperationException();
  }
  @Override
  public void leggTil(int pos, T x){
    throw new UnsupportedOperationException();
  }
}

class TestMe {
  public static void main(String[] args) {
    SortertLenkeliste<String> l = new SortertLenkeliste<>();
    l.leggTil("CCC");
    l.leggTil("BBB");
    l.leggTil("AAA");
    System.out.println(l.hent(0));
    System.out.println(l.hent(1));
    System.out.println(l.hent(2));
  }
}
