class MResept extends HvitResept {
  // gir alltid 100% rabatt
  public MResept(Legemiddel legemiddel, Lege utskrivendeLege, Pasient pasient, int reit){
    super(legemiddel, utskrivendeLege, pasient, reit);
  }

  public String farge(){
    return "Hvit resept";
  }

  public double prisAaBetale(){
    return 0;
  }
}
