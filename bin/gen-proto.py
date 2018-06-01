#!/usr/bin/env python3

import click

from metamodel.utils.schemaloader import load_schema
from metamodel.generators.protogen import ProtoGenerator

@click.command()
@click.argument("file", type=click.File('r'))
def cli(file):
    schema = load_schema(file)
    g = ProtoGenerator(schema=schema)
    print(g.serialize())



if __name__ == "__main__":
    cli()
    
