public class TestPreparat{
  public static void main(String[] args) {

    PreparatA aa = new PreparatA("aa", 500, 20, 7);
    PreparatB bb = new PreparatB("bb", 300, 40, 8);
    PreparatC cc = new PreparatC("cc", 100, 10);

    System.out.println("-----Samlet informasjon om preparatene: ----");
    System.out.println(aa);
    System.out.println(bb);
    System.out.println(cc);

    //Tester PreparatA
    System.out.println("-----Tester Preparat A: -----");
    stringPrepTest(aa.hentNavn(), "aa");
    doublePrepTest(aa.hentPris(), 600);
    doublePrepTest(aa.hentVirkestoff(), 20);
    intPrepTest(aa.hentNarkotiskStyrke(), 3);
    aa.settNyPris(1000);
    System.out.println("Ny pris: "+ aa.hentPris() + "kr");
    //Tester PreparatB
    System.out.println("-----Tester Preparat B: -----");
    stringPrepTest(bb.hentNavn(), "zz");
    doublePrepTest(bb.hentPris(), 300);
    doublePrepTest(bb.hentVirkestoff(), 40);
    intPrepTest(bb.hentVanedannedeStyrke(), 8);
    bb.settNyPris(150);
    System.out.println("Ny pris: "+ bb.hentPris() + "kr");
    //Tester PreparatC
    System.out.println("-----Tester Preparat C: -----");
    stringPrepTest(cc.hentNavn(), "cc");
    doublePrepTest(cc.hentPris(), 2000);
    doublePrepTest(cc.hentVirkestoff(), 5);
    cc.settNyPris(70);
    System.out.println("Ny pris: "+ cc.hentPris() + "kr");
  }

    /* Dette er en lang løsning!
    if(aa.hentPris() == 500){
      System.out.println("Riktig");
    }else{
      System.out.println("Feil");
      }*/


  //Testing double values
  public static boolean doublePrepTest(double faktiskResultat, double forventetResultat){
    if (faktiskResultat == forventetResultat) {
      System.out.println("Riktig");
    }else{
      System.out.println("Feil");
    }
    return faktiskResultat == forventetResultat;
  }


  //Testing string values
  public static boolean stringPrepTest(String faktiskResultat, String forventetResultat){
    if (faktiskResultat == forventetResultat) {
      System.out.println("Riktig");
    }else{
      System.out.println("Feil");
    }
    return faktiskResultat == forventetResultat;
  }

  //Testing integer values
  public static boolean intPrepTest(int faktiskResultat, int forventetResultat){
    if (faktiskResultat == forventetResultat) {
      System.out.println("Riktig");
    }else{
      System.out.println("Feil");
    }
    return faktiskResultat == forventetResultat;
  }

}
