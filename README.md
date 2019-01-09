# iPad-strat-tools

This is a basic toolset for collecting stratigraphic data in the field
on an iPad, and rendering a seamless high-resolution section that can
be exported to other software such as Illustrator or Procreate more
suited to precision drawing and preparation of publication-ready sections.

# Stratigraphic measurement in GoodNotes

A new template optimized for your measurement parameters can be made using the
graph-paper preset in GoodNotes. Be sure to leave a one-large-box margin at the
top and bottom of the section drawing area. If you want to change this margin,
adjusting the script will be required.

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

```
Usage: stack-section [OPTIONS] INFILE OUTFILE

  Stack a section drawn on a cm-gridded GoodNotes template to a PNG image of
  the whole section

Options:
  --clip-left FLOAT        [cm] Left crop (default: 0)
  --clip-right FLOAT       [cm] Right crop (default: 0)
  --height-per-page FLOAT  [cm] Height of section on single page
                           (default: 15). Assumes that the section is centered
                           relative to the drawing area on the page.
  --dpi INTEGER            [px/inch] Resolution of output
                           (default: 300).
  --max-height INTEGER     [px] Threshold to split output image
                           if too tall (no default). If not specified, doesn't
                           split the image at all. A value of <=16384 px
                           allows the image to be imported without scaling
                           into Procreate
  --help                   Show this message and exit.
```
