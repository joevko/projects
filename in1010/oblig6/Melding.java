public class Melding implements Comparable<Melding> {

	private String melding;
	private int sekvensnummer;
	private int kanalId;


	public Melding(String melding, int kanalId, int sekvensnummer) {
		this.melding = melding;
		this.kanalId = kanalId;
		this.sekvensnummer = sekvensnummer;
	}

	public String toString() {
		return this.melding;
	}

	public int getKanalId() {
		return this.kanalId;	
	}

	public int getSekvensnummer() {
		return this.sekvensnummer;
	}

	public int compareTo(Melding melding) {
		if (this.kanalId == melding.kanalId) {
			return this.getSekvensnummer() - melding.getSekvensnummer();
		}
		return this.getKanalId() - melding.getKanalId();
	}
}