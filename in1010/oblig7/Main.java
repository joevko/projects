import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.LinkedList;

public class Main extends Application {
    Stage primaryStage;
    Labyrint labyrint;
    LabyrintGrid labyrintGrid;
    HashMap<String, RuteRect> hviteRuter;
    LinkedList<String> losninger;
    int losningIndex = 0;
    Label label;

    @Override
    public void start(Stage primaryStage) throws Exception {
        this.hviteRuter = new HashMap<String, RuteRect>();
        this.labyrintGrid = new LabyrintGrid();
        primaryStage.setTitle("Hello World");
        primaryStage.show();
        this.primaryStage = primaryStage;
        File file = this.chooseFile();
        this.labyrint = lagLabyrint(file);
        this.primaryStage.setScene(new Scene(
                this.labyrintGrid,
                this.labyrint.getKolonner() * Settings.RECT_HEIGHT_WIDTH + 120,
                this.labyrint.getRader() * Settings.RECT_HEIGHT_WIDTH)
        );
        this.label = new Label();
        this.drawGrid();
    }

    public void drawSolution () {
        for (RuteRect r: this.hviteRuter.values()) {
            r.setFill(Settings.getWalkableColor());
            r.setFillColors(Settings.getWalkableColor(), Settings.getWalkableSecondaryColor());
        }
        String path = this.losninger.get(this.losningIndex);
        for (String p : path.split(" -> ")) {
            RuteRect r = this.hviteRuter.get(p);
            r.setFillColors(Settings.getPathColor(), Settings.getPathSecondaryColor());
            r.setFill(Settings.getPathColor());
        }
        this.label.setText("Løsninger: " + this.losninger.size());
    }

    public void finnLosning (Rute rute) {
        this.losningIndex = 0;
        this.losninger = this.labyrint.finnUtveiFra(rute);
        if (this.losninger == null) {
            this.label.setText("Ingen løsninger");
        } else {
            this.drawSolution();
        }
    }

    public RuteRect createRuteRect (Rute rute) {
        if (rute instanceof SortRute) {
            return RuteRect.SortRute();
        } else {
            RuteRect ruteRect = RuteRect.HvitRute(rute, this);
            this.hviteRuter.put(rute.getCoords(), ruteRect);
            return ruteRect;
        }
    }

    public void drawGrid () {
        Rute[][] ruter = this.labyrint.getRuter();
        for (Rute[] rr : ruter) {
            for (Rute r : rr) {
                this.labyrintGrid.add(this.createRuteRect(r), r.getKolonne(), r.getRad());
            }
        }
        this.labyrintGrid.add(this.label, this.labyrint.getRader(), 0);
    }

    private Labyrint lagLabyrint(File file) throws FileNotFoundException {
        return Labyrint.lesFraFil(file);
    }

    private File chooseFile() {
        FileChooser fileChooser = new FileChooser();
        return fileChooser.showOpenDialog(this.primaryStage);
    }

    public static void main(String[] args) {
        launch(args);
    }
}
