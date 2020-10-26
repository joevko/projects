public class Spesialist extends Lege implements Godkjenningsfritak {
  int kontrollID;

  public Spesialist(String legeNavn, int kontrollID){
  super(legeNavn);
  this.kontrollID = kontrollID;
  }

  public int hentKontrollID(){
    return kontrollID;
  }
  public Resept skrivResept(Legemiddel legemiddel, int pasientId, int reit) throws UlovligUtskrift{
    Legemiddel lm = legemiddel;
    BlaaResept b = new BlaaResept(lm, this, pasientId, reit);
    return b;

  }
}
