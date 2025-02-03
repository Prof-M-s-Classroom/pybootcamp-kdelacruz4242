class CrewMember:
    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience  # Years of experience

    def __str__(self):
        return f"{self.name} - {self.role} ({self.experience} yrs exp)"

class CrewRoster:

    def __init__(self):
        self.crew = []  # List of CrewMember objects

    def add_member(self, name, role, experience):
        self.crew.append(CrewMember(name, role, experience))


    def remove_member(self, name):
        for member in self.crew:
           if member.name == name:
               self.crew.remove(member)


    def list_crew(self):
        for member in self.crew:
            print(member)


# === TEST CODE ===

roster = CrewRoster() #Empty Crew roster created

# TODO: Uncomment and implement methods
roster.add_member("Alice", "Engineer", 5)
roster.add_member("Bob", "Pilot", 10)
roster.list_crew()

roster.remove_member("Alice")
roster.list_crew()

"""
#git add .
#git commit -m "Completed homework assignment"
#git push
"""""