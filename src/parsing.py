class Contributor:
    def __init__(self, name, skills) -> None:
        self.name = name
        self.skills = skills
    
    def __str__(self) -> str:
        return f"name: {self.name}, skills {self.skills}"

class Project:
    def __init__(self, name, days, score, bestBefore, nbRoles, skills) -> None:
        self.name = name
        self.days = days
        self.score = score
        self.bestBefore = bestBefore
        self.nbRoles = nbRoles
        self.skills = skills
        self.projects = []
        self.contributors = []
    
    def __str__(self) -> str:
        return f'name : {self.name}, days : {self.days}, score : {self.score}, best before : {self.nbRoles}, nbRoles : {self.nbRoles}, skills : {self.skills}'

class Parsing:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.result = []

    def parse(self) -> list:
        f = open(self.filepath)
        rawValue = f.read().split('\n')
        skills = []
        contributors = []
        projects = []

        nbContributor = int(rawValue[0].split(' ')[0])
        nbProj = int(rawValue[0].split(' ')[1])

        tmp = 1

        for _ in range(nbContributor):
            skills = []
            name = rawValue[tmp].split(' ')[0]
            nbSkills = int(rawValue[tmp].split(' ')[1])
            tmp += 1

            for _ in range(nbSkills):
                skillName = rawValue[tmp].split(' ')[0]
                lvl = rawValue[tmp].split(' ')[1]
                skills.append((skillName, lvl))
                tmp += 1

            c = Contributor(name, skills)
            contributors.append(c)
            skills = []

        for _ in range(nbProj):
            skills = []
            list = rawValue[tmp].split(' ')
            nbSkills = int(list[4])
            tmp += 1

            for _ in range(nbSkills):
                skillName = rawValue[tmp].split(' ')[0]
                lvl = rawValue[tmp].split(' ')[1]
                skills.append((skillName, lvl))
                tmp += 1

            p = Project(list[0], list[1], list[2], list[3], list[4], skills)
            projects.append(p)
            skills = []
        
        self.projects = projects
        self.contributors = contributors








