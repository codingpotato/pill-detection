"""
Convert label xml to csv
"""
import os
import glob
import xml.etree.ElementTree as ET
import pandas as pd


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def convert(csv_prefix):
    annotation_path = os.environ['ANNOTATION_DIR']
    train_dir = os.environ['TRAIN_DIR']

    xml_df_train = xml_to_csv(os.path.join(annotation_path, csv_prefix + '_*.xml'))
    train_csv_path = os.path.join(train_dir, csv_prefix + '.csv')
    xml_df_train.to_csv(train_csv_path, index=None)


def main():
    convert('train')
    convert('eval')
    print('Successfully converted xml to csv.')


if __name__ == '__main__':
    main()
