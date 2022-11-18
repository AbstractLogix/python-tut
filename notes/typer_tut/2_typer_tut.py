# MAIN FILE IN TUT FOR YOUTUBE FOR SIMPLICITY
# This is an upgrade to the previous simple 
# example to add some complexity

import typer

# Creates a typer.Typer() app, and create two subcommands with their parameters
# run python --help
# run python 2_typer_tut hello oscar
# run python 2_typer_tut goodbye oscar
# run python hello --help
# run python goodbye --help
app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello, {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye, {name}. Have a good day.")
    else:
        print(f"Bye {name}.")


if __name__ == "__main__":
    app()

# Explicitly create a typer.Typer app.
# The previous typer.run actually creates one implicitly for you.
# Add two subcommands with @app.command().
# Execute the app() itself, as if it was a function (instead of typer.run).