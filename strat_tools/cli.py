from __future__ import division
import click
from click import secho, echo, style
from io import BytesIO
from PIL import Image
from os import path
from math import ceil
from textwrap import dedent
# Wand is an `imagemagick` binding, so ImageMagick needs to be installed
from wand.image import Image as WandImage

def save_image(image, outfile):
    echo(style(outfile, fg="green")
        +" [{}x{}]".format(image.width, image.height))
    image.save(outfile)


help = {
    'clip-left': "Left crop (default: 0)",
    'clip-right': "Right crop (default: 0)",
    'height-per-page': "Height of section on single page (default: 15). Assumes that the "
        "section is centered on the vertical axis of the page.",
    'max-height': "Threshold to split output image if too tall (no default). If not specified, "
        "doesn't split the image at all. A value of <=16384 px allows the "
        "image to be imported without scaling into Procreate",
    'dpi': "Resolution of output (default: 300)."
}

def option(*args, **kwargs):
    key = args[0].replace("--","")
    unit = kwargs.pop('unit')
    text = help[key]
    kwargs['help'] = style("["+unit+"] ", bold=True, fg='green')+text
    return click.option(*args, **kwargs)

@click.command(name='stack-section')
@click.argument('infile', type=click.Path(exists=True), metavar='<pdf-input>')
@click.argument('outfile', type=click.Path(), metavar='<png-output>')
@option('--clip-left', type=float, default=0, unit="cm")
@option('--clip-right', type=float, default=0, unit="cm")
@option('--height-per-page', type=float, default=15, unit="cm")
@option('--dpi', type=int, default=300, unit="px/inch")
@option('--max-height', type=int, unit='px')
def cli(infile, outfile, dpi=300, clip_left=0, clip_right=0,
        height_per_page=15, max_height=None):
    """
    Stack a stratigraphic column drawn on multiple pages using
    a cm-gridded GoodNotes template to composite png image(s) of the entire
    section.

    \b
    <pdf-input> is a multipage PDF file
        (presumably exported from GoodNotes).
    <png-output> is a filename for the output PNG
        (it will be suffixed with _1,_2, etc.
        if output is split by --max-height).
    """

    secho(infile, fg='green')

    # GoodNotes PDF template is a 5.82x7.42in document
    # Grid in the graph paper is 1cm large boxes

    with WandImage(filename=infile, resolution=dpi) as img:
        n = len(img.sequence)
        secho('pages = '+str(n))

        pixels_per_box = dpi/2.54

        # The working area (with grid) is 17 boxes tall by 13 boxes wide
        n_boxes = (13,17)

        # section is 15 boxes high in the center of the image in our current
        # template
        working_height = height_per_page*pixels_per_box

        margin = (img.height-working_height)/2
        total_height = int(round(working_height*n+2*margin))

        # Set right and left crop
        left = round(clip_left*dpi)
        right = round(clip_right*dpi)

        width = int(img.width-left-right)

        surface = Image.new('RGBA', (width, total_height))

        for i, page in enumerate(img.sequence):
            bytes = BytesIO()
            p = page.clone()
            with p.convert('png') as converted:
                converted.save(bytes)
            img = Image.open(bytes)

            # Set top
            top = round(margin)
            if i == n-1: top = 0

            # bottom
            bottom = round(margin+working_height)
            if i == 0: bottom = img.height

            cropped = img.crop((left, top, img.width-right, bottom))
            # The most this will ever be off from desired height
            # is half a pixel.
            insert_height = int(round(working_height*(n-1-i)+top))
            ul = (0,insert_height)

            surface.paste(cropped, ul)

    # Split image if too tall
    if not max_height or max_height > surface.height:
        save_image(surface, outfile)
        return

    nsplits = ceil(surface.height/max_height)

    echo("Splitting into {} parts".format(nsplits))

    stem, ext = path.splitext(outfile)

    split_size = ceil(surface.height/nsplits)

    # iterate through splits from bottom to top
    bottom = surface.height
    top = bottom-split_size
    i = 1
    while bottom > 0:
        # Fix last division if need be
        if top < 0: top = 0

        filename = stem + "_" + str(i) + ext
        cropped = surface.crop((0,top,surface.width,bottom))

        echo("Creating image {} of {}".format(i,nsplits))
        save_image(cropped, filename)

        bottom = top
        top -= split_size
        i+= 1

    # Here we split into chunks less than the split threshold
