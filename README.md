# Diagram Parsing Project

This project provides code and file examples for working with Microsoft Visio (.vsdx) files, including modification capabilities and SVG conversion.

## Project Structure

```
README.md
vsdx/
├── modify_vsdx.py              # Script to modify VSDX files
├── vsdx_to_svg.py             # Script to convert VSDX to SVG
├── my_diagram_modified.vsdx    # Modified diagram file
├── my_diagram_modified.zip     # Backup/alternative format
├── output.svg                  # Generated SVG output
├── Sample/
│   └── Drawing 1.vsdx         # Sample Visio diagram
├── before_modify/             # Original diagram structure
│   ├── [Content_Types].xml
│   ├── _rels/
│   ├── docProps/
│   └── visio/
└── after_modify/              # Modified diagram structure
    ├── [Content_Types].xml
    ├── _rels/
    ├── docProps/
    └── visio/
```

## Scripts

### modify_vsdx.py
Modifies VSDX files programmatically. This script can be used to:
- Update diagram content
- Modify shapes and their properties
- Change text elements
- Alter diagram structure

### vsdx_to_svg.py
Converts VSDX files to SVG format for web-compatible display and sharing.

## File Formats

### VSDX Files
VSDX files are essentially ZIP archives containing XML files that define the diagram structure:
- `[Content_Types].xml` - Defines content types
- `_rels/` - Relationship definitions
- `docProps/` - Document properties
- `visio/` - Core diagram data including pages, masters, and themes

### Generated Files
- `my_diagram_modified.vsdx` - The modified version of the original diagram
- `output.svg` - SVG representation of the diagram
- `my_diagram_modified.zip` - ZIP format of the modified diagram

## Usage

### Modifying a VSDX File
```bash
python vsdx/modify_vsdx.py
```

### Converting to SVG
```bash
python vsdx/vsdx_to_svg.py
```

## Sample Data

The [`Sample/Drawing 1.vsdx`](vsdx/Sample/Drawing%201.vsdx) file provides a test diagram for experimenting with the modification and conversion tools.

## Dependencies

This project likely requires:
- Python 3.x
- XML parsing libraries
- ZIP file handling capabilities
- SVG generation libraries

## Notes

This project consists only of example code. For web viewing, it is recommended to modify the SVG rather than the VSDX, due to the lack of open-source libraries for converting VSDX to SVG. This process can be performed on SVG using similar logic.
