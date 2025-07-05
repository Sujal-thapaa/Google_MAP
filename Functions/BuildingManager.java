import java.util.ArrayList;
import java.util.List;

public class BuildingManager {

    public static class Building {
        private String name;
        private double latitude;
        private double longitude;
        private String description;
        private String category;

        public Building(String name, double latitude, double longitude, String description, String category) {
            this.name = name;
            this.latitude = latitude;
            this.longitude = longitude;
            this.description = description;
            this.category = category;
        }

        public String getName() {
            return name;
        }

        public double getLatitude() {
            return latitude;
        }

        public double getLongitude() {
            return longitude;
        }

        public String getDescription() {
            return description;
        }

        public String getCategory() {
            return category;
        }

        public String formatDetails() {
            return name + " (" + latitude + ", " + longitude + ") - " + description + " [" + category + "]";
        }
    }

    private List<Building> buildings;

    public BuildingManager() {
        buildings = new ArrayList<>();
    }

    public void addBuilding(Building building) {
        buildings.add(building);
    }

    public List<Building> findByCategory(String category) {
        List<Building> result = new ArrayList<>();
        for (Building b : buildings) {
            if (b.getCategory().equalsIgnoreCase(category)) {
                result.add(b);
            }
        }
        return result;
    }

    public Building findByName(String name) {
        for (Building b : buildings) {
            if (b.getName().equalsIgnoreCase(name)) {
                return b;
            }
        }
        return null;
    }

    public List<Building> getAllBuildings() {
        return buildings;
    }

    public int countBuildings() {
        return buildings.size();
    }

    public static void printBuildingList(List<Building> list) {
        for (Building b : list) {
            System.out.println(b.formatDetails());
        }
    }

    public static void printCategoryCounts(BuildingManager manager) {
        List<String> categories = new ArrayList<>();
        for (Building b : manager.getAllBuildings()) {
            if (!categories.contains(b.getCategory())) {
                categories.add(b.getCategory());
            }
        }
        for (String category : categories) {
            int count = manager.findByCategory(category).size();
            System.out.println(category + ": " + count);
        }
    }

    public static void main(String[] args) {
        BuildingManager manager = new BuildingManager();

        manager.addBuilding(new Building("Library", 28.236, 83.993, "Main library with extensive collections.", "Academic"));
        manager.addBuilding(new Building("Student Success Center", 28.237, 83.994, "Support center for all students.", "Support"));
        manager.addBuilding(new Building("Sandell Hall", 28.238, 83.995, "Classrooms and labs.", "Academic"));
        manager.addBuilding(new Building("HUB", 28.239, 83.996, "Dining and student activities.", "Recreation"));
        manager.addBuilding(new Building("BCM", 28.240, 83.997, "Ministry center.", "Religious"));
        manager.addBuilding(new Building("Madison Hall", 28.241, 83.998, "Residence hall for students.", "Housing"));
        manager.addBuilding(new Building("Kitty Degree Hall", 28.242, 83.999, "Lecture halls and events.", "Academic"));
        manager.addBuilding(new Building("Sugar Hall", 28.243, 84.000, "Engineering and science facilities.", "Academic"));
        manager.addBuilding(new Building("Hanna Hall", 28.244, 84.001, "Faculty offices and classrooms.", "Academic"));

        System.out.println("All Buildings:");
        printBuildingList(manager.getAllBuildings());

        System.out.println("\nCategory Counts:");
        printCategoryCounts(manager);

        System.out.println("\nBuildings in Academic Category:");
        List<Building> academic = manager.findByCategory("Academic");
        printBuildingList(academic);

        System.out.println("\nSearching for 'Library':");
        Building library = manager.findByName("Library");
        if (library != null) {
            System.out.println(library.formatDetails());
        } else {
            System.out.println("Not found.");
        }

        System.out.println("\nSearching for 'Gym':");
        Building gym = manager.findByName("Gym");
        if (gym != null) {
            System.out.println(gym.formatDetails());
        } else {
            System.out.println("Not found.");
        }

        System.out.println("\nSummary Statistics:");
        System.out.println("Total Buildings: " + manager.countBuildings());
        double avgLat = calculateAverageLatitude(manager);
        double avgLng = calculateAverageLongitude(manager);
        System.out.printf("Average Latitude: %.6f\n", avgLat);
        System.out.printf("Average Longitude: %.6f\n", avgLng);
    }

    public static double calculateAverageLatitude(BuildingManager manager) {
        double total = 0;
        List<Building> list = manager.getAllBuildings();
        for (Building b : list) {
            total += b.getLatitude();
        }
        return list.size() > 0 ? total / list.size() : 0;
    }

    public static double calculateAverageLongitude(BuildingManager manager) {
        double total = 0;
        List<Building> list = manager.getAllBuildings();
        for (Building b : list) {
            total += b.getLongitude();
        }
        return list.size() > 0 ? total / list.size() : 0;
    }
}
