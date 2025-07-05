class Location:
    def __init__(self, name, lat, lng, description):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "latitude": self.lat,
            "longitude": self.lng,
            "description": self.description
        }

class LocationManager:
    def __init__(self):
        self.locations = []

    def add_location(self, location):
        self.locations.append(location)

    def find_by_name(self, name):
        return [loc for loc in self.locations if loc.name.lower() == name.lower()]

    def get_all(self):
        return [loc.to_dict() for loc in self.locations]

def create_sample_data():
    manager = LocationManager()
    manager.add_location(Location("Library", 28.236, 83.993, "Main library with extensive resources."))
    manager.add_location(Location("Student Success Center", 28.237, 83.994, "Support center for student success."))
    manager.add_location(Location("Sandell Hall", 28.238, 83.995, "Academic building with classrooms."))
    manager.add_location(Location("HUB", 28.239, 83.996, "Dining and student life center."))
    manager.add_location(Location("BCM", 28.240, 83.997, "Baptist Collegiate Ministry building."))
    manager.add_location(Location("Madison Hall", 28.241, 83.998, "Student residence hall."))
    return manager

if __name__ == "__main__":
    data = create_sample_data()
    for loc in data.get_all():
        print(loc)

class Building:
    def __init__(self, name, latitude, longitude, description, category):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.category = category

    def to_dict(self):
        return {
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "description": self.description,
            "category": self.category
        }

    def format_info(self):
        return f"{self.name} ({self.latitude}, {self.longitude}) - {self.description} [{self.category}]"


class BuildingRepository:
    def __init__(self):
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

    def find_by_name(self, name):
        return [b for b in self.buildings if b.name.lower() == name.lower()]

    def find_by_category(self, category):
        return [b for b in self.buildings if b.category.lower() == category.lower()]

    def get_all(self):
        return self.buildings

    def format_all(self):
        return [b.format_info() for b in self.buildings]


def create_sample_repository():
    repo = BuildingRepository()
    repo.add_building(Building("Library", 28.236, 83.993, "Main library with extensive collections.", "Academic"))
    repo.add_building(Building("Student Success Center", 28.237, 83.994, "Support and resources for all students.", "Support"))
    repo.add_building(Building("Sandell Hall", 28.238, 83.995, "Academic building with classrooms and labs.", "Academic"))
    repo.add_building(Building("HUB", 28.239, 83.996, "Dining and student life center.", "Recreation"))
    repo.add_building(Building("BCM", 28.240, 83.997, "Baptist Collegiate Ministry.", "Religious"))
    repo.add_building(Building("Madison Hall", 28.241, 83.998, "Residence hall for students.", "Housing"))
    repo.add_building(Building("Kitty Degree Hall", 28.242, 83.999, "Lecture halls and event spaces.", "Academic"))
    repo.add_building(Building("Sugar Hall", 28.243, 84.000, "Engineering and science facilities.", "Academic"))
    repo.add_building(Building("Hanna Hall", 28.244, 84.001, "Faculty offices and classrooms.", "Academic"))
    return repo


def generate_report(buildings):
    lines = []
    for b in buildings:
        lines.append(b.format_info())
    return "\n".join(lines)


def export_to_json(buildings):
    import json
    data = [b.to_dict() for b in buildings]
    return json.dumps(data, indent=2)


def search_and_report(repo, search_term):
    results = repo.find_by_name(search_term)
    if not results:
        return f"No buildings found matching '{search_term}'."
    return generate_report(results)


def main():
    repo = create_sample_repository()
    print("All Buildings:\n")
    print(generate_report(repo.get_all()))
    print("\nFiltered by category 'Academic':\n")
    academic = repo.find_by_category("Academic")
    print(generate_report(academic))
    print("\nExporting JSON:\n")
    print(export_to_json(repo.get_all()))
    print("\nSearching for 'Library':\n")
    print(search_and_report(repo, "Library"))
    print("\nSearching for 'Gym':\n")
    print(search_and_report(repo, "Gym"))


class BuildingStatistics:
    def __init__(self, buildings):
        self.buildings = buildings

    def count_by_category(self):
        counts = {}
        for b in self.buildings:
            cat = b.category
            if cat not in counts:
                counts[cat] = 0
            counts[cat] += 1
        return counts

    def average_latitude(self):
        if not self.buildings:
            return 0
        return sum(b.latitude for b in self.buildings) / len(self.buildings)

    def average_longitude(self):
        if not self.buildings:
            return 0
        return sum(b.longitude for b in self.buildings) / len(self.buildings)


def print_statistics(repo):
    stats = BuildingStatistics(repo.get_all())
    counts = stats.count_by_category()
    print("\nBuilding Counts by Category:")
    for category, count in counts.items():
        print(f"{category}: {count}")
    print(f"\nAverage Latitude: {stats.average_latitude():.6f}")
    print(f"Average Longitude: {stats.average_longitude():.6f}")


def display_detailed_list(buildings):
    for idx, b in enumerate(buildings, start=1):
        print(f"{idx}. {b.format_info()}")


def find_and_display(repo, category):
    print(f"\nBuildings in category '{category}':")
    results = repo.find_by_category(category)
    if results:
        display_detailed_list(results)
    else:
        print("No buildings found.")


if __name__ == "__main__":
    main()
    repo = create_sample_repository()
    print_statistics(repo)
    find_and_display(repo, "Housing")
    find_and_display(repo, "Religious")
    find_and_display(repo, "Recreation")
