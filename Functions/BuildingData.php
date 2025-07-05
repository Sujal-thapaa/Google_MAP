<?php

class Building
{
    private $name;
    private $latitude;
    private $longitude;
    private $description;
    private $category;

    public function __construct($name, $latitude, $longitude, $description, $category)
    {
        $this->name = $name;
        $this->latitude = $latitude;
        $this->longitude = $longitude;
        $this->description = $description;
        $this->category = $category;
    }

    public function getName()
    {
        return $this->name;
    }

    public function getLatitude()
    {
        return $this->latitude;
    }

    public function getLongitude()
    {
        return $this->longitude;
    }

    public function getDescription()
    {
        return $this->description;
    }

    public function getCategory()
    {
        return $this->category;
    }

    public function formatDetails()
    {
        return $this->name . " (" . $this->latitude . ", " . $this->longitude . ") - " . $this->description . " [" . $this->category . "]";
    }
}

class BuildingRepository
{
    private $buildings = array();

    public function add(Building $building)
    {
        $this->buildings[] = $building;
    }

    public function getAll()
    {
        return $this->buildings;
    }

    public function findByName($name)
    {
        foreach ($this->buildings as $b) {
            if (strcasecmp($b->getName(), $name) === 0) {
                return $b;
            }
        }
        return null;
    }

    public function findByCategory($category)
    {
        $result = array();
        foreach ($this->buildings as $b) {
            if (strcasecmp($b->getCategory(), $category) === 0) {
                $result[] = $b;
            }
        }
        return $result;
    }

    public function count()
    {
        return count($this->buildings);
    }

    public function countByCategory()
    {
        $counts = array();
        foreach ($this->buildings as $b) {
            $cat = $b->getCategory();
            if (!isset($counts[$cat])) {
                $counts[$cat] = 0;
            }
            $counts[$cat]++;
        }
        return $counts;
    }

    public function averageLatitude()
    {
        $total = 0;
        foreach ($this->buildings as $b) {
            $total += $b->getLatitude();
        }
        return $this->count() > 0 ? $total / $this->count() : 0;
    }

    public function averageLongitude()
    {
        $total = 0;
        foreach ($this->buildings as $b) {
            $total += $b->getLongitude();
        }
        return $this->count() > 0 ? $total / $this->count() : 0;
    }
}

function printBuildingList($buildings)
{
    foreach ($buildings as $b) {
        echo $b->formatDetails() . "\n";
    }
}

function printCounts($counts)
{
    foreach ($counts as $category => $count) {
        echo $category . ": " . $count . "\n";
    }
}

function printAverageCoordinates(BuildingRepository $repo)
{
    echo "Average Latitude: " . number_format($repo->averageLatitude(), 6) . "\n";
    echo "Average Longitude: " . number_format($repo->averageLongitude(), 6) . "\n";
}

function createSampleRepository()
{
    $repo = new BuildingRepository();
    $repo->add(new Building("Library", 28.236, 83.993, "Main library with extensive collections.", "Academic"));
    $repo->add(new Building("Student Success Center", 28.237, 83.994, "Support center for students.", "Support"));
    $repo->add(new Building("Sandell Hall", 28.238, 83.995, "Classrooms and labs.", "Academic"));
    $repo->add(new Building("HUB", 28.239, 83.996, "Dining and activities center.", "Recreation"));
    $repo->add(new Building("BCM", 28.240, 83.997, "Ministry building.", "Religious"));
    $repo->add(new Building("Madison Hall", 28.241, 83.998, "Residence hall.", "Housing"));
    $repo->add(new Building("Kitty Degree Hall", 28.242, 83.999, "Lecture halls.", "Academic"));
    $repo->add(new Building("Sugar Hall", 28.243, 84.000, "Engineering facilities.", "Academic"));
    $repo->add(new Building("Hanna Hall", 28.244, 84.001, "Faculty offices.", "Academic"));
    return $repo;
}

function searchAndPrint($repo, $name)
{
    echo "\nSearching for '{$name}':\n";
    $building = $repo->findByName($name);
    if ($building) {
        echo $building->formatDetails() . "\n";
    } else {
        echo "Not found.\n";
    }
}

function printCategory($repo, $category)
{
    echo "\nBuildings in category '{$category}':\n";
    $list = $repo->findByCategory($category);
    if ($list) {
        printBuildingList($list);
    } else {
        echo "No buildings found.\n";
    }
}

// Main execution
$repo = createSampleRepository();

echo "All Buildings:\n";
printBuildingList($repo->getAll());

echo "\nCounts by Category:\n";
$counts = $repo->countByCategory();
printCounts($counts);

echo "\nAverage Coordinates:\n";
printAverageCoordinates($repo);

searchAndPrint($repo, "Library");
searchAndPrint($repo, "Gym");

printCategory($repo, "Academic");
printCategory($repo, "Housing");
printCategory($repo, "Recreation");

?>
