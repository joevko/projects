public class BlaaResept extends Resept {
  public BlaaResept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId, int reit) {
    super(legemiddel, utskrivendeLege, pasientId, reit);
    super.beloep = super.beloep * 0.25;
  }
  public String farge(){
    return "Blå resept";
  }

  public double prisAaBetale(){
    return super.beloep;
  }
  
}
