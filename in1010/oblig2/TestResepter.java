public class TestResepter{
  public static void main(String[] args) {
    PreparatA aa = new PreparatA("aa", 500, 20, 7);
    PreparatB bb = new PreparatB("bb", 300, 40, 8);
    PreparatC cc = new PreparatC("cc", 100, 10);

    Lege lege1 = new Lege("Hans The Doctor");

    // Oppretter resepter:
    BlaaResept res1 = new BlaaResept(aa, lege1, 123, 1);
    MResept mres1 = new MResept(bb, lege1, 456, 10);
    PResept pres1 = new PResept(cc, lege1, 789, 3);



    // Sjekker om unik legemiddel id fungerer
    System.out.println("Henter legemiddel ID 1: " + res1.hentId());
    System.out.println("Henter legemiddel ID 1: " + res1.hentId());
    System.out.println("Henter legemiddel ID 2: " + mres1.hentId());
    System.out.println("Henter legemiddel ID 3: " + pres1.hentId());

    //
    System.out.println(res1.hentLegemiddel());
    System.out.println(mres1.hentLegemiddel());
    System.out.println(pres1.hentLegemiddel());

    System.out.println(res1.hentLege().hentLegeNavn());

    // Sjekker om unik pasientId fungerer
    System.out.println("Henter pasientId 1: " + res1.hentPasientId());
    System.out.println("Henter pasientId 1: " + res1.hentPasientId());
    System.out.println("Henter pasientId 2: " + mres1.hentPasientId());
    System.out.println("Reit Test: ");
    System.out.println(res1.hentReit());
    res1.bruk();
    System.out.println(res1.hentReit());
    res1.bruk();

    // Tester farge
    System.out.println("Farge Test: ");
    System.out.println(res1.farge());
    System.out.println(mres1.farge());
    System.out.println(pres1.farge());

  //  System.out.println(lege1.skrivResept(aa,231,3));
  //  System.out.println(lege1.skrivResept(aa, 2334, 7));

  //exception
  try{
    lege1.skrivResept(aa, 2334, 7);

  }
  catch (UlovligUtskrift e){
    System.out.println(e);
  }




  }
}
