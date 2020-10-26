import java.util.ArrayList;
import java.util.Collections;
import java.io.File;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Operasjonsleder extends Thread {
	private MonitorDekryptert monitor;
	private String filnavn;

	public Operasjonsleder(MonitorDekryptert monitor, String filnavn) {
		this.monitor = monitor;
		this.filnavn = filnavn;
	}

	public void skrivTilFil(String data, int kanalID) {
		try {
			String filename = hentFilnavn(kanalID);
			PrintWriter pw = new PrintWriter(new File(filename), "utf-8");
			pw.print(data);
			pw.close();
		} catch(Exception e) {

		}
	}

	//Sorterer meldingene og skriver til fil
	public void run() {
		ArrayList<Melding> meldinger = this.monitor.hentMeldinger();
		Collections.sort(meldinger);
		String filename = null;
		int kanalID = -1;
		PrintWriter pw = null;
		String data = "";
			for (int i = 0; i < meldinger.size();i++) {
				if (kanalID == -1) {
					kanalID = meldinger.get(i).getKanalId();
				}
				data += meldinger.get(i).toString() + "\n\n";
				if (meldinger.size() > i + 1 && meldinger.get(i+1).getKanalId() != kanalID) {
					this.skrivTilFil(data, kanalID);
					data = "";
					kanalID = meldinger.get(i+1).getKanalId();
				}
				else if (meldinger.size() == i + 1) {
					this.skrivTilFil(data, kanalID);
				}
			}
	}

	private String hentFilnavn(int kanalId) {
		return filnavn + "-kanal-" + kanalId + ".txt";
	}

}
