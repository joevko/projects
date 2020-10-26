public class Telegrafist extends Thread{

	private Kanal kanal;
	private MonitorKryptert monitor;

	public Telegrafist(Kanal kanal, MonitorKryptert monitor) {
		this.kanal = kanal;
		this.monitor = monitor;
	}

	//Lytter på kanal, oppretter melding med sekvensnummer og kanal id og setter melding inn i monitor kryptert
	public void run() {
		this.monitor.incAntallTelegrafister();
		String melding = null;
		int sekvensnummer = 0;

			while ((melding = this.kanal.lytt()) != null) {
				this.monitor.settInnMelding(
					new Melding(melding, this.kanal.hentId(), sekvensnummer++));
			}

		this.monitor.decAntallTelegrafister();
	}
}
