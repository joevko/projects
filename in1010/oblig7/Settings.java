import javafx.scene.paint.Color;

public class Settings {
    public static final String WALL_COLOR_PRIMARY = "#454851";
    public static final String PATH_COLOR_PRIMARY = "25CED1";
    public static final String PATH_COLOR_SECONDARY = "#9BE8EA";
    public static final String WALKABLE_COLOR_PRIMARY = "#BBBDF6";
    public static final String WALKABLE_COLOR_SECONDARY = "#D3D5F9";
    public static final double RECT_HEIGHT_WIDTH = 20;

    public static Color getWallColor () {
        return Color.web(Settings.WALL_COLOR_PRIMARY);
    }

    public static Color getPathColor () {
        return Color.web(Settings.PATH_COLOR_PRIMARY);
    }

    public static Color getWalkableColor () {
        return Color.web(Settings.WALKABLE_COLOR_PRIMARY);
    }

    public static Color getWalkableSecondaryColor() {
        return Color.web(Settings.WALKABLE_COLOR_SECONDARY);
    }

    public static Color getPathSecondaryColor() {
        return Color.web(Settings.PATH_COLOR_SECONDARY);
    }
}
