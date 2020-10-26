class MResept extends HvitResept {
  // gir alltid 100% rabatt
  public MResept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId, int reit){
    super(legemiddel, utskrivendeLege, pasientId, reit);
  }

  public String farge(){
    return "Hvit resept";
  }

  public double prisAaBetale(){
    return 0;
  }
}
