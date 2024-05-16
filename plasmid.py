import subprocess
import os

def mobsuite(input_path, output_name):

        input_path = os.path.abspath(input_path)
        filename = os.path.basename(input_path)

        current_dir = os.getcwd()
        input_docker = input_path + ':/tmp/docker_ana/' + filename
        mob_input = '/tmp/docker_ana/' + filename

        wk_dir = current_dir + ':/wk_dir/'

        output_folder = '/wk_dir/' + output_name
        output_dir = os.path.join(current_dir, output_name)

        subprocess.run(['docker', 'run', '--rm', '-v', str(input_docker), '-v', str(wk_dir), 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'mobsuite', 'mob_recon', '-i', str(mob_input), '-o', str(output_folder)], text=True)

        print('Output is saved in', output_dir)


def plasme(input_path, db_path, output_name):

    input_path = os.path.abspath(input_path)
    db_path = os.path.abspath(db_path)
    filename = os.path.basename(input_path)
    current_dir = os.getcwd()
    input_folder = os.path.dirname(input_path)

    db_name = os.path.basename(db_path)

    input_db = db_path + ':/opt/docker_ana/'
    input_genome = input_path + ':/tmp/' + filename
    input_plasme = '/tmp/' + filename
    
    wk_dir = current_dir + ':/wk_dir/'
    output_prefix = '/wk_dir/' + str(output_name)
    output_dir = os.path.join(current_dir, output_name)

    subprocess.run(['docker', 'run', '--rm', '-v', str(input_db), '-v', str(input_genome), '-v', str(wk_dir), '-w', '/opt/docker_ana', 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'base', 'python', 'PLASMe.py', str(input_plasme), str(output_prefix)], text=True)

    print('Outputs are saved in', output_dir)

