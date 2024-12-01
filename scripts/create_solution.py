import argparse
import os.path


def create_run_config(title, code_file, input_file, output_file):
    try:
        # Read the appropriate template file based on the language
        with open(input_file, 'r') as file:
            content = file.read()

        # Replace all occurrences of 'template' with the given title
        modified_content = content.replace('!!NAME!!', title).replace('!!PATH!!', code_file)

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Successfully created {output_file}.")
    except FileNotFoundError as e:
        print(f"File error: " + e)
    except Exception as e:
        print(f"An error occurred: {e}")

def create_source_file(title, input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            
        # Write the modified content to the output file
        if not os.path.exists(output_file):
            with open(output_file, 'w') as file:
                file.write(content)
            print(f"Successfully created {output_file}.")
        else:
            print('Skipped creating as source file already exists')

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Replace 'template' in a C++ or Python XML configuration file.")
    parser.add_argument("title", type=str, help="The title to replace 'template' with.")

    parser.add_argument("--no-run-config", action="store_true", help="Skip creating the run configuration for CLion.")
    parser.add_argument("--no-source-file", action="store_true", help="Skip creating the source file from the template.")
    
    args = parser.parse_args()

    base_name = os.path.basename(args.title)
    file_title = base_name.split('.')[0]
    language = base_name.split('.')[-1]

    this_directory = os.path.dirname(__file__)
    # Map the aliases to the correct language
    if language == 'cpp':
        run_config_file = os.path.join(this_directory, 'templates/template__cpp_.xml')
        source_file = os.path.join(this_directory, 'templates/template.cpp')
    elif language == 'py':
        run_config_file = os.path.join(this_directory, 'templates/template__py_.xml')
        source_file = os.path.join(this_directory, 'templates/template.py')
    else:
        print('Unrecognized File Extension')
        return

    # Call the function to replace 'template' with the given title
    if not args.no_run_config:
        create_run_config(file_title, args.title, run_config_file, f'.idea/runConfigurations/{file_title}.xml')
        
    if not args.no_source_file:
        create_source_file(file_title, source_file, args.title)
        

if __name__ == "__main__":
    main()
