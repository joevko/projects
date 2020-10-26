import java.util.*;

public abstract class Rute {

    private int			rad;
    private int			kolonne;

    private Labyrint 	labyrint;

    private Rute		nord;
    private Rute		sor;
    private Rute		ost;
    private Rute		vest;

    public Rute(int rad, int kolonne) {
        this.rad = rad;
        this.kolonne = kolonne;
    }

    public void setLabyrint (Labyrint labyrint) {
        this.labyrint = labyrint;
    }
    //Setter nabo rute til nord for denne ruten.
    public void setNord(Rute nRute) {
        this.nord = nRute;
    }
    //Setter nabo rute til sor for denne ruten.
    public void setSor(Rute sRute) {
        this.sor = sRute;
    }
    //Setter nabo rute til ost for denne ruten.
    public void setOst(Rute oRute) {
        this.ost = oRute;
    }
    //Setter nabo rute til vest for denne ruten.
    public void setVest(Rute vRute) {
        this.vest = vRute;
    }

    public int getRad() {
        return this.rad;
    }

    public int getKolonne() {
        return this.kolonne;
    }

    public abstract LinkedList<String> gaa(Rute caller);

    //Sjekker om rute har nord rute og at den ikke kom fra den, og går ditt eller ikke rekursivt.
    protected LinkedList<String> gaaNord(Rute caller) {
        return this.nord != null && this.nord != caller ? this.nord.gaa(this) : null;
    }
    //Sjekker om rute har sor rute og at den ikke kom fra den og går ditt eller ikke..
    protected LinkedList<String> gaaSor(Rute caller) {
        return this.sor != null && this.sor != caller ? this.sor.gaa(this) : null;
    }
    //Sjekker om rute har ost rute og at den ikke kom fra den og går ditt eller ikke..
    protected LinkedList<String> gaaOst(Rute caller) {
        return this.ost != null && this.ost != caller ? this.ost.gaa(this) : null;
    }
    //Sjekker om rute har vest rute og at den ikke kom fra den og går ditt eller ikke..
    protected LinkedList<String> gaaVest(Rute caller) {
        return this.vest != null && this.vest != caller ? this.vest.gaa(this) : null;
    }

    public abstract char tilTegn();

    public String getCoords() {
        return "(" + this.kolonne + ", " + this.rad + ")";
    };

    public String toString() {
        return "  " + this.tilTegn() + "  ";
    }
}