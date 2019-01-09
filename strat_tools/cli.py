import click

@click.command(name='stack-section')
@click.option(infile, type=click.Path(exists=True))
@click.option(outfile type=click.Path())
def cli(infile, outfile):
    pass
