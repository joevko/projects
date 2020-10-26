import java.util.ArrayList;

public class MonitorDekryptert {

	private ArrayList<Melding> meldinger;

	//variabel for å holde orden på hvor mange kryptografer som jobber med monitoren.
	private int antallKryptografer;

	public MonitorDekryptert() {
		this.meldinger = new ArrayList<Melding>();
		this.antallKryptografer = -1;
	}

	public synchronized void incAntallKryptografer() {
		if (this.antallKryptografer == -1) {
			this.antallKryptografer = 1;
		} else {
			this.antallKryptografer++;
		}
	}

	public synchronized void decAntallKryptografer() {
		this.antallKryptografer--;
		notifyAll();
	}

	//Setter inn melding i monitor og gir beskjed til operasjonsleder tråden om at vi kanskje er ferdig
	public synchronized void settInnMelding(Melding melding) {
		this.meldinger.add(melding);
		notifyAll();
	}

	//hvis det antallKryptografer er 0 så er alle meldingen ferdig kryptert
	//og operasjonslederen kan hente alle meldingene
	//hvis ikke så venter operasjonslederen.
	public synchronized ArrayList<Melding> hentMeldinger() {
		while (this.antallKryptografer == -1 || this.antallKryptografer > 0){
			try {
				wait();
			} catch (InterruptedException e) {}
		}
		return this.meldinger;
	}
}
