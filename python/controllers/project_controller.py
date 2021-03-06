# -*- coding: utf-8 -*-

from python.models.project import Project


class ProjectController:
    def __init__(self):
        self.projects = dict()
        self.current_id = 0

    def add_project(self, name: str, description: str, base_text: str, mentor: object, mentor_aux: object, areas: list) -> int:
        project_id = len(self.projects) + 1
        self.current_id = project_id

        project = Project(name, description, base_text,
                          mentor, mentor_aux, areas)
        self.projects[project_id] = project

        return project_id

    def list_projects(self) -> list:
        return list(self.projects.values())

    def find_projects_by_state(self, state: str) -> dict:
        found_projects = {}

        for key, val in self.projects.items():
            if val.state == state:
                found_projects.update({key: val})
        if not found_projects:
            raise Exception('Projects not found!')

        return found_projects

    def find_projects_by_area(self, area: list) -> dict:
        found_projects = {}

        for key, val in self.projects.items():
            if area in val.areas:
                found_projects.update({key: val})
        if not found_projects:
            raise Exception('Projects not found!')

        return found_projects

    def update_project_value(self, current_id: int, key: str, new_value: str) -> object:
        if current_id in self.projects:
            project = self.projects[current_id]
            setattr(project, key, new_value)
            return project
        else:
            raise Exception('Index Error')

    def add_project_area(self, current_id: int, new_area: str) -> object:
        if current_id in self.projects:
            project = self.projects[current_id]
            project.areas.append(new_area)
            return project
        else:
            raise Exception('Index Error')

    def remove_project_area(self, current_id: int, area: str) -> str:
        if current_id in self.projects:
            project = self.projects[current_id]
            try:
                project.areas.remove(area)
                return area
            except ValueError as e:
                return e
        else:
            raise Exception('Index Error')

    def remove_project(self, current_id: int):
        if current_id in self.projects:
            project = self.projects[current_id]
            del self.projects[current_id]
            return project
        else:
            raise Exception('Index Error')

    def find_project_by_mentor(self, email_mentor: str) -> dict:
        found_projects = {}
        for key, project in self.projects.items():
            if project.check_mentor_by_email(email_mentor):
                found_projects.update({key: project})
        if not found_projects:
            raise Exception('Mentor not found!')

        return found_projects
