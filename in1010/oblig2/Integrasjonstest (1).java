public class Integrasjonstest{
  public static void main(String[] args) {
    PreparatA aa = new PreparatA("aa", 500, 20, 7);
    PreparatB bb = new PreparatB("bb", 300, 40, 8);
    PreparatC cc = new PreparatC("cc", 100, 10);

    Lege lege1 = new Lege("Arne");
    Spesialist spesialist1 = new Spesialist("Steinar", 1583);

    MResept resept1 = new MResept(cc, lege1, 0, 6);
    PResept resept2 = new PResept(aa, spesialist1, 0, 288); //reit = 3
    BlaaResept resept3 = new BlaaResept(bb, lege1, 2303, 2);

    System.out.println("----Resept 1----");
    System.out.println("Navn på legemiddelet: " + cc.hentNavn() );
    System.out.println("Pris: " + cc.hentPris() + "kr");
    System.out.println("Virkestoff: " + cc.hentVirkestoff() + "mg");
    System.out.println("Legemiddel-ID: " + cc.hentId());
    resept1.bruk();
    System.out.println("Antall reit: " + resept1.hentReit());
    System.out.println("Resept-ID: " + resept1.hentId());
    System.out.println("Farge på resepten: " + resept1.farge());
    System.out.println("Prisen å betale: " + resept1.prisAaBetale());
    System.out.println("Legens navn: " + lege1.hentLegeNavn());
    System.out.println("Antall reit: " + resept1.hentReit());
    resept1.bruk();
    System.out.println("Antall reit: " + resept1.hentReit()  + "\n");

    System.out.println("----Resept 2----");
    System.out.println("Navn: " + aa.hentNavn() );
    System.out.println("Pris: " + aa.hentPris() + "kr");
    System.out.println("Virkestoff: " + aa.hentVirkestoff() + "mg" );
    System.out.println("Narkotisk styrke: " + aa.hentNarkotiskStyrke());
    System.out.println("Legemiddel-ID: " + aa.hentId());
    System.out.println("Resept-ID: " + resept2.hentId());
    System.out.println("Farge på resepten: " + resept2.farge());
    System.out.println("Prisen å betale: " + resept2.prisAaBetale());
    System.out.println("Legens navn: " + spesialist1.hentLegeNavn());
    System.out.println("Antall reit: " + resept2.hentReit() );
    resept2.bruk();
    resept2.bruk();
    resept2.bruk();
    resept2.bruk(); //reit = 3, printer ut "resepten er ugyldig"
    System.out.println("Antall reit: " + resept2.hentReit()  + "\n");

    System.out.println("----Resept 3----");
    System.out.println("Navn: " + bb.hentNavn() );
    System.out.println("Pris: " + bb.hentPris() + "kr");
    System.out.println("Virkestoff: " + bb.hentVirkestoff() + "mg" );
    System.out.println("Narkotisk styrke: " + bb.hentVanedannedeStyrke());
    System.out.println("Legemiddel-ID: " + bb.hentId());
    System.out.println("Resept-ID: " + resept3.hentId());
    System.out.println("Farge på resepten: " + resept3.farge());
    System.out.println("Pris å betale: " + resept3.prisAaBetale());
    System.out.println("Legens navn: " + lege1.hentLegeNavn());
    System.out.println("Antall reit: " + resept3.hentReit());

  }
}
