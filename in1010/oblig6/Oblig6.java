import java.util.*;

public class Oblig6 {

	private ArrayList<Thread> arbeidere;
	private MonitorKryptert monitorKryptert;
	private MonitorDekryptert monitorDekryptert;

	//Konstruktøren setter opp monitorene og oppretter n antall telegrafister og kryptografer,
	//og en operasjonsleder.
	//Når alle trådene er opprettet så startes de.
	public Oblig6(int antallTelegrafister, int antallKryptografer, String filnavn) {
		Operasjonssentral ops = new Operasjonssentral(antallTelegrafister);
		Kanal[] kanaler = ops.hentKanalArray();
		this.monitorKryptert = new MonitorKryptert();
		this.monitorDekryptert = new MonitorDekryptert();
		this.arbeidere = new ArrayList<Thread>();
		
		for (int i = 0; i < antallKryptografer; i++) {
			this.arbeidere.add(new Kryptograf(this.monitorKryptert, this.monitorDekryptert));
		}

		for (Kanal k: kanaler) {
			this.arbeidere.add(new Telegrafist(k, this.monitorKryptert));
		}

		this.arbeidere.add(new Operasjonsleder(this.monitorDekryptert, filnavn));

		this.startArbeidere();
	}

	public static void main(String[] args) {
		if (args.length < 3) {
			System.out.println("Usage: java Oblig6 [antall telegrafister] [antall kryptografer] [filnavn]");
			return;
		}
		new Oblig6(Integer.parseInt(args[0]), Integer.parseInt(args[1]), args[2]);
	}

	public void startArbeidere() {
		for (Thread t: this.arbeidere) {
			t.start();
		}
	}
}
