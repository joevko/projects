import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class RuteRect extends Rectangle {
    private Color primaryColor;
    private Color secondaryColor;

    public static RuteRect HvitRute(Rute rute, Main main) {
        return new RuteRect(Settings.getWalkableColor(), Settings.getWalkableSecondaryColor(), rute, main);
    }

    public static RuteRect SortRute() {
        return new RuteRect(Settings.getWallColor());
    }

    public RuteRect (Color color) {
        super(Settings.RECT_HEIGHT_WIDTH, Settings.RECT_HEIGHT_WIDTH, color);
    }

    public RuteRect (Color primary, Color secondary, Rute rute, Main main) {
        super(Settings.RECT_HEIGHT_WIDTH, Settings.RECT_HEIGHT_WIDTH, primary);
        this.primaryColor = primary;
        this.secondaryColor = secondary;

        this.setOnMouseEntered(event -> {
            this.setFill(this.secondaryColor);
        });
        this.setOnMouseExited(event -> {
            this.setFill(this.primaryColor);
        });
        this.setOnMouseClicked(event -> {
            main.finnLosning(rute);
        });
    }

    public void setFillColors(Color primaryColor, Color secondaryColor) {
        this.primaryColor = primaryColor;
        this.secondaryColor = secondaryColor;
    }

    public void setPathColor() {
        this.setFill(Settings.getPathColor());
    }
}
