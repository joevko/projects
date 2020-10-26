class PResept extends HvitResept{

  public PResept(Legemiddel legemiddel, Lege utskrivendeLege, Pasient pasient, int reit){
    super(legemiddel, utskrivendeLege, pasient, reit);
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

  @Override
  public String toString(){
    String output = legemiddel.hentNavn() + ", " + legemiddel.hentId() + ", " + utskrivendeLege.hentLegeNavn() + ", " + pasient.hentId();
    return output;
  }
}
