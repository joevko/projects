public class Lege{
  String legeNavn;

  public Lege(String legeNavn){
    this.legeNavn = legeNavn;
    }
  public String hentLegeNavn(){
    return legeNavn;
  }
//Forstod ikke helt hvordan den delen burde løses
  public Resept skrivResept(Legemiddel legemiddel, int pasientId, int reit) throws UlovligUtskrift{
    if(legemiddel instanceof PreparatA){
      throw new UlovligUtskrift(this, legemiddel);
    }
    Legemiddel lm = legemiddel;
    BlaaResept b = new BlaaResept(lm, this, pasientId, reit);
    return b;

  }
}
