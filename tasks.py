from invoke import task


@task
def vai(c):
    c.run("python3 manage.py runserver")
