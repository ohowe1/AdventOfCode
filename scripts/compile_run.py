import os
import sys
import subprocess
import time

def main():
    # Check if an argument was passed
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <source_file_without_extension>")
        sys.exit(1)

    source_file = sys.argv[1]
    basename = os.path.basename(source_file)
    directory = os.path.dirname(source_file)
    output_file = f"build/{basename}"

    # Ensure the build directory exists
    os.makedirs("build", exist_ok=True)

    # Compile the C++ file using g++-14
    compile_command = ["g++-14", "-x", "c++", "-g", "-O2", "-std=gnu++20", "-o", output_file, source_file]
    compilation = subprocess.run(compile_command)

    # Check if the compilation was successful
    if compilation.returncode == 0:
        try:
            # Run the compiled program with input redirection
            input_file = f"{directory}/input.in"
            with open(input_file, "r") as input_file:
              start_time = time.time()
              run_command = subprocess.run([f"./{output_file}"], stdin=input_file)
              end_time = time.time()
              print(f"Execution time: {end_time - start_time:.2f} seconds")
        except FileNotFoundError:
            print(f"Error: {input_file} file not found.")
            sys.exit(1)
    else:
        print("Compilation failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
