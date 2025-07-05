```java
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

public class BuildingManager {

    public static class Building {
        private String name;
        private double latitude;
        private double longitude;
        private String description;
        private String category;
        private int yearBuilt; // New attribute

        public Building(String name, double latitude, double longitude, String description, String category, int yearBuilt) {
            this.name = name;
            this.latitude = latitude;
            this.longitude = longitude;
            this.description = description;
            this.category = category;
            this.yearBuilt = yearBuilt;
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

        public int getYearBuilt() {
            return yearBuilt;
        }

        public String formatDetails() {
            return name + " (" + latitude + ", " + longitude + ") - " + description + " [" + category + "] - Built: " + yearBuilt;
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

    // New method: Find buildings built after a specific year
    public List<Building> findByYearBuiltAfter(int year) {
        List<Building> result = new ArrayList<>();
        for (Building b : buildings) {
            if (b.getYearBuilt() > year) {
                result.add(b);
            }
        }
        return result;
    }

    // New method: Find buildings within a certain latitude and longitude range
    public List<Building> findByLocationRange(double minLat, double maxLat, double minLong, double maxLong) {
        List<Building> result = new ArrayList<>();
        for (Building b : buildings) {
            if (b.getLatitude() >= minLat && b.getLatitude() <= maxLat &&
                b.getLongitude() >= minLong && b.getLongitude() <= maxLong) {
                result.add(b);
            }
        }
        return result;
    }

    public static void printBuildingList(List<Building> list) {
        if (list.isEmpty()) {
            System.out.println("No buildings found in this list.");
            return;
        }
        for (Building b : list) {
            System.out.println(b.formatDetails());
        }
    }

    public static void printCategoryCounts(BuildingManager manager) {
        Map<String, Integer> categoryCounts = new HashMap<>();
        for (Building b : manager.getAllBuildings()) {
            String category = b.getCategory();
            categoryCounts.put(category, categoryCounts.getOrDefault(category, 0) + 1);
        }
        for (Map.Entry<String, Integer> entry : categoryCounts.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        BuildingManager manager = new BuildingManager();

        manager.addBuilding(new Building("Library", 28.236, 83.993, "Main library with extensive collections.", "Academic", 1975));
        manager.addBuilding(new Building("Student Success Center", 28.237, 83.994, "Support center for all students.", "Support", 2005));
        manager.addBuilding(new Building("Sandell Hall", 28.238, 83.995, "Classrooms and labs.", "Academic", 1980));
        manager.addBuilding(new Building("HUB", 28.239, 83.996, "Dining and student activities.", "Recreation", 2010));
        manager.addBuilding(new Building("BCM", 28.240, 83.997, "Ministry center.", "Religious", 1995));
        manager.addBuilding(new Building("Madison Hall", 28.241, 83.998, "Residence hall for students.", "Housing", 1968));
        manager.addBuilding(new Building("Kitty Degree Hall", 28.242, 83.999, "Lecture halls and events.", "Academic", 2001));
        manager.addBuilding(new Building("Sugar Hall", 28.243, 84.000, "Engineering and science facilities.", "Academic", 1988));
        manager.addBuilding(new Building("Hanna Hall", 28.244, 84.001, "Faculty offices and classrooms.", "Academic", 1972));
        manager.addBuilding(new Building("University Bookstore", 28.245, 84.002, "Textbooks, supplies, and apparel.", "Retail", 2008));
        manager.addBuilding(new Building("Health Center", 28.246, 84.003, "Student medical services.", "Health", 1999));
        manager.addBuilding(new Building("Performing Arts Center", 28.247, 84.004, "Theater and music venues.", "Arts", 2012));
        manager.addBuilding(new Building("Athletic Complex", 28.248, 84.005, "Sports facilities and gym.", "Recreation", 2003));
        manager.addBuilding(new Building("Alumni Center", 28.249, 84.006, "Alumni relations and events.", "Administration", 1990));
        manager.addBuilding(new Building("President's Office", 28.250, 84.007, "University administration headquarters.", "Administration", 1955));
        manager.addBuilding(new Building("Dining Hall East", 28.251, 84.008, "Additional campus dining option.", "Food Service", 1985));
        manager.addBuilding(new Building("Research Lab 1", 28.252, 84.009, "Specialized science research facility.", "Academic", 2015));
        manager.addBuilding(new Building("Career Services", 28.253, 84.010, "Job placement and internship assistance.", "Support", 2007));
        manager.addBuilding(new Building("Technology Center", 28.254, 84.011, "IT support and computer labs.", "Academic", 2000));
        manager.addBuilding(new Building("Student Union Annex", 28.255, 84.012, "Meeting rooms and student organization offices.", "Recreation", 2006));
        manager.addBuilding(new Building("Nursing Building", 28.256, 84.013, "Nursing program classrooms and labs.", "Academic", 1998));
        manager.addBuilding(new Building("Art Studio", 28.257, 84.014, "Visual arts instruction and creation space.", "Arts", 1970));
        manager.addBuilding(new Building("Faculty Club", 28.258, 84.015, "Private club for faculty members.", "Social", 1965));
        manager.addBuilding(new Building("South Residence Hall", 28.259, 84.016, "Another student residence.", "Housing", 1978));
        manager.addBuilding(new Building("North Campus Apartments", 28.260, 84.017, "University-affiliated off-campus housing.", "Housing", 2011));
        manager.addBuilding(new Building("Law School Building", 28.261, 84.018, "Home to the university's law program.", "Academic", 1992));
        manager.addBuilding(new Building("Business School", 28.262, 84.019, "College of Business administration and classrooms.", "Academic", 1983));
        manager.addBuilding(new Building("Education Building", 28.263, 84.020, "College of Education facilities.", "Academic", 1977));
        manager.addBuilding(new Building("Campus Police Station", 28.264, 84.021, "Campus security and emergency services.", "Safety", 1989));
        manager.addBuilding(new Building("Botanical Gardens Office", 28.265, 84.022, "Administration for the campus botanical gardens.", "Administration", 1960));
        manager.addBuilding(new Building("Aquatics Center", 28.266, 84.023, "Indoor and outdoor pools for recreation and sports.", "Recreation", 2002));
        manager.addBuilding(new Building("Child Development Center", 28.267, 84.024, "On-campus childcare and early education.", "Support", 1996));
        manager.addBuilding(new Building("Engineering Research Center", 28.268, 84.025, "Advanced engineering research facilities.", "Academic", 2018));
        manager.addBuilding(new Building("Humanities Building", 28.269, 84.026, "Departments for literature, history, and philosophy.", "Academic", 1973));
        manager.addBuilding(new Building("Music Recital Hall", 28.270, 84.027, "Concert venue for music performances.", "Arts", 2009));
        manager.addBuilding(new Building("Gymnasium Annex", 28.271, 84.028, "Additional courts and fitness areas.", "Recreation", 1997));
        manager.addBuilding(new Building("Financial Aid Office", 28.272, 84.029, "Assistance with student financial planning.", "Support", 1987));
        manager.addBuilding(new Building("Chemistry Lab Building", 28.273, 84.030, "Dedicated chemistry research and teaching labs.", "Academic", 2004));
        manager.addBuilding(new Building("Student Health Annex", 28.274, 84.031, "Expanded health services for students.", "Health", 2013));
        manager.addBuilding(new Building("International Student Office", 28.275, 84.032, "Support for international students.", "Support", 2000));
        manager.addBuilding(new Building("Veterinary Clinic", 28.276, 84.033, "Animal care and veterinary studies.", "Academic", 2016));
        manager.addBuilding(new Building("Campus Ministry Center", 28.277, 84.034, "Additional religious services and student groups.", "Religious", 1993));
        manager.addBuilding(new Building("Public Safety Building", 28.278, 84.035, "Central hub for campus safety operations.", "Safety", 2001));
        manager.addBuilding(new Building("Greenhouse Complex", 28.279, 84.036, "Facilities for plant science research.", "Academic", 1991));
        manager.addBuilding(new Building("Welcome Center", 28.280, 84.037, "First stop for campus visitors and tours.", "Administration", 2017));
        manager.addBuilding(new Building("Food Court North", 28.281, 84.038, "Variety of dining options on north campus.", "Food Service", 2014));
        manager.addBuilding(new Building("Performing Arts Annex", 28.282, 84.039, "Rehearsal spaces and smaller performance rooms.", "Arts", 2005));
        manager.addBuilding(new Building("Athletic Training Facility", 28.283, 84.040, "Sports medicine and rehabilitation services.", "Recreation", 2019));
        manager.addBuilding(new Building("Student Government Office", 28.284, 84.041, "Headquarters for student leadership.", "Support", 1982));
        manager.addBuilding(new Building("Earth Sciences Building", 28.285, 84.042, "Geology and environmental science departments.", "Academic", 1979));
        manager.addBuilding(new Building("Parking Garage A", 28.286, 84.043, "Multi-level parking structure.", "Parking", 2008));
        manager.addBuilding(new Building("Parking Garage B", 28.287, 84.044, "Another multi-level parking structure.", "Parking", 2010));
        manager.addBuilding(new Building("University Press", 28.288, 84.045, "Publishing arm of the university.", "Administration", 1963));
        manager.addBuilding(new Building("Disability Services", 28.289, 84.046, "Support for students with disabilities.", "Support", 1994));
        manager.addBuilding(new Building("IT Services Help Desk", 28.290, 84.047, "Walk-in technical support.", "Support", 2003));
        manager.addBuilding(new Building("Counseling Center", 28.291, 84.048, "Mental health and wellness support.", "Health", 1997));
        manager.addBuilding(new Building("Campus Mailroom", 28.292, 84.049, "Mail and package services for students and staff.", "Service", 1986));
        manager.addBuilding(new Building("Campus Print Shop", 28.293, 84.050, "Printing and design services.", "Service", 2006));
        manager.addBuilding(new Building("Outdoor Adventure Center", 28.294, 84.051, "Equipment rental and trip planning for outdoor activities.", "Recreation", 2012));
        manager.addBuilding(new Building("Student Recreation Fields", 28.295, 84.052, "Outdoor fields for various sports.", "Recreation", 2001));
        manager.addBuilding(new Building("Conference Center", 28.296, 84.053, "Venue for conferences and large events.", "Administration", 2009));
        manager.addBuilding(new Building("Campus Museum", 28.297, 84.054, "Exhibits and collections for education and research.", "Arts", 1971));
        manager.addBuilding(new Building("Observatory", 28.298, 84.055, "Astronomical research and public viewing.", "Academic", 1980));
        manager.addBuilding(new Building("Veterans Affairs Office", 28.299, 84.056, "Support for student veterans.", "Support", 2007));
        manager.addBuilding(new Building("Campus Green", 28.300, 84.057, "Open space for outdoor events and relaxation.", "Recreation", 1950));
        manager.addBuilding(new Building("Research Greenhouse 2", 28.301, 84.058, "Additional greenhouse facilities for advanced research.", "Academic", 2011));
        manager.addBuilding(new Building("Food Truck Zone", 28.302, 84.059, "Designated area for mobile food vendors.", "Food Service", 2015));


        System.out.println("---");
        System.out.println("All Buildings:");
        printBuildingList(manager.getAllBuildings());

        System.out.println("\n---");
        System.out.println("Category Counts:");
        printCategoryCounts(manager);

        System.out.println("\n---");
        System.out.println("Buildings in Academic Category:");
        List<Building> academic = manager.findByCategory("Academic");
        printBuildingList(academic);

        System.out.println("\n---");
        System.out.println("Buildings in Housing Category:");
        List<Building> housing = manager.findByCategory("Housing");
        printBuildingList(housing);

        System.out.println("\n---");
        System.out.println("Searching for 'Library':");
        Building library = manager.findByName("Library");
        if (library != null) {
            System.out.println(library.formatDetails());
        } else {
            System.out.println("Not found.");
        }

        System.out.println("\n---");
        System.out.println("Searching for 'Gym':");
        Building gym = manager.findByName("Gym");
        if (gym != null) {
            System.out.println(gym.formatDetails());
        } else {
            System.out.println("Not found.");
        }

        System.out.println("\n---");
        System.out.println("Searching for 'Athletic Complex':");
        Building athleticComplex = manager.findByName("Athletic Complex");
        if (athleticComplex != null) {
            System.out.println(athleticComplex.formatDetails());
        } else {
            System.out.println("Not found.");
        }

        System.out.println("\n---");
        System.out.println("Buildings built after 2000:");
        List<Building> builtAfter2000 = manager.findByYearBuiltAfter(2000);
        printBuildingList(builtAfter2000);

        System.out.println("\n---");
        System.out.println("Buildings within latitude 28.250-28.270 and longitude 84.000-84.020:");
        List<Building> specificArea = manager.findByLocationRange(28.250, 28.270, 84.000, 84.020);
        printBuildingList(specificArea);


        System.out.println("\n---");
        System.out.println("Summary Statistics:");
        System.out.println("Total Buildings: " + manager.countBuildings());
        double avgLat = calculateAverageLatitude(manager);
        double avgLng = calculateAverageLongitude(manager);
        System.out.printf("Average Latitude: %.6f\n", avgLat);
        System.out.printf("Average Longitude: %.6f\n", avgLng);

        System.out.println("Average Year Built: " + calculateAverageYearBuilt(manager));
        System.out.println("Oldest Building: " + findOldestBuilding(manager).getName() + " (Built: " + findOldestBuilding(manager).getYearBuilt() + ")");
        System.out.println("Newest Building: " + findNewestBuilding(manager).getName() + " (Built: " + findNewestBuilding(manager).getYearBuilt() + ")");
    }

    public static double calculateAverageLatitude(BuildingManager manager) {
        double total = 0;
        List<Building> list = manager.getAllBuildings();
        if (list.isEmpty()) return 0;
        for (Building b : list) {
            total += b.getLatitude();
        }
        return total / list.size();
    }

    public static double calculateAverageLongitude(BuildingManager manager) {
        double total = 0;
        List<Building> list = manager.getAllBuildings();
        if (list.isEmpty()) return 0;
        for (Building b : list) {
            total += b.getLongitude();
        }
        return total / list.size();
    }

    // New method: Calculate average year built
    public static double calculateAverageYearBuilt(BuildingManager manager) {
        double total = 0;
        List<Building> list = manager.getAllBuildings();
        if (list.isEmpty()) return 0;
        for (Building b : list) {
            total += b.getYearBuilt();
        }
        return total / list.size();
    }

    // New method: Find the oldest building
    public static Building findOldestBuilding(BuildingManager manager) {
        List<Building> list = manager.getAllBuildings();
        if (list.isEmpty()) return null;
        Building oldest = list.get(0);
        for (Building b : list) {
            if (b.getYearBuilt() < oldest.getYearBuilt()) {
                oldest = b;
            }
        }
        return oldest;
    }

    // New method: Find the newest building
    public static Building findNewestBuilding(BuildingManager manager) {
        List<Building> list = manager.getAllBuildings();
        if (list.isEmpty()) return null;
        Building newest = list.get(0);
        for (Building b : list) {
            if (b.getYearBuilt() > newest.getYearBuilt()) {
                newest = b;
            }
        }
        return newest;
    }
}
