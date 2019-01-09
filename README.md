# iPad-strat-tools

This is a basic toolset for collecting stratigraphic data in the field
on an iPad, and rendering a seamless high-resolution stratigraphic column
that can be exported for publication or handed off to other software
such as Illustrator or Procreate for completion.

It includes a description of an iPad workflow for section-measuring,
a set of PDF section axes to use as a GoodNotes template, and a command-line
tool, `stack-section`, that stacks rendered section pages into a complete section. 

# The workflow: stratigraphic measurement in GoodNotes

The iPad Pro, with its Apple Pencil, has the potential to completely change
how we do field geology. One of the easiest ways to see its potential is to
use it to measure a section in the field – gone are the days of tediously
scanning your field notebook, massive layouts in Photoshop, and finicky graphics
tablets. Or giant sheets of vellum.

Stylus-enabled note-taking apps allow drawing like paper on a consistent set
of axes, in an intuitive and robust way. They also support progressive enhancement
in a way their Rite-in-the-Rain cousins cannot — by the time you're out of the
field, you're much of the way to your publication-quality sections!

[GoodNotes](https://www.goodnotes.com/) is one of the best note-taking apps
we have encountered for the iPad, and the workflow described here is tailored to
its use. Other note-taking apps like [Paper](https://paper.bywetransfer.com/)
might also be useful, in which case the procedures and scripts

## A standardized template

Not having to re-label your axes every ~10-20 meters of stratigraphy is
a huge time-saver in the field

A basic PDF template for a stratigraphic column is included in this

A new template optimized for your desired set of section axes can be made using the
graph-paper preset in GoodNotes. Be sure to leave a one-large-box margin at the
top and bottom of the section drawing area. If you want to change this margin,
adjusting the script will be required. Export your new PDF from GoodNotes and
re-import it as a *Template* to use it as the basis for a notebook.

# Tool for stitching together a production section

After returning from the field, you'll want to standardize your sections,
remove extraneous annotation, and make them conform to a consistent graphical
style. This could mean artistic rendition and/or painting in patterns such as the
[USGS FGDC Geologic Patterns](https://davenquinn.com/projects/geologic-patterns).

At its core, this command-line tool stitches together sections that were created
using the template

Parts of the Python code are an adaptation of earlier code that I wrote for assembling
field sections of the Naukluft plateau from scanned images of field notebook pages.
However, the standard size and orientation of a digital notebook page makes extraction
of images from GoodNotes far easier.

For reference, the maximum allowed single dimension for an image imported into
Procreate is 16384 pixels; if an image exceeds this size, it will be
scaled to fit. This is annoying, especially given that it is important
to keep section images at the same scale for later use.



## Command-line usage

After installation, the command-line tool should be usable at te

```
Usage: stack-section [OPTIONS] <pdf-input> <png-output>

  Stack a stratigraphic column drawn on multiple pages using a cm-gridded
  GoodNotes template to composite png image(s) of the entire section.

  <pdf-input> is a multipage PDF file
      (presumably exported from GoodNotes).
  <png-output> is a filename for the output PNG
      (it will be suffixed with _1,_2, etc.
      if output is split by --max-height).

Options:
  --clip-left FLOAT        [cm] Left crop (default: 0)
  --clip-right FLOAT       [cm] Right crop (default: 0)
  --height-per-page FLOAT  [cm] Height of section on single page
                           (default: 15). Assumes that the section is centered
                           on the vertical axis of the page.
  --dpi INTEGER            [px/inch] Resolution of output
                           (default: 300).
  --max-height INTEGER     [px] Threshold to split output image
                           if too tall (no default). If not specified, doesn't
                           split the image at all. A value of <=16384 px
                           allows the image to be imported without scaling
                           into Procreate
  --help                   Show this message and exit.
```
