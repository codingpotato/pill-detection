"""
Generate label map
"""
import os

def main():
    label_map_path = os.path.join(os.environ['TRAIN_DIR'], 'label_map.pbtxt')
    with open(label_map_path, 'w') as f:
        for index in range(1, 9):
            text = "item {\n  id: " + str(index) + "\n  name: '" + str(index) + "'\n}\n\n"
            f.write(text)


if __name__ == '__main__':
    main()
