class PResept extends HvitResept{

  public PResept(Legemiddel legemiddel, Lege utskrivendeLege, int pasientId, int reit){
    super(legemiddel, utskrivendeLege, pasientId, reit);
    super.reit = 3; // siden P-resept har alltid 3 reit
    if (super.beloep < 108.00){ //brukeren kan aldri betale minder enn 0 kr
      super.beloep = 0;
    }else{
      super.beloep = super.beloep - 108.00; //betaler alltid 116kr mindre for legemiddelet
    }
  }

  public String farge() {
    return "Hvit resept";
  }

  public double prisAaBetale(){
    return super.beloep;
  }
}
