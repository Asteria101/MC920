from utils import *

def textify():
    # Input format
    # python3 textify.py <input-folder> <output-folder>

    if len(argv) != 3:
        print("Usage: python3 textify.py <input-folder> <output-folder>")
        return
    
    input_folder = argv[1]
    output_folder = argv[2]

    try:
        files = os.listdir(input_folder)
        input_files = [f for f in files if (f.endswith('.png') and f.startswith('rot_'))]

        if not input_files:
            print(f"No input files found in {input_folder}.")
            return

        for input_file in sorted(input_files):
            subprocess.run(["tesseract", os.path.join(input_folder, input_file), os.path.join(output_folder, input_file[:-4])])

    except FileNotFoundError:
        print(f"Folder {input_folder} not found.")
        return

    except Exception as e:
        print(f"An error occurred: {e}")
        return

if __name__ == "__main__":
    textify()