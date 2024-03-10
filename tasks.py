from invoke import task


@task
def lint(ctx):
    """Run flake8 linter"""
    ctx.run("flake8 .")


@task
def test(ctx):
    """Run pytest"""
    ctx.run("pytest")


@task
def act_push(ctx):
    """Run Github push actions locally."""
    ctx.run("clear && ./bin/act push")


@task
def act_install(ctx):
    """
    Install local runner for Github actions.

    See: https://github.com/nektos/act?tab=readme-ov-file
    """

    fn = "act-install.sh"
    # ctx.run(
    #     "curl --proto '=https' --tlsv1.2 -sSf \
    #     https://raw.githubusercontent.com/nektos/act/master/install.sh"
    # )
    ctx.run(
        f"curl \
        https://raw.githubusercontent.com/nektos/act/master/install.sh \
        > {fn}"
    )
    ctx.run(f"chmod +x {fn}")
    ctx.run(f"./{fn}")
    ctx.run(f"rm {fn}")
