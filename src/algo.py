def sort(projects) -> list:
    projects.sort(key=lambda x: x.getBestBefore())
    
    return projects

contributorsUsed = []

def contributorIsAvailable(contributors, skill):
    for contributor in contributors:
        if (contributor.hasTheSkill(skill)):
            contributorsUsed.append(contributor)
            return True
    return False

def projectFilledWithContributors(project, contributors):
    for skill in project.skills:
        if(not contributorIsAvailable(contributors, skill)):
            return False
    return True

def displayProject(project):
    print(f"{project.name}")
    for contributorUsed in contributorsUsed:
        print(contributorUsed.name, end='')
        if (contributorUsed != contributorsUsed[-1]):
            print(' ', end='')
    print()

def updateSkillsContributors(contributors):
    for contributor in contributors:
        if contributor.free:
            continue
        contributor.addSkill()

def algo(projects, contributors):
    projects = sort(projects)

    print(len(projects))
    for _ in range(len(projects)):
        update = False
        for project in projects:
            if (project.done):
                continue
            if (not projectFilledWithContributors(project, contributors)):
                contributorsUsed.clear()
                continue

            displayProject(project)
            updateSkillsContributors(contributors)
            for contributor in contributors:
                contributor.free = True
            contributorsUsed.clear()
            project.done = True
            update = True
        if not update:
            break
