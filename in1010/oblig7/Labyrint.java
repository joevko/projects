import java.io.*;
import java.util.*;

public class Labyrint {

    private Rute[][] 	ruter;
    private int 		rader;
    private int 		kolonner;


    private Labyrint(int kolonner, int rader, Rute[][] ruter) {
        this.ruter = ruter;
        this.rader = rader;
        this.kolonner = kolonner;
        this.setNaboerOgLabyrint();
    }
    //Setter opp referanser for ruter sin naboer og labirinten
    public void setNaboerOgLabyrint() {
        for (Rute [] ruter : this.ruter) {
            for (Rute rute: ruter) {
                this.setNabo(rute);
                rute.setLabyrint(this);
            }
        }
    }

    public int getRader() {
        return this.rader;
    }

    public int getKolonner() {
        return this.kolonner;
    }

    private void setNabo(Rute rute) {
        if (!this.erNord(rute)) {
            rute.setNord(this.ruter[rute.getRad() - 1][rute.getKolonne()]);
        }
        if (!this.erSor(rute)) {
            rute.setSor(this.ruter[rute.getRad() + 1][rute.getKolonne()]);
        }
        if (!this.erVest(rute)) {
            rute.setVest(this.ruter[rute.getRad()][rute.getKolonne() - 1]);
        }
        if (!this.erOst(rute)) {
            rute.setOst(this.ruter[rute.getRad()][rute.getKolonne() + 1]);
        }
    }
    //sjekker om ruten de er på nord/øst/vest/sør kantene
    private Boolean erNord(Rute rute) {
        return rute.getRad() == 0;
    }

    private Boolean erSor(Rute rute) {
        return rute.getRad() == this.rader - 1;
    }

    private Boolean erOst(Rute rute) {
        return rute.getKolonne() == this.kolonner - 1;
    }

    private Boolean erVest(Rute rute) {
        return rute.getKolonne() == 0;
    }
    //klasifiserer rutene
    public static Rute genererRute(char rute, int rad, int kolonne, Boolean kant) {
        if (rute == '.' && kant) {
            return new Aapning(rad, kolonne);
        } else if (rute == '.') {
            return new HvitRute(rad, kolonne);
        } else {
            return new SortRute(rad, kolonne);
        }
    }

    public static Boolean sjekkKant(int kolonne, int rad, int kolonner, int rader) {
        return kolonne == kolonner - 1 || kolonne == 0 || rad == rader - 1 || rad == 0;
    }

    //Starter forsøket å finne veien ut av en bestemt rute.
    public LinkedList<String> finnUtveiFra(int kolonne, int rad) {
        LinkedList<String> path = this.ruter[rad][kolonne].gaa(null);
        return path;
    }

    public LinkedList<String> finnUtveiFra (Rute rute) {
        return rute.gaa(null);
    }

    public static Labyrint lesFraFil(File fil) throws FileNotFoundException {
        Scanner scanner = new Scanner(fil);
        String dimensions = scanner.nextLine();
        int rader = Integer.parseInt(dimensions.split(" ")[0].trim());
        int kolonner = Integer.parseInt(dimensions.split(" ")[1].trim());

        Rute ruter[][] = new Rute[rader][kolonner];

        //leser inn filene og genere rute array
        String row = "";
        int rad = 0;
        while (scanner.hasNextLine()) {
            row = scanner.nextLine();
            int kolonne = 0;
            for (char rute: row.toCharArray()) {
                ruter[rad][kolonne] = Labyrint.genererRute(rute, rad, kolonne, Labyrint.sjekkKant(kolonne, rad, kolonner, rader));
                kolonne++;
            }
            rad++;
        }
        return new Labyrint(kolonner, rader, ruter);
    }

    public String toString() {
        String string = "   ";
        int i = 0;
        for (int j = 0; j < kolonner; j++) {
            string += j > 10 ? " " + j + "  " : "  " + j + "  ";
        }
        string += "\n";
        for (Rute[] ruter : this.ruter) {
            string += i >= 10 ? i + " " : i + "  ";
            for (Rute rute: ruter) {
                string += rute;
            }
            i++;
            string += "\n";
        }
        return string;
    }

    public Rute[][] getRuter () {
        return this.ruter;
    }
}
