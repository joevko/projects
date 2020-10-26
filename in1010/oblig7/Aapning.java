import java.util.*;

public class Aapning extends HvitRute {
    public Aapning(int rad, int kolonne) {
        super(rad, kolonne);
    }
    //Når den blir funnet returener den kordinate slik at
    //vi er ferdig og trenger logge veien tilbake.
    public LinkedList<String> gaa(Rute caller) {
        LinkedList<String> liste = new LinkedList<String>();
        liste.add(this.getCoords());
        return liste;
    }
}
