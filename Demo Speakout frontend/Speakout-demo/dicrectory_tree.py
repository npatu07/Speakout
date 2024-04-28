import os

def create_directory_tree(directory, file):
    with open(file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                f.write('{}{}\n'.format(sub_indent, file))

# Specify the directory and output file path
directory = 'C:/Users/Admin/OneDrive/Máy tính/Demo Speakout frontend/Speakout-demo'
output_file = 'directory_tree.txt'

# Call the function to create the directory tree
create_directory_tree(directory, output_file)