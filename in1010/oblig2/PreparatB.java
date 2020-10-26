public class PreparatB extends Legemiddel{
  int styrke;
  public PreparatB(String navn, double pris, double virkestoff,int styrke){
    super(navn, pris, virkestoff);
    this.styrke = styrke;
  }

  public int hentVanedannedeStyrke(){
    return styrke;
  }
  @Override
  public String toString(){
    return "Navn: " + this.navn + ", Pris: " + this.pris + "kr" + ", Virkestoff: " + this.virkestoff + "mg"+ ", Vanedannede styrke: " + this.styrke + "/10";
  }
}
