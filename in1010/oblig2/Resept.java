abstract class Resept{
  int id = 0;
  int pasientId;
  int reit;
  int reseptId;
  double beloep;
  static int teller;
  Legemiddel legemiddel;
  public Lege utskrivendeLege;


  public Resept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId, int reit){
    this.legemiddel = legemiddel;
    this.utskrivendeLege = utskrivendeLege;
    this.pasientId = pasientId;
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
  public int hentPasientId(){
    return pasientId;
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

  abstract public String farge();
  abstract public double prisAaBetale();





}
