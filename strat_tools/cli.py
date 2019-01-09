import click
from click import secho
from PyPDF2 import PdfFileReader, PdfFileWriter
from io import BytesIO
from PIL import Image
# Wand is an `imagemagick` binding, so ImageMagick needs to be installed
from wand.image import Image as WandImage

@click.command(name='stack-section')
@click.argument('infile', type=click.Path(exists=True))
@click.argument('outfile', type=click.Path())
@click.option('--dpi', type=int, default=300)
def cli(infile, outfile, dpi=300):

    secho(infile, fg='green')

    # GoodNotes PDF template is a 5.82x7.42in document
    # Grid in the graph paper is 1cm large boxes

    with WandImage(filename=infile, resolution=dpi) as img:
        n = len(img.sequence)
        secho('pages = '+str(n))

        height = img.height
        width = img.width

        height_inches = height/dpi

        pixels_per_box = dpi/2.54

        # The working area (with grid) is 17 boxes tall by 13 boxes wide
        n_boxes = (13,17)
        # section is 15 boxes high in the center of the image in our current
        # template
        working_height = (n_boxes[1]-2)*pixels_per_box
        margin = (height-working_height)/2
        total_height = round(working_height*n+2*margin)

        surface = Image.new('RGBA', (img.width, total_height))

        for i, page in enumerate(img.sequence):
            bytes = BytesIO()
            p = page.clone()
            with p.convert('png') as converted:
                converted.save(bytes)
            img = Image.open(bytes)
            cropped = img.crop((0, round(margin), width, round(margin+working_height)))
            # The most this will ever be off from desired height
            # is half a pixel.
            insert_height = round(working_height*(n-1-i)+margin)
            ul = (0,insert_height)

            surface.paste(cropped, ul)

    surface.save(outfile)
