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

After returning from the field, you'll want to standardize all of your sections,
remove extraneous annotation, and make them conform to a consistent graphical
style. This could mean artistic rendition and/or painting in patterns such as the
[USGS FGDC Geologic Patterns](https://davenquinn.com/projects/geologic-patterns).

For reference, the maximum allowed single dimension for an image imported into
Procreate is 16384 pixels; if an image exceeds this size, it will be
scaled to fit. This is annoying, especially given that it is important
to keep section images at the same scale for later use.



## Command-line usage

```
> stack-section <infile> <outfile>
```
