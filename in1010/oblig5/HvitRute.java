import java.util.*;

public class HvitRute extends Rute {

	private final int DIRECTIONS = 4;

	public HvitRute(int rad, int kolonne) {
		super(rad, kolonne);
	}

	public char tilTegn() {
		return '.';
	}
	//Setter nåværende kordinater til gått veien
	private LinkedList<String> setNaavearendeCoords(LinkedList<String> liste) {
		LinkedList<String> utveier = new LinkedList<String>();
		for (String u: liste) {
			utveier.add(this.getCoords() + " -> " + u);
		}
		return utveier;
	}
	//Prøver å gå alle fire retninger, hvis en av retningene treffer
	//åpning legges, retningene til en liste for den ruten av veier som
	//finnes til utgang. Deretter blir nåværende kord lagt til for hvert
	//hver vei i listen og retunert. 
	//Om ingen veiere har vei til utgangen returneres null. 
	public LinkedList<String> gaa(Rute caller) {
		LinkedList<String> utveier = new LinkedList<String>();
		LinkedList<String> utvei;
		
		if ((utvei = this.gaaNord(caller)) != null) {
			utveier.addAll(utvei);
		}

		if ((utvei = this.gaaSor(caller)) != null) {
			utveier.addAll(utvei);
		}

		if ((utvei = this.gaaOst(caller)) != null) {
			utveier.addAll(utvei);
		}

		if ((utvei = this.gaaVest(caller)) != null) {
			utveier.addAll(utvei);
		}

		return utveier.size() > 0 ? this.setNaavearendeCoords(utveier) : null;
	}
}
