from utils import *

filetype = '.png'
mode = 'ht'

def execute():
    # Input format
    # python3 execute.py <program> <input-folder> <output-folder>
    # Script resposible for executing the <program> by reading all entries from <input-folder>
    # and saving the outputs in the <output-folder>.

    if len(argv) != 4:
        print("Usage: python3 execute.py <program> <input-folder> <output-folder>")
        return
    
    main_script = argv[1]
    input_folder = argv[2]
    output_folder = argv[3]
    
    try:
        files = os.listdir(input_folder)
        input_files = [f for f in files if f.endswith(filetype)]

        if not input_files:
            print(f"No input files found in {input_folder}.")
            return
        
        for input_file in sorted(input_files):
            # Run the main script with the input file
            subprocess.run(["python3", main_script, input_file, mode])
            
            
    except FileNotFoundError:
        print(f"Folder {input_folder} not found.")
        return

    except Exception as e:
        print(f"An error occurred: {e}")
        return
    

if __name__ == "__main__":
    execute()

