import java.util.*;

public class MonitorKryptert {

	private LinkedList<Melding> meldinger;

	//Variabel for å holde orden på hvor mange telegrafister som jobber med monitoren.
	private int antallTelegrafister;

	public MonitorKryptert() {
		this.meldinger = new LinkedList<Melding>();
		this.antallTelegrafister = -1;
	}

	//Setter inn melding i monitoren og gir beskjed til kryptografene at
	//en ny melding har blitt lagt til
	public synchronized void settInnMelding(Melding melding) {
		this.meldinger.push(melding);
		notifyAll();
	}

	public synchronized void incAntallTelegrafister() {
		if (this.antallTelegrafister == -1) {
			this.antallTelegrafister = 1;
		} else {
			this.antallTelegrafister++;
		}
	}

	public synchronized void decAntallTelegrafister() {
		this.antallTelegrafister--;
	}

	//Kryptografene henter en melding fra monitoren eller venter
	//hvis det ikke er noen meldinger i monitoren og telegrafistene ikke er ferdige.
	//Når alle telegrafistene er ferdige og det ikke er flere meldinger i monitoren
	//så returneres null
	public synchronized Melding hentMelding() {
		while (this.meldinger.isEmpty() && (this.antallTelegrafister == -1 || this.antallTelegrafister > 0)) {
			try {
				wait();
			} catch (InterruptedException e) {}
		}
		if (this.antallTelegrafister == 0 && this.meldinger.isEmpty()) {
			return null;
		}
		Melding melding = this.meldinger.pollLast();
		return melding;
	}
}
