import click
from done.services import analytictools
from done.services import habits


@click.group()
def cli():
    # welcomes you to the app
    """Welcome to DONE your Habit Tracker"""
    pass


@cli.command()
def returnHabits():
    """returns all habits and all information"""
    analytictools.returnAllHabits()


@cli.command()
@click.argument("name")
def longeststreak(name: str):
    """
    returns longest streak of a specific habit that you name

    use as: done longeststreak <name>
    """
    analytictools.returnLongestStreak(name)


@cli.command()
@click.argument("name")
def returnstreak(name: str):
    """
    returns current streak of a specific habit that you name

    use as: done returnstreak <name>
    """
    analytictools.returnGivenStreak(name)


@cli.command()
@click.argument("periodicity")
def sameperiodicity(periodicity: int):
    """
    returns all habits with the same periodicity

    use as: done returnstreak <periodicity>
    """
    analytictools.returnHabitSamePeridocity(periodicity)


@cli.command()
@click.argument("name")
def delete(name: str):
    """
    delets a specific habit that you name

    use as: done delete <name>
    """
    habits.delete_habit(name)


@cli.command()
@click.argument("name")
def check(name: str):
    """
    check a specific habit that you name

    use as: done check <name>
    """
    habits.check_habit(name)


@cli.command()
@click.argument("name")
@click.argument("periodicity")
def newhabit(name: str, periodicity: int):
    """
    creates a new habit with a name and periodicity

    use as: done newhabit <name> <periodicity>
    """
    habits.Habit(name, periodicity)
