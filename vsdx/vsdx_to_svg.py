import os
# Set environment variable before any aspose imports to fix ICU issue
os.environ['DOTNET_SYSTEM_GLOBALIZATION_INVARIANT'] = '1'

import aspose.diagram as diagram

# Load the VSDX file
dia = diagram.Diagram("./my_diagram_modified.vsdx")

# Save as SVG
dia.save("output.svg", diagram.SaveFileFormat.SVG)