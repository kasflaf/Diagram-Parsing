# Advanced VSDX modification using python-vsdx library

import xml.etree.ElementTree as ET
from datetime import datetime
try:
    from vsdx import VisioFile
    from vsdx import namespace
except ImportError:
    print("Error: python-vsdx library not found. Install it with: pip install python-vsdx")
    exit(1)

# --- CONFIGURATION ---
INPUT_FILE = 'Sample/Drawing 1.vsdx'
OUTPUT_FILE = 'my_diagram_modified.vsdx'
TARGET_SHAPE_TEXT = 'hancurkancandi()'
NEW_TEXT_FOR_SHAPE = 'hancurkancandi() modified'
NEW_PROPERTY_1_NAME = 'tesdata1'
NEW_PROPERTY_1_VALUE = datetime.now().strftime('%Y-%m-%d')
NEW_PROPERTY_2_NAME = 'tesdata2'
NEW_PROPERTY_2_VALUE = 'Budi'

def add_xml_property(shape, prop_name, prop_value, prop_label):
    """Add property by creating proper XML structure"""
    # Find or create Property section
    property_section = shape.xml.find(f'{namespace}Section[@N="Property"]')
    if property_section is None:
        property_section = ET.SubElement(shape.xml, f'{namespace}Section')
        property_section.set('N', 'Property')
    
    # Create Row for the property
    row = ET.SubElement(property_section, f'{namespace}Row')
    row.set('N', prop_name)
    
    # Add cells
    label_cell = ET.SubElement(row, f'{namespace}Cell')
    label_cell.set('N', 'Label')
    label_cell.set('V', prop_label)
    
    value_cell = ET.SubElement(row, f'{namespace}Cell')
    value_cell.set('N', 'Value')
    value_cell.set('V', f'{prop_value}')
    
    type_cell = ET.SubElement(row, f'{namespace}Cell')
    type_cell.set('N', 'Type')
    type_cell.set('V', '0')

def modify_vsdx():
    """
    VSDX modification using correct python-vsdx API based on documentation
    """
    try:
        with VisioFile(INPUT_FILE) as vis:
            print(f"File has {len(vis.pages)} page(s)")
            
            for page_num, page in enumerate(vis.pages, 1):
                child_shapes = page.child_shapes
                print(f"\nPage {page_num}: {len(child_shapes)} shapes")
                
                for shape_num, shape in enumerate(child_shapes, 1):
                    shape_text = getattr(shape, 'text', '') or ''
                    shape_id = getattr(shape, 'ID', 'Unknown')
                    
                    print(f"  Shape {shape_num}: '{shape_text}' (ID: {shape_id})")
                    
                    # Check if this is our target shape
                    if shape_text and TARGET_SHAPE_TEXT in shape_text:
                        print(f"    -> MODIFYING THIS SHAPE")
                        
                        # Text modification
                        shape.text = NEW_TEXT_FOR_SHAPE
                        print(f"    -> Text changed to: '{shape.text}'")
                        
                        # Color modification
                        shape.fill_color = 'red'
                        print(f"    -> Fill color set to red")
                        
                        # REPLACE THE OLD PROPERTY METHOD WITH XML METHOD
                        try:
                            # Instead of: shape.data_properties[NEW_PROPERTY_1_NAME] = NEW_PROPERTY_1_VALUE
                            # Do this:
                            add_xml_property(shape, NEW_PROPERTY_1_NAME, NEW_PROPERTY_1_VALUE, 'tesdata1')
                            add_xml_property(shape, NEW_PROPERTY_2_NAME, NEW_PROPERTY_2_VALUE, 'tesdata2')
                            print(f"    -> Data properties added via XML")
                            
                            # Clear cache and check
                            shape._data_properties = None
                            updated_props = shape.data_properties
                            print(f"    -> Updated properties: {list(updated_props.keys())}")
                            
                        except Exception as prop_error:
                            print(f"    -> Data properties failed: {prop_error}")
                        
                        # Print final shape info
                        print(f"    -> Final text: '{shape.text}'")
                        print(f"    -> Position: ({shape.x}, {shape.y})")
                        print(f"    -> Size: {shape.width} x {shape.height}")
                        print(f"    -> Fill color: {shape.fill_color}")
            
            # Save the file
            vis.save_vsdx(OUTPUT_FILE)
            print(f"\nSaved to: {OUTPUT_FILE}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

def debug_vsdx():
    """
    Debug function to explore available methods
    """
    try:
        with VisioFile(INPUT_FILE) as vis:
            print(f"=== DEBUG INFO ===")
            print(f"File: {INPUT_FILE}")
            print(f"Pages: {len(vis.pages)}")
            
            page = vis.pages[0]
            shapes = page.child_shapes
            
            for shape in shapes:
                if shape.text and TARGET_SHAPE_TEXT in shape.text:
                    print(f"\n=== Target Shape Debug ===")
                    print(f"Shape type: {type(shape)}")
                    
                    # Show all property-related methods
                    prop_methods = [m for m in dir(shape) if 'prop' in m.lower() or 'data' in m.lower()]
                    print(f"Property methods: {prop_methods}")
                    
                    # Check data_properties specifically
                    if hasattr(shape, 'data_properties'):
                        dp = shape.data_properties
                        print(f"data_properties type: {type(dp)}")
                        print(f"data_properties dir: {[m for m in dir(dp) if not m.startswith('_')]}")
                    
                    break
                
    except Exception as e:
        print(f"Debug error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("=== VSDX Modification ===")
    debug_vsdx()  # Run debug first to see available methods
    print("\n" + "="*50)
    modify_vsdx()   # Then run modification