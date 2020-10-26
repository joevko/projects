import java.util.*;

public class Lege implements Comparable<Lege>{
  String legeNavn;

  Lenkeliste<Resept> utskrevedeResepter;

  public Lege(String legeNavn){
    this.legeNavn = legeNavn;
    this.utskrevedeResepter = new Lenkeliste<Resept>();


  }

  public String hentLegeNavn(){
    return legeNavn;
  }

  public int antallUtskrevneNarkotiskeLegemidler () {
    int antall = 0;
    for (Resept r : this.utskrevedeResepter) {
      if (r.hentLegemiddel() instanceof PreparatA) {
        antall++;
      }
    }
    return antall;
  }

  public int compareTo(Lege l) {
    return this.hentLegeNavn().compareTo(l.hentLegeNavn());
  }

  public void leggTilResept(Resept r){
    utskrevedeResepter.leggTil(r);
  }

  public Lenkeliste<Resept> hentResepter(){
    return utskrevedeResepter;
  }


  //Forstod ikke helt hvordan den delen burde løses
  public Resept skrivResept(Legemiddel legemiddel, Pasient pasient, int reit) throws UlovligUtskrift{
    if(legemiddel instanceof PreparatA){
      throw new UlovligUtskrift(this, legemiddel);
    }

    Legemiddel lm = legemiddel;
    BlaaResept b = new BlaaResept(lm, this, pasient, reit);
    this.leggTilResept(b);
    pasient.leggTilResept(b);

    return b;
  }

  public String toString() {
    return "Lege " + this.hentLegeNavn();
  }
}
