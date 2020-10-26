public class PreparatC extends Legemiddel{
  public PreparatC(String navn, double pris, double virkestoff){
    super(navn, pris, virkestoff);
  }
  @Override
  public String toString(){
    return "Navn: " + this.navn + ", Pris: " + this.pris + "kr" + ", Virkestoff: " + this.virkestoff + "mg";
  }
}
