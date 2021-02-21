import csv
import xml.etree.ElementTree as et

def xml_to_csv(xml_file_path, csv_file_path) -> None:
    tree = et.parse(xml_file_path)
    root_node = tree.getroot()

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        headers = (child.tag for child in root_node[0])
        writer.writerow(headers)
        num_records = len(root_node)

        for record in range(num_records):
            rec = (child.text for child in root_node[record])
            writer.writerow(rec)

if __name__ == '__main__':
    import sys
    import pathlib

    try:
        xml_path = sys.argv[1]
        csv_path = sys.argv[2]
        
    except IndexError:
        sys.exit('Two arguments required. [1] xml source file path, [2] csv destination file path') 
    
    with pathlib.Path(xml_path) as xml_file:
        if xml_file.is_file():
            xml_to_csv(xml_path, csv_path)
        else:
            sys.exit(f'Specified file not found: {xml_path}')