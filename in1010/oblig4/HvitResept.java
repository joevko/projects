abstract public class HvitResept extends Resept{
  public HvitResept(Legemiddel legemiddel, Lege utskrivendeLege, Pasient pasient, int reit){
    super(legemiddel, utskrivendeLege, pasient, reit);
  }

  @Override
  public String toString(){
    String output = legemiddel.hentNavn() + ", " + legemiddel.hentId() + ", " + utskrivendeLege.hentLegeNavn() + ", " + pasient.hentId();
    return output;
  }
}

