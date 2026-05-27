from repro.models import Project


def get_project_count_ok():
    return Project.objects.all().count()

def get_project_count_lint_error():
    queryset = Project.objects.all()
    return queryset.count()
