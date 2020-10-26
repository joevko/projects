public class Kryptograf extends Thread {

	MonitorKryptert monitorKryptert;
	MonitorDekryptert monitorDekryptert;

	public Kryptograf(MonitorKryptert monitorKryptert, MonitorDekryptert monitorDekryptert) {
		this.monitorKryptert = monitorKryptert;
		this.monitorDekryptert = monitorDekryptert;
	}

	//Henter meldinger fra kryptert monitor, krypterer dem og setter dem i dekryptert monitoren
	//Når det ikke er flere meldinger igjen i dekryptert monitor så avslutter tråden
	public void run() {
		Melding melding = null;
		this.monitorDekryptert.incAntallKryptografer();
		while ((melding = this.monitorKryptert.hentMelding()) != null) {
			Melding m = new Melding(
				Kryptografi.dekrypter(
					melding.toString()),
					melding.getKanalId(),
					melding.getSekvensnummer()
				);
			this.monitorDekryptert.settInnMelding(m);
		}
		this.monitorDekryptert.decAntallKryptografer();
	}
}
