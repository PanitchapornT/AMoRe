import os
import subprocess

def amrfinderplus(input_path, output_name):

    input_path = os.path.abspath(input_path)
    filename = os.path.basename(input_path)
    current_dir = os.getcwd()

    input_docker = input_path + ':/tmp/docker_ana/' + filename
    amr_input = '/tmp/docker_ana/' + filename

    wk_dir = current_dir + ':/wk_dir/'
    output_dir = os.path.join(current_dir, output_name)
   
    command = ['docker', 'run', '--rm', '-v', str(input_docker), '-v', str(wk_dir), 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'amr', 'amrfinder', '-n', str(amr_input)]
    
    try:
        output = subprocess.check_output(command)
        output_text = output.decode("utf-8")
        print(output_text)

        with open(output_dir, "w") as f:
            f.write(output_text)
        print("Output is saved in", output_dir)
    except subprocess.CalledProcessError as e:
        print("Error:", e) 

