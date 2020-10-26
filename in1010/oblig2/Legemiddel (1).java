abstract class Legemiddel{
  String navn;
  double pris;
  double virkestoff;
  int id = 0;
  static int teller;

  public Legemiddel(String navn, double pris, double virkestoff){
    this.navn = navn;
    this.pris = pris;
    this.virkestoff = virkestoff;
    id = teller;
    teller++;
  }

  public String hentNavn(){
    return navn;
  }
  public double hentPris(){
    return pris;
  }
  public double hentVirkestoff(){
    return virkestoff;
  }
  public int hentId(){
    return id;
  }
  public void settNyPris(double nyPris){
    pris = nyPris;

  }

}
