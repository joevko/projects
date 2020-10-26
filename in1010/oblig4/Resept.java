public class Resept{
  int id = 0;
  Pasient pasient;
  int reit;
  int reseptId;
  double beloep;
  static int teller;
  Legemiddel legemiddel;
  public Lege utskrivendeLege;


  public Resept(Legemiddel legemiddel, Lege utskrivendeLege, Pasient pasient, int reit){
    this.legemiddel = legemiddel;
    this.utskrivendeLege = utskrivendeLege;
    this.pasient = pasient;
    this.reit = reit;
    id = teller;
    teller++;
    beloep = legemiddel.hentPris();
  }
  public int hentId(){
    return id;
  }
  public Legemiddel hentLegemiddel(){
    return legemiddel;
  }
  public Lege hentLege(){
    return utskrivendeLege;
  }
  public Pasient hentPasientId(){
    return pasient;
  }
  public int hentReit(){
    return reit;
  }

  public boolean bruk(){
    if(reit <= 0){
      System.out.println("Resepten er ugyldig.");
      return false;
    }else{
      reit = reit - 1;
      return true;
    }
  }

 

  public String farge() {
    return null;
  }
  public double prisAaBetale() {
    return 0.0;
  }





}
