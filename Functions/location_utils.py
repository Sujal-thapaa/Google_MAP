```python
import json

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
    manager.add_location(Location("Kitty Degree Hall", 28.242, 83.999, "Lecture halls and event spaces."))
    manager.add_location(Location("Sugar Hall", 28.243, 84.000, "Engineering and science facilities."))
    manager.add_location(Location("Hanna Hall", 28.244, 84.001, "Faculty offices and classrooms."))
    manager.add_location(Location("University Bookstore", 28.245, 84.002, "Textbooks, supplies, and apparel."))
    manager.add_location(Location("Health Center", 28.246, 84.003, "Student medical services."))
    manager.add_location(Location("Performing Arts Center", 28.247, 84.004, "Theater and music venues."))
    manager.add_location(Location("Athletic Complex", 28.248, 84.005, "Sports facilities and gym."))
    manager.add_location(Location("Alumni Center", 28.249, 84.006, "Alumni relations and events."))
    manager.add_location(Location("President's Office", 28.250, 84.007, "University administration headquarters."))
    manager.add_location(Location("Dining Hall East", 28.251, 84.008, "Additional campus dining option."))
    manager.add_location(Location("Research Lab 1", 28.252, 84.009, "Specialized science research facility."))
    manager.add_location(Location("Career Services", 28.253, 84.010, "Job placement and internship assistance."))
    manager.add_location(Location("Technology Center", 28.254, 84.011, "IT support and computer labs."))
    manager.add_location(Location("Student Union Annex", 28.255, 84.012, "Meeting rooms and student organization offices."))
    manager.add_location(Location("Nursing Building", 28.256, 84.013, "Nursing program classrooms and labs."))
    manager.add_location(Location("Art Studio", 28.257, 84.014, "Visual arts instruction and creation space."))
    manager.add_location(Location("Faculty Club", 28.258, 84.015, "Private club for faculty members."))
    manager.add_location(Location("South Residence Hall", 28.259, 84.016, "Another student residence."))
    manager.add_location(Location("North Campus Apartments", 28.260, 84.017, "University-affiliated off-campus housing."))
    manager.add_location(Location("Law School Building", 28.261, 84.018, "Home to the university's law program."))
    manager.add_location(Location("Business School", 28.262, 84.019, "College of Business administration and classrooms."))
    manager.add_location(Location("Education Building", 28.263, 84.020, "College of Education facilities."))
    manager.add_location(Location("Campus Police Station", 28.264, 84.021, "Campus security and emergency services."))
    manager.add_location(Location("Botanical Gardens Office", 28.265, 84.022, "Administration for the campus botanical gardens."))
    manager.add_location(Location("Aquatics Center", 28.266, 84.023, "Indoor and outdoor pools for recreation and sports."))
    manager.add_location(Location("Child Development Center", 28.267, 84.024, "On-campus childcare and early education."))
    manager.add_location(Location("Engineering Research Center", 28.268, 84.025, "Advanced engineering research facilities."))
    manager.add_location(Location("Humanities Building", 28.269, 84.026, "Departments for literature, history, and philosophy."))
    manager.add_location(Location("Music Recital Hall", 28.270, 84.027, "Concert venue for music performances."))
    manager.add_location(Location("Gymnasium Annex", 28.271, 84.028, "Additional courts and fitness areas."))
    manager.add_location(Location("Financial Aid Office", 28.272, 84.029, "Assistance with student financial planning."))
    manager.add_location(Location("Chemistry Lab Building", 28.273, 84.030, "Dedicated chemistry research and teaching labs."))
    manager.add_location(Location("Student Health Annex", 28.274, 84.031, "Expanded health services for students."))
    manager.add_location(Location("International Student Office", 28.275, 84.032, "Support for international students."))
    manager.add_location(Location("Veterinary Clinic", 28.276, 84.033, "Animal care and veterinary studies."))
    manager.add_location(Location("Campus Ministry Center", 28.277, 84.034, "Additional religious services and student groups."))
    manager.add_location(Location("Public Safety Building", 28.278, 84.035, "Central hub for campus safety operations."))
    manager.add_location(Location("Greenhouse Complex", 28.279, 84.036, "Facilities for plant science research."))
    manager.add_location(Location("Welcome Center", 28.280, 84.037, "First stop for campus visitors and tours."))
    manager.add_location(Location("Food Court North", 28.281, 84.038, "Variety of dining options on north campus."))
    manager.add_location(Location("Performing Arts Annex", 28.282, 84.039, "Rehearsal spaces and smaller performance rooms."))
    manager.add_location(Location("Athletic Training Facility", 28.283, 84.040, "Sports medicine and rehabilitation services."))
    manager.add_location(Location("Student Government Office", 28.284, 84.041, "Headquarters for student leadership."))
    manager.add_location(Location("Earth Sciences Building", 28.285, 84.042, "Geology and environmental science departments."))
    manager.add_location(Location("Parking Garage A", 28.286, 84.043, "Multi-level parking structure."))
    manager.add_location(Location("Parking Garage B", 28.287, 84.044, "Another multi-level parking structure."))
    manager.add_location(Location("University Press", 28.288, 84.045, "Publishing arm of the university."))
    manager.add_location(Location("Disability Services", 28.289, 84.046, "Support for students with disabilities."))
    manager.add_location(Location("IT Services Help Desk", 28.290, 84.047, "Walk-in technical support."))
    manager.add_location(Location("Counseling Center", 28.291, 84.048, "Mental health and wellness support."))
    manager.add_location(Location("Campus Mailroom", 28.292, 84.049, "Mail and package services for students and staff."))
    manager.add_location(Location("Campus Print Shop", 28.293, 84.050, "Printing and design services."))
    manager.add_location(Location("Outdoor Adventure Center", 28.294, 84.051, "Equipment rental and trip planning for outdoor activities."))
    manager.add_location(Location("Student Recreation Fields", 28.295, 84.052, "Outdoor fields for various sports."))
    manager.add_location(Location("Conference Center", 28.296, 84.053, "Venue for conferences and large events."))
    manager.add_location(Location("Campus Museum", 28.297, 84.054, "Exhibits and collections for education and research."))
    manager.add_location(Location("Observatory", 28.298, 84.055, "Astronomical research and public viewing."))
    manager.add_location(Location("Veterans Affairs Office", 28.299, 84.056, "Support for student veterans."))
    manager.add_location(Location("Campus Green", 28.300, 84.057, "Open space for outdoor events and relaxation."))
    manager.add_location(Location("Research Greenhouse 2", 28.301, 84.058, "Additional greenhouse facilities for advanced research."))
    manager.add_location(Location("Food Truck Zone", 28.302, 84.059, "Designated area for mobile food vendors."))
    manager.add_location(Location("Innovation Hub", 28.303, 84.060, "Collaborative space for entrepreneurship and innovation."))
    manager.add_location(Location("Digital Arts Studio", 28.304, 84.061, "High-tech lab for digital media and design."))
    manager.add_location(Location("Interfaith Chapel", 28.305, 84.062, "Place of worship and reflection for all faiths."))
    manager.add_location(Location("Campus Farm", 28.306, 84.063, "Agricultural research and sustainable farming practices."))
    manager.add_location(Location("Graduate Student Lounge", 28.307, 84.064, "Dedicated space for graduate students to study and relax."))
    manager.add_location(Location("Esports Arena", 28.308, 84.065, "Gaming facility for competitive esports teams and enthusiasts."))
    manager.add_location(Location("Outdoor Amphitheater", 28.309, 84.066, "Venue for outdoor concerts, lectures, and performances."))
    manager.add_location(Location("Student Radio Station", 28.310, 84.067, "Student-run radio broadcasting facility."))
    manager.add_location(Location("Climbing Wall", 28.311, 84.068, "Indoor climbing and bouldering facility."))
    manager.add_location(Location("Campus Wellness Garden", 28.312, 84.069, "Tranquil space for meditation and relaxation."))
    manager.add_location(Location("Robotics Lab", 28.313, 84.070, "Advanced robotics research and development facility."))
    manager.add_location(Location("Journalism Department", 28.314, 84.071, "Classrooms and newsroom for journalism students."))
    manager.add_location(Location("Film and Media Studies Building", 28.315, 84.072, "Facilities for film production and media analysis."))
    manager.add_location(Location("Athletic Field House", 28.316, 84.073, "Indoor practice facilities for various sports."))
    manager.add_location(Location("Campus Recycling Center", 28.317, 84.074, "Central point for campus recycling efforts."))
    manager.add_location(Location("Study Abroad Office", 28.318, 84.075, "Resources and advising for international study programs."))
    manager.add_location(Location("Accessibility Services", 28.319, 84.076, "Comprehensive support for students with disabilities."))
    manager.add_location(Location("Student Legal Services", 28.320, 84.077, "Free legal advice for students."))
    manager.add_location(Location("Campus Data Center", 28.321, 84.078, "Secure facility for university's IT infrastructure."))
    manager.add_location(Location("Outdoor Education Center", 28.322, 84.079, "Programs and facilities for outdoor learning and adventure."))
    manager.add_location(Location("Language Lab", 28.323, 84.080, "Resources for language learning and practice."))
    manager.add_location(Location("Community Engagement Office", 28.324, 84.081, "Connects students with volunteer and service opportunities."))
    manager.add_location(Location("Visual Arts Gallery", 28.325, 84.082, "Exhibition space for student and faculty art."))
    manager.add_location(Location("University Archives", 28.326, 84.083, "Collection of historical university documents and artifacts."))
    manager.add_location(Location("Forensic Science Lab", 28.327, 84.084, "Specialized lab for forensic investigations."))
    manager.add_location(Location("Cybersecurity Center", 28.328, 84.085, "Research and education in cybersecurity."))
    manager.add_location(Location("Biotechnology Research Institute", 28.329, 84.086, "Leading-edge biotechnology research facilities."))
    manager.add_location(Location("Campus Sustainability Office", 28.330, 84.087, "Promotes environmental initiatives and sustainable practices."))
    manager.add_location(Location("Veterans Resource Center", 28.331, 84.088, "Dedicated support services for military veterans."))
    manager.add_location(Location("Applied Sciences Building", 28.332, 84.089, "Houses various applied science programs and labs."))
    manager.add_location(Location("Dance Studio", 28.333, 84.090, "Facilities for dance classes and rehearsals."))
    manager.add_location(Location("Student Innovation Lounge", 28.334, 84.091, "Open space for student projects and collaborative work."))
    manager.add_location(Location("Campus History Museum", 28.335, 84.092, "Chronicles the history of the university and its community."))
    manager.add_location(Location("Speech and Hearing Clinic", 28.336, 84.093, "Provides clinical services and training in communication disorders."))
    manager.add_location(Location("Urban Planning Department", 28.337, 84.094, "Focuses on urban development and city planning studies."))
    manager.add_location(Location("Psychology Research Labs", 28.338, 84.095, "Labs for experimental psychology research."))
    manager.add_location(Location("Sociology Department", 28.339, 84.096, "Studies human society and social behavior."))
    manager.add_location(Location("Political Science Department", 28.340, 84.097, "Focuses on government, public policy, and international relations."))
    manager.add_location(Location("Economics Department", 28.341, 84.098, "Studies the production, distribution, and consumption of goods and services."))
    manager.add_location(Location("Physics Lab Complex", 28.342, 84.099, "Advanced laboratories for physics experiments and research."))
    manager.add_location(Location("Mathematics Department", 28.343, 84.100, "Teaching and research in pure and applied mathematics."))
    manager.add_location(Location("Astronomy Department", 28.344, 84.101, "Dedicated to the study of celestial objects and phenomena."))
    manager.add_location(Location("Geology Department", 28.345, 84.102, "Research and education in earth sciences."))
    manager.add_location(Location("Environmental Science Institute", 28.346, 84.103, "Interdisciplinary research on environmental issues."))
    manager.add_location(Location("Marine Biology Lab", 28.347, 84.104, "Research on marine organisms and ecosystems."))
    manager.add_location(Location("Genetics Research Center", 28.348, 84.105, "Focuses on genetic research and biotechnology applications."))
    manager.add_location(Location("Neuroscience Institute", 28.349, 84.106, "Interdisciplinary study of the nervous system."))
    manager.add_location(Location("Nanotechnology Center", 28.350, 84.107, "State-of-the-art facilities for nanotechnology research."))
    manager.add_location(Location("Materials Science Lab", 28.351, 84.108, "Research on the properties and applications of materials."))
    manager.add_location(Location("Robotics Institute", 28.352, 84.109, "Advanced research and development in robotics."))
    manager.add_location(Location("Artificial Intelligence Center", 28.353, 84.110, "Focuses on AI research and applications."))
    manager.add_location(Location("Data Science Institute", 28.354, 84.111, "Interdisciplinary research and education in data science."))
    manager.add_location(Location("Cybersecurity Lab", 28.355, 84.112, "Hands-on training and research in cybersecurity threats and defenses."))
    manager.add_location(Location("Bioinformatics Center", 28.356, 84.113, "Combines biology, computer science, and statistics."))
    manager.add_location(Location("Quantum Computing Lab", 28.357, 84.114, "Exploration of quantum computing principles and technologies."))
    manager.add_location(Location("Renewable Energy Research Facility", 28.358, 84.115, "Develops and tests sustainable energy solutions."))
    manager.add_location(Location("Climate Change Research Center", 28.359, 84.116, "Investigates the impacts of climate change and mitigation strategies."))
    manager.add_location(Location("Food Science Lab", 28.360, 84.117, "Research and development in food production and safety."))
    manager.add_location(Location("Nutrition Science Department", 28.361, 84.118, "Studies the role of food in health and disease."))
    manager.add_location(Location("Public Health Building", 28.362, 84.119, "Focuses on community health and disease prevention."))
    manager.add_location(Location("Global Studies Institute", 28.363, 84.120, "Interdisciplinary approach to global issues and cultures."))
    manager.add_location(Location("Peace and Conflict Studies Center", 28.364, 84.121, "Promotes research and education in conflict resolution and peacebuilding."))
    manager.add_location(Location("Anthropology Department", 28.365, 84.122, "Studies human societies, cultures, and their development."))
    manager.add_location(Location("Archeology Lab", 28.366, 84.123, "Analysis of archaeological finds and historical research."))
    manager.add_location(Location("Folklore Studies Center", 28.367, 84.124, "Explores traditional beliefs, customs, and stories."))
    manager.add_location(Location("Linguistics Department", 28.368, 84.125, "Scientific study of language and its structure."))
    manager.add_location(Location("Cognitive Science Institute", 28.369, 84.126, "Interdisciplinary study of mind and intelligence."))
    manager.add_location(Location("Philosophy Department", 28.370, 84.127, "Examines fundamental questions about existence, knowledge, values, and reason."))
    manager.add_location(Location("Religious Studies Department", 28.371, 84.128, "Academic study of religious beliefs, behaviors, and institutions."))
    manager.add_location(Location("Theatre Department", 28.372, 84.129, "Training and performance in dramatic arts."))
    manager.add_location(Location("Dance Department", 28.373, 84.130, "Instruction in various dance forms and choreography."))
    manager.add_location(Location("Music Education Building", 28.374, 84.131, "Facilities for music teaching and learning."))
    manager.add_location(Location("Art History Department", 28.375, 84.132, "Studies the history and theory of art."))
    manager.add_location(Location("Creative Writing Program", 28.376, 84.133, "Workshops and courses in fiction, poetry, and non-fiction writing."))
    manager.add_location(Location("Publishing House", 28.377, 84.134, "University-affiliated publishing operations."))
    manager.add_location(Location("Literary Journal Office", 28.378, 84.135, "Manages and produces the university's literary journal."))
    manager.add_location(Location("Center for Digital Humanities", 28.379, 84.136, "Applies computational methods to humanities research."))
    manager.add_location(Location("Archives and Special Collections", 28.380, 84.137, "Preserves rare books, manuscripts, and historical documents."))
    manager.add_location(Location("Oral History Program", 28.381, 84.138, "Collects and preserves spoken testimonies of historical events."))
    manager.add_location(Location("Public Art Initiative Office", 28.382, 84.139, "Manages and promotes public art installations on campus."))
    manager.add_location(Location("Campus Gallery 2", 28.383, 84.140, "Additional exhibition space for contemporary art."))
    manager.add_location(Location("Sculpture Studio", 28.384, 84.141, "Facilities for three-dimensional art creation."))
    manager.add_location(Location("Printmaking Studio", 28.385, 84.142, "Specialized equipment for various printmaking techniques."))
    manager.add_location(Location("Ceramics Studio", 28.386, 84.143, "Equipment for pottery and ceramic art."))
    manager.add_location(Location("Photography Lab", 28.387, 84.144, "Darkroom and digital facilities for photography students."))
    manager.add_location(Location("Fashion Design Studio", 28.388, 84.145, "Workspaces for fashion design and textile arts."))
    manager.add_location(Location("Jewelry and Metalsmithing Studio", 28.389, 84.146, "Facilities for creating jewelry and metal art."))
    manager.add_location(Location("Woodworking Shop", 28.390, 84.147, "Tools and space for woodworking projects."))
    manager.add_location(Location("Glass Blowing Studio", 28.391, 84.148, "Specialized equipment for glass art."))
    manager.add_location(Location("Digital Fabrication Lab", 28.392, 84.149, "Utilizes 3D printers, laser cutters, and CNC machines."))
    manager.add_location(Location("Graphic Design Studio", 28.393, 84.150, "Computer labs and workspaces for graphic design."))
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
    repo.add_building(Building("University Bookstore", 28.245, 84.002, "Textbooks, supplies, and apparel.", "Retail"))
    repo.add_building(Building("Health Center", 28.246, 84.003, "Student medical services.", "Health"))
    repo.add_building(Building("Performing Arts Center", 28.247, 84.004, "Theater and music venues.", "Arts"))
    repo.add_building(Building("Athletic Complex", 28.248, 84.005, "Sports facilities and gym.", "Recreation"))
    repo.add_building(Building("Alumni Center", 28.249, 84.006, "Alumni relations and events.", "Administration"))
    repo.add_building(Building("President's Office", 28.250, 84.007, "University administration headquarters.", "Administration"))
    repo.add_building(Building("Dining Hall East", 28.251, 84.008, "Additional campus dining option.", "Food Service"))
    repo.add_building(Building("Research Lab 1", 28.252, 84.009, "Specialized science research facility.", "Academic"))
    repo.add_building(Building("Career Services", 28.253, 84.010, "Job placement and internship assistance.", "Support"))
    repo.add_building(Building("Technology Center", 28.254, 84.011, "IT support and computer labs.", "Academic"))
    repo.add_building(Building("Student Union Annex", 28.255, 84.012, "Meeting rooms and student organization offices.", "Recreation"))
    repo.add_building(Building("Nursing Building", 28.256, 84.013, "Nursing program classrooms and labs.", "Academic"))
    repo.add_building(Building("Art Studio", 28.257, 84.014, "Visual arts instruction and creation space.", "Arts"))
    repo.add_building(Building("Faculty Club", 28.258, 84.015, "Private club for faculty members.", "Social"))
    repo.add_building(Building("South Residence Hall", 28.259, 84.016, "Another student residence.", "Housing"))
    repo.add_building(Building("North Campus Apartments", 28.260, 84.017, "University-affiliated off-campus housing.", "Housing"))
    repo.add_building(Building("Law School Building", 28.261, 84.018, "Home to the university's law program.", "Academic"))
    repo.add_building(Building("Business School", 28.262, 84.019, "College of Business administration and classrooms.", "Academic"))
    repo.add_building(Building("Education Building", 28.263, 84.020, "College of Education facilities.", "Academic"))
    repo.add_building(Building("Campus Police Station", 28.264, 84.021, "Campus security and emergency services.", "Safety"))
    repo.add_building(Building("Botanical Gardens Office", 28.265, 84.022, "Administration for the campus botanical gardens.", "Administration"))
    repo.add_building(Building("Aquatics Center", 28.266, 84.023, "Indoor and outdoor pools for recreation and sports.", "Recreation"))
    repo.add_building(Building("Child Development Center", 28.267, 84.024, "On-campus childcare and early education.", "Support"))
    repo.add_building(Building("Engineering Research Center", 28.268, 84.025, "Advanced engineering research facilities.", "Academic"))
    repo.add_building(Building("Humanities Building", 28.269, 84.026, "Departments for literature, history, and philosophy.", "Academic"))
    repo.add_building(Building("Music Recital Hall", 28.270, 84.027, "Concert venue for music performances.", "Arts"))
    repo.add_building(Building("Gymnasium Annex", 28.271, 84.028, "Additional courts and fitness areas.", "Recreation"))
    repo.add_building(Building("Financial Aid Office", 28.272, 84.029, "Assistance with student financial planning.", "Support"))
    repo.add_building(Building("Chemistry Lab Building", 28.273, 84.030, "Dedicated chemistry research and teaching labs.", "Academic"))
    repo.add_building(Building("Student Health Annex", 28.274, 84.031, "Expanded health services for students.", "Health"))
    repo.add_building(Building("International Student Office", 28.275, 84.032, "Support for international students.", "Support"))
    repo.add_building(Building("Veterinary Clinic", 28.276, 84.033, "Animal care and veterinary studies.", "Academic"))
    repo.add_building(Building("Campus Ministry Center", 28.277, 84.034, "Additional religious services and student groups.", "Religious"))
    repo.add_building(Building("Public Safety Building", 28.278, 84.035, "Central hub for campus safety operations.", "Safety"))
    repo.add_building(Building("Greenhouse Complex", 28.279, 84.036, "Facilities for plant science research.", "Academic"))
    repo.add_building(Building("Welcome Center", 28.280, 84.037, "First stop for campus visitors and tours.", "Administration"))
    repo.add_building(Building("Food Court North", 28.281, 84.038, "Variety of dining options on north campus.", "Food Service"))
    repo.add_building(Building("Performing Arts Annex", 28.282, 84.039, "Rehearsal spaces and smaller performance rooms.", "Arts"))
    repo.add_building(Building("Athletic Training Facility", 28.283, 84.040, "Sports medicine and rehabilitation services.", "Recreation"))
    repo.add_building(Building("Student Government Office", 28.284, 84.041, "Headquarters for student leadership.", "Support"))
    repo.add_building(Building("Earth Sciences Building", 28.285, 84.042, "Geology and environmental science departments.", "Academic"))
    repo.add_building(Building("Parking Garage A", 28.286, 84.043, "Multi-level parking structure.", "Parking"))
    repo.add_building(Building("Parking Garage B", 28.287, 84.044, "Another multi-level parking structure.", "Parking"))
    repo.add_building(Building("University Press", 28.288, 84.045, "Publishing arm of the university.", "Administration"))
    repo.add_building(Building("Disability Services", 28.289, 84.046, "Support for students with disabilities.", "Support"))
    repo.add_building(Building("IT Services Help Desk", 28.290, 84.047, "Walk-in technical support.", "Support"))
    repo.add_building(Building("Counseling Center", 28.291, 84.048, "Mental health and wellness support.", "Health"))
    repo.add_building(Building("Campus Mailroom", 28.292, 84.049, "Mail and package services for students and staff.", "Service"))
    repo.add_building(Building("Campus Print Shop", 28.293, 84.050, "Printing and design services.", "Service"))
    repo.add_building(Building("Outdoor Adventure Center", 28.294, 84.051, "Equipment rental and trip planning for outdoor activities.", "Recreation"))
    repo.add_building(Building("Student Recreation Fields", 28.295, 84.052, "Outdoor fields for various sports.", "Recreation"))
    repo.add_building(Building("Conference Center", 28.296, 84.053, "Venue for conferences and large events.", "Administration"))
    repo.add_building(Building("Campus Museum", 28.297, 84.054, "Exhibits and collections for education and research.", "Arts"))
    repo.add_building(Building("Observatory", 28.298, 84.055, "Astronomical research and public viewing.", "Academic"))
    repo.add_building(Building("Veterans Affairs Office", 28.299, 84.056, "Support for student veterans.", "Support"))
    repo.add_building(Building("Campus Green", 28.300, 84.057, "Open space for outdoor events and relaxation.", "Recreation"))
    repo.add_building(Building("Research Greenhouse 2", 28.301, 84.058, "Additional greenhouse facilities for advanced research.", "Academic"))
    repo.add_building(Building("Food Truck Zone", 28.302, 84.059, "Designated area for mobile food vendors.", "Food Service"))
    repo.add_building(Building("Innovation Hub", 28.303, 84.060, "Collaborative space for entrepreneurship and innovation.", "Academic"))
    repo.add_building(Building("Digital Arts Studio", 28.304, 84.061, "High-tech lab for digital media and design.", "Arts"))
    repo.add_building(Building("Interfaith Chapel", 28.305, 84.062, "Place of worship and reflection for all faiths.", "Religious"))
    repo.add_building(Building("Campus Farm", 28.306, 84.063, "Agricultural research and sustainable farming practices.", "Academic"))
    repo.add_building(Building("Graduate Student Lounge", 28.307, 84.064, "Dedicated space for graduate students to study and relax.", "Support"))
    repo.add_building(Building("Esports Arena", 28.308, 84.065, "Gaming facility for competitive esports teams and enthusiasts.", "Recreation"))
    repo.add_building(Building("Outdoor Amphitheater", 28.309, 84.066, "Venue for outdoor concerts, lectures, and performances.", "Arts"))
    repo.add_building(Building("Student Radio Station", 28.310, 84.067, "Student-run radio broadcasting facility.", "Student Life"))
    repo.add_building(Building("Climbing Wall", 28.311, 84.068, "Indoor climbing and bouldering facility.", "Recreation"))
    repo.add_building(Building("Campus Wellness Garden", 28.312, 84.069, "Tranquil space for meditation and relaxation.", "Recreation"))
    repo.add_building(Building("Robotics Lab", 28.313, 84.070, "Advanced robotics research and development facility.", "Academic"))
    repo.add_building(Building("Journalism Department", 28.314, 84.071, "Classrooms and newsroom for journalism students.", "Academic"))
    repo.add_building(Building("Film and Media Studies Building", 28.315, 84.072, "Facilities for film production and media analysis.", "Academic"))
    repo.add_building(Building("Athletic Field House", 28.316, 84.073, "Indoor practice facilities for various sports.", "Recreation"))
    repo.add_building(Building("Campus Recycling Center", 28.317, 84.074, "Central point for campus recycling efforts.", "Service"))
    repo.add_building(Building("Study Abroad Office", 28.318, 84.075, "Resources and advising for international study programs.", "Support"))
    repo.add_building(Building("Accessibility Services", 28.319, 84.076, "Comprehensive support for students with disabilities.", "Support"))
    repo.add_building(Building("Student Legal Services", 28.320, 84.077, "Free legal advice for students.", "Support"))
    repo.add_building(Building("Campus Data Center", 28.321, 84.078, "Secure facility for university's IT infrastructure.", "Administration"))
    repo.add_building(Building("Outdoor Education Center", 28.322, 84.079, "Programs and facilities for outdoor learning and adventure.", "Recreation"))
    repo.add_building(Building("Language Lab", 28.323, 84.080, "Resources for language learning and practice.", "Academic"))
    repo.add_building(Building("Community Engagement Office", 28.324, 84.081, "Connects students with volunteer and service opportunities.", "Administration"))
    repo.add_building(Building("Visual Arts Gallery", 28.325, 84.082, "Exhibition space for student and faculty art.", "Arts"))
    repo.add_building(Building("University Archives", 28.326, 84.083, "Collection of historical university documents and artifacts.", "Administration"))
    repo.add_building(Building("Forensic Science Lab", 28.327, 84.084, "Specialized lab for forensic investigations.", "Academic"))
    repo.add_building(Building("Cybersecurity Center", 28.328, 84.085, "Research and education in cybersecurity.", "Academic"))
    repo.add_building(Building("Biotechnology Research Institute", 28.329, 84.086, "Leading-edge biotechnology research facilities.", "Academic"))
    repo.add_building(Building("Campus Sustainability Office", 28.330, 84.087, "Promotes environmental initiatives and sustainable practices.", "Administration"))
    repo.add_building(Building("Veterans Resource Center", 28.331, 84.088, "Dedicated support services for military veterans.", "Support"))
    repo.add_building(Building("Applied Sciences Building", 28.332, 84.089, "Houses various applied science programs and labs.", "Academic"))
    repo.add_building(Building("Dance Studio", 28.333, 84.090, "Facilities for dance classes and rehearsals.", "Arts"))
    repo.add_building(Building("Student Innovation Lounge", 28.334, 84.091, "Open space for student projects and collaborative work.", "Academic"))
    repo.add_building(Building("Campus History Museum", 28.335, 84.092, "Chronicles the history of the university and its community.", "Arts"))
    repo.add_building(Building("Speech and Hearing Clinic", 28.336, 84.093, "Provides clinical services and training in communication disorders.", "Health"))
    repo.add_building(Building("Urban Planning Department", 28.337, 84.094, "Focuses on urban development and city planning studies.", "Academic"))
    repo.add_building(Building("Psychology Research Labs", 28.338, 84.095, "Labs for experimental psychology research.", "Academic"))
    repo.add_building(Building("Sociology Department", 28.339, 84.096, "Studies human society and social behavior.", "Academic"))
    repo.add_building(Building("Political Science Department", 28.340, 84.097, "Focuses on government, public policy, and international relations.", "Academic"))
    repo.add_building(Building("Economics Department", 28.341, 84.098, "Studies the production, distribution, and consumption of goods and services.", "Academic"))
    repo.add_building(Building("Physics Lab Complex", 28.342, 84.099, "Advanced laboratories for physics experiments and research.", "Academic"))
    repo.add_building(Building("Mathematics Department", 28.343, 84.100, "Teaching and research in pure and applied mathematics.", "Academic"))
    repo.add_building(Building("Astronomy Department", 28.344, 84.101, "Dedicated to the study of celestial objects and phenomena.", "Academic"))
    repo.add_building(Building("Geology Department", 28.345, 84.102, "Research and education in earth sciences.", "Academic"))
    repo.add_building(Building("Environmental Science Institute", 28.346, 84.103, "Interdisciplinary research on environmental issues.", "Academic"))
    repo.add_building(Building("Marine Biology Lab", 28.347, 84.104, "Research on marine organisms and ecosystems.", "Academic"))
    repo.add_building(Building("Genetics Research Center", 28.348, 84.105, "Focuses on genetic research and biotechnology applications.", "Academic"))
    repo.add_building(Building("Neuroscience Institute", 28.349, 84.106, "Interdisciplinary study of the nervous system.", "Academic"))
    repo.add_building(Building("Nanotechnology Center", 28.350, 84.107, "State-of-the-art facilities for nanotechnology research.", "Academic"))
    repo.add_building(Building("Materials Science Lab", 28.351, 84.108, "Research on the properties and applications of materials.", "Academic"))
    repo.add_building(Building("Robotics Institute", 28.352, 84.109, "Advanced research and development in robotics.", "Academic"))
    repo.add_building(Building("Artificial Intelligence Center", 28.353, 84.110, "Focuses on AI research and applications.", "Academic"))
    repo.add_building(Building("Data Science Institute", 28.354, 84.111, "Interdisciplinary research and education in data science.", "Academic"))
    repo.add_building(Building("Cybersecurity Lab", 28.355, 84.112, "Hands-on training and research in cybersecurity threats and defenses.", "Academic"))
    repo.add_building(Building("Bioinformatics Center", 28.356, 84.113, "Combines biology, computer science, and statistics.", "Academic"))
    repo.add_building(Building("Quantum Computing Lab", 28.357, 84.114, "Exploration of quantum computing principles and technologies.", "Academic"))
    repo.add_building(Building("Renewable Energy Research Facility", 28.358, 84.115, "Develops and tests sustainable energy solutions.", "Academic"))
    repo.add_building(Building("Climate Change Research Center", 28.359, 84.116, "Investigates the impacts of climate change and mitigation strategies.", "Academic"))
    repo.add_building(Building("Food Science Lab", 28.360, 84.117, "Research and development in food production and safety.", "Academic"))
    repo.add_building(Building("Nutrition Science Department", 28.361, 84.118, "Studies the role of food in health and disease.", "Academic"))
    repo.add_building(Building("Public Health Building", 28.362, 84.119, "Focuses on community health and disease prevention.", "Academic"))
    repo.add_building(Building("Global Studies Institute", 28.363, 84.120, "Interdisciplinary approach to global issues and cultures.", "Academic"))
    repo.add_building(Building("Peace and Conflict Studies Center", 28.364, 84.121, "Promotes research and education in conflict resolution and peacebuilding.", "Academic"))
    repo.add_building(Building("Anthropology Department", 28.365, 84.122, "Studies human societies, cultures, and their development.", "Academic"))
    repo.add_building(Building("Archeology Lab", 28.366, 84.123, "Analysis of archaeological finds and historical research.", "Academic"))
    repo.add_building(Building("Folklore Studies Center", 28.367, 84.124, "Explores traditional beliefs, customs, and stories.", "Academic"))
    repo.add_building(Building("Linguistics Department", 28.368, 84.125, "Scientific study of language and its structure.", "Academic"))
    repo.add_building(Building("Cognitive Science Institute", 28.369, 84.126, "Interdisciplinary study of mind and intelligence.", "Academic"))
    repo.add_building(Building("Philosophy Department", 28.370, 84.127, "Examines fundamental questions about existence, knowledge, values, and reason.", "Academic"))
    repo.add_building(Building("Religious Studies Department", 28.371, 84.128, "Academic study of religious beliefs, behaviors, and institutions.", "Academic"))
    repo.add_building(Building("Theatre Department", 28.372, 84.129, "Training and performance in dramatic arts.", "Arts"))
    repo.add_building(Building("Dance Department", 28.373, 84.130, "Instruction in various dance forms and choreography.", "Arts"))
    repo.add_building(Building("Music Education Building", 28.374, 84.131, "Facilities for music teaching and learning.", "Academic"))
    repo.add_building(Building("Art History Department", 28.375, 84.132, "Studies the history and theory of art.", "Academic"))
    repo.add_building(Building("Creative Writing Program", 28.376, 84.133, "Workshops and courses in fiction, poetry, and non-fiction writing.", "Academic"))
    repo.add_building(Building("Publishing House", 28.377, 84.134, "University-affiliated publishing operations.", "Administration"))
    repo.add_building(Building("Literary Journal Office", 28.378, 84.135, "Manages and produces the university's literary journal.", "Academic"))
    repo.add_building(Building("Center for Digital Humanities", 28.379, 84.136, "Applies computational methods to humanities research.", "Academic"))
    repo.add_building(Building("Archives and Special Collections", 28.380, 84.137, "Preserves rare books, manuscripts, and historical documents.", "Academic"))
    repo.add_building(Building("Oral History Program", 28.381, 84.138, "Collects and preserves spoken testimonies of historical events.", "Academic"))
    repo.add_building(Building("Public Art Initiative Office", 28.382, 84.139, "Manages and promotes public art installations on campus.", "Arts"))
    repo.add_building(Building("Campus Gallery 2", 28.383, 84.140, "Additional exhibition space for contemporary art.", "Arts"))
    repo.add_building(Building("Sculpture Studio", 28.384, 84.141, "Facilities for three-dimensional art creation.", "Arts"))
    repo.add_building(Building("Printmaking Studio", 28.385, 84.142, "Specialized equipment for various printmaking techniques.", "Arts"))
    repo.add_building(Building("Ceramics Studio", 28.386, 84.143, "Equipment for pottery and ceramic art.", "Arts"))
    repo.add_building(Building("Photography Lab", 28.387, 84.144, "Darkroom and digital facilities for photography students.", "Arts"))
    repo.add_building(Building("Fashion Design Studio", 28.388, 84.145, "Workspaces for fashion design and textile arts.", "Arts"))
    repo.add_building(Building("Jewelry and Metalsmithing Studio", 28.389, 84.146, "Facilities for creating jewelry and metal art.", "Arts"))
    repo.add_building(Building("Woodworking Shop", 28.390, 84.147, "Tools and space for woodworking projects.", "Arts"))
    repo.add_building(Building("Glass Blowing Studio", 28.391, 84.148, "Specialized equipment for glass art.", "Arts"))
    repo.add_building(Building("Digital Fabrication Lab", 28.392, 84.149, "Utilizes 3D printers, laser cutters, and CNC machines.", "Academic"))
    repo.add_building(Building("Graphic Design Studio", 28.393, 84.150, "Computer labs and workspaces for graphic design.", "Arts"))
    return repo


def generate_report(buildings):
    lines = []
    for b in buildings:
        lines.append(b.format_info())
    return "\n".join(lines)


def export_to_json(buildings):
    data = [b.to_dict() for b in buildings]
    return json.dumps(data, indent=2)


def search_and_report(repo, search_term):
    results = repo.find_by_name(search_term)
    if not results:
        return f"No buildings found matching '{search_term}'."
    return generate_report(results)


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


def main():
    repo = create_sample_repository()

    print("---")
    print("All Buildings:\n")
    print(generate_report(repo.get_all()))

    print("\n---")
    print("Filtered by category 'Academic':\n")
    academic = repo.find_by_category("Academic")
    print(generate_report(academic))

    print("\n---")
    print("Exporting JSON:\n")
    print(export_to_json(repo.get_all()))

    print("\n---")
    print("Searching for 'Library':\n")
    print(search_and_report(repo, "Library"))

    print("\n---")
    print("Searching for 'Gym':\n")
    print(search_and_report(repo, "Gym"))

    print("\n---")
    print_statistics(repo)

    print("\n---")
    find_and_display(repo, "Housing")
    find_and_display(repo, "Religious")
    find_and_display(repo, "Recreation")
    find_and_display(repo, "Arts")
    find_and_display(repo, "Support")
    find_and_display(repo, "Administration")
    find_and_display(repo, "Health")
    find_and_display(repo, "Safety")
    find_and_display(repo, "Food Service")
    find_and_display(repo, "Retail")
    find_and_display(repo, "Social")
    find_and_display(repo, "Parking")
    find_and_display(repo, "Service")
    find_and_display(repo, "Student Life") # New category

if __name__ == "__main__":
    main()
