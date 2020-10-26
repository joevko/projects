
public class Hovedprogram {
  public static void main(String[] args) {
    Regneklynge abel = new Regneklynge("regneklynge.txt");
    System.out.println("--- Regneklynge Abel ---" + "\n");
    System.out.println("Antall rack:" + abel.antRacks());
    System.out.println("Antall prosessorer:" + abel.antProsessorer() + "\n");
    System.out.println("Noder med minst 32:" + abel.noderMedNokMinne(32));
    System.out.println("Noder med minst 64:" + abel.noderMedNokMinne(64));
    System.out.println("Noder med minst 128:" + abel.noderMedNokMinne(128));



  }
}
