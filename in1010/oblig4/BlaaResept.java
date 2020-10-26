public class BlaaResept extends Resept {
  public BlaaResept(Legemiddel legemiddel, Lege utskrivendeLege, Pasient pasient, int reit) {
    super(legemiddel, utskrivendeLege, pasient, reit);
    super.beloep = super.beloep * 0.25;
  }
  public String farge(){
    return "Blå resept";
  }

  public double prisAaBetale(){
    return super.beloep;
  }

  @Override
  public String toString(){
    String output = legemiddel.hentNavn() + ", " + legemiddel.hentId() + ", " + utskrivendeLege.hentLegeNavn() + ", " + pasient.hentId();
    return output;
  }
  
}
