import typer # type: ignore 

# run python typertut --help
# you get help for free

# using a type anotation and a default value.
# remove the default value to see how the help message changes.
def main(name: str = "Please enter a name."): 
    print(f"Hello, {name}")

if __name__ == "__main__":
    typer.run(main)