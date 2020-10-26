public class Pasient {
  String navn;
  String foedselsnr;
  int id;
  static int teller;
  Stabel<Resept> resepter;

  public Pasient(String navn, String foedselsnr){
    this.navn = navn;
    this.foedselsnr = foedselsnr;
    resepter = new Stabel<Resept>();
    id = teller;
    teller++;
  }

  public void leggTilResept(Resept r){
    resepter.leggPaa(r);
  }

  public Stabel<Resept> hentResepter(){
    return resepter;
  }
  public int hentId(){
    return id;
  }

  public String hentNavn(){
    return navn;
  }
  public String foedselsnr(){
    return foedselsnr;
  }

  @Override
  public String toString(){
    String output = navn + ", " + foedselsnr;
    return output;
  }
}
