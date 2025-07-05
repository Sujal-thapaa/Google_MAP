using System;
using System.Collections.Generic;
using System.Linq;

public class Building
{
    public string Name { get; set; }
    public double Latitude { get; set; }
    public double Longitude { get; set; }
    public string Description { get; set; }
    public string Category { get; set; }

    public string GetInfo()
    {
        return $"{Name} ({Latitude}, {Longitude}) - {Description} [{Category}]";
    }
}

public class BuildingRepository
{
    private List<Building> buildings;

    public BuildingRepository()
    {
        buildings = new List<Building>();
    }

    public void Add(Building building)
    {
        buildings.Add(building);
    }

    public List<Building> GetAll()
    {
        return buildings;
    }

    public Building FindByName(string name)
    {
        return buildings.FirstOrDefault(b => b.Name.Equals(name, StringComparison.OrdinalIgnoreCase));
    }

    public List<Building> FindByCategory(string category)
    {
        return buildings.Where(b => b.Category.Equals(category, StringComparison.OrdinalIgnoreCase)).ToList();
    }

    public int Count()
    {
        return buildings.Count;
    }

    public Dictionary<string, int> CountByCategory()
    {
        var counts = new Dictionary<string, int>();
        foreach (var b in buildings)
        {
            if (!counts.ContainsKey(b.Category))
            {
                counts[b.Category] = 0;
            }
            counts[b.Category]++;
        }
        return counts;
    }

    public double AverageLatitude()
    {
        return buildings.Count > 0 ? buildings.Average(b => b.Latitude) : 0;
    }

    public double AverageLongitude()
    {
        return buildings.Count > 0 ? buildings.Average(b => b.Longitude) : 0;
    }
}

public class BuildingPrinter
{
    public static void PrintAll(List<Building> buildings)
    {
        foreach (var b in buildings)
        {
            Console.WriteLine(b.GetInfo());
        }
    }

    public static void PrintCounts(Dictionary<string, int> counts)
    {
        foreach (var kvp in counts)
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }
    }

    public static void PrintAverageCoordinates(BuildingRepository repo)
    {
        Console.WriteLine($"Average Latitude: {repo.AverageLatitude():F6}");
        Console.WriteLine($"Average Longitude: {repo.AverageLongitude():F6}");
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        var repo = new BuildingRepository();

        repo.Add(new Building
        {
            Name = "Library",
            Latitude = 28.236,
            Longitude = 83.993,
            Description = "Main library with extensive resources.",
            Category = "Academic"
        });

        repo.Add(new Building
        {
            Name = "Student Success Center",
            Latitude = 28.237,
            Longitude = 83.994,
            Description = "Support center for student success.",
            Category = "Support"
        });

        repo.Add(new Building
        {
            Name = "Sandell Hall",
            Latitude = 28.238,
            Longitude = 83.995,
            Description = "Academic building with classrooms.",
            Category = "Academic"
        });

        repo.Add(new Building
        {
            Name = "HUB",
            Latitude = 28.239,
            Longitude = 83.996,
            Description = "Dining and student life center.",
            Category = "Recreation"
        });

        repo.Add(new Building
        {
            Name = "BCM",
            Latitude = 28.240,
            Longitude = 83.997,
            Description = "Baptist Collegiate Ministry.",
            Category = "Religious"
        });

        repo.Add(new Building
        {
            Name = "Madison Hall",
            Latitude = 28.241,
            Longitude = 83.998,
            Description = "Residence hall for students.",
            Category = "Housing"
        });

        repo.Add(new Building
        {
            Name = "Kitty Degree Hall",
            Latitude = 28.242,
            Longitude = 83.999,
            Description = "Lecture halls and event spaces.",
            Category = "Academic"
        });

        repo.Add(new Building
        {
            Name = "Sugar Hall",
            Latitude = 28.243,
            Longitude = 84.000,
            Description = "Engineering and science facilities.",
            Category = "Academic"
        });

        repo.Add(new Building
        {
            Name = "Hanna Hall",
            Latitude = 28.244,
            Longitude = 84.001,
            Description = "Faculty offices and classrooms.",
            Category = "Academic"
        });

        Console.WriteLine("All Buildings:\n");
        BuildingPrinter.PrintAll(repo.GetAll());

        Console.WriteLine("\nCounts by Category:\n");
        var counts = repo.CountByCategory();
        BuildingPrinter.PrintCounts(counts);

        Console.WriteLine("\nAverage Coordinates:\n");
        BuildingPrinter.PrintAverageCoordinates(repo);

        Console.WriteLine("\nSearching for 'Library':\n");
        var library = repo.FindByName("Library");
        if (library != null)
        {
            Console.WriteLine(library.GetInfo());
        }
        else
        {
            Console.WriteLine("Library not found.");
        }

        Console.WriteLine("\nSearching for 'Gym':\n");
        var gym = repo.FindByName("Gym");
        if (gym != null)
        {
            Console.WriteLine(gym.GetInfo());
        }
        else
        {
            Console.WriteLine("Gym not found.");
        }

        Console.WriteLine("\nAcademic Buildings:\n");
        var academic = repo.FindByCategory("Academic");
        BuildingPrinter.PrintAll(academic);
    }
}
