import click
import db
#import install

@click.command()
@click.argument('command')
@click.argument('option')
def install(command, option):
    if command  == "install":
        package = db.install(option)
        click.echo("--------- Installing " + option + " ---------")
    if command == "db":
        if option == "init":
            db.init()
        if option == "new":
            name = click.prompt("Name: ")
            desc = click.prompt("desc: ")
            print(name,desc)
if __name__ == "__main__":
    install()
