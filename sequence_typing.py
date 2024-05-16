
def mlst(input_path, output_name):
    import os
    import subprocess
    import pandas as pd
    from io import StringIO
    
    input_path = os.path.abspath(input_path)
    filename = os.path.basename(input_path)
    current_dir = os.getcwd()

    input_docker = input_path + ':/tmp/docker_ana/' + filename
    mlst_input = '/tmp/docker_ana/' + filename

    wk_dir = current_dir + ':/wk_dir/'
    output_dir = os.path.join(current_dir, output_name)

    command = ['docker', 'run', '--rm', '-v', str(input_docker), '-v', str(wk_dir), 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'mlst_env', 'mlst', str(mlst_input)]
    
    try:
        output = subprocess.check_output(command)
        output_text = output.decode("utf-8")
        print('output_text',output_text)

        df = pd.read_csv(StringIO(output_text), sep='\t', header=None)
        
        if not df.empty:
            for i in range(len(df.columns)):
                if i == 0:
                    df = df.rename(columns={i: "FILE"})
                if i == 1:
                    df = df.rename(columns={i: "SCHEME"})
                if i == 2:
                    df = df.rename(columns={i: "ST"})
                if i > 2:
                    loci = df.iloc[0,i].split('(')[0]
                    profile = df.iloc[0,i].split('(')[1]
                    profile = profile.split(')')[0]
                    df = df.rename(columns={i: loci})
                    df[loci] = profile
            df['FILE'] = filename
        df.to_csv(output_dir, sep='\t', index=False)
        print("Output saved to " + output_dir)

         
        if df['SCHEME'].values[0]  == 'abaumannii':
            mlst_command = ['docker', 'run', '--rm', '-v', str(input_docker), '-v', str(wk_dir), 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'mlst_env', 'mlst', '--legacy', '--scheme' ,'abaumannii_2',str(mlst_input)]
            try:
                output = subprocess.check_output(mlst_command)
                output_text = output.decode("utf-8")
                print('output_text',output_text)

            except subprocess.CalledProcessError as e:
                print("Error:", e)

            df = pd.read_csv(StringIO(output_text), sep='\t')
            print(df)
            df['FILE'] = filename

            output_filename = os.path.basename(output_name)
            print(output_filename)
            output_dirname = os.path.dirname(output_name)
            print(output_dirname)
            output_name2 = "scheme_abuamannii_2_" + output_filename
            print(output_name2)
            output_dir = os.path.join(output_dirname, output_name2)
            print(output_dir)
            df.to_csv(output_dir, sep='\t', index=False)
            print("Output saved to " + output_dir)


        if df['SCHEME'].values[0]  == 'abaumannii_2':
            mlst_command = ['docker', 'run', '--rm', '-v', str(input_docker), '-v', str(wk_dir), 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'mlst_env', 'mlst', '--legacy', '--scheme' ,'abaumannii',str(mlst_input)]
            try:
                output = subprocess.check_output(mlst_command)
                output_text = output.decode("utf-8")
                print('output_text',output_text)

            except subprocess.CalledProcessError as e:
                print("Error:", e)

            df = pd.read_csv(StringIO(output_text), sep='\t')
            print(df)
            df['FILE'] = filename

            output_filename = os.path.basename(output_name)
            print(output_filename)
            output_dirname = os.path.dirname(output_name)
            print(output_dirname)
            output_name2 = "scheme_abuamannii_" + output_filename
            print(output_name2)
            output_dir = os.path.join(output_dirname, output_name2)
            print(output_dir)
            df.to_csv(output_dir, sep='\t', index=False)
            print("Output saved to " + output_dir)


        if df['SCHEME'].values[0] == 'ecoli_achtman_4':
            mlst_command = ['docker', 'run', '--rm', '-v', str(input_docker), '-v', str(wk_dir), 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'mlst_env', 'mlst', '--legacy', '--scheme' ,'ecoli',str(mlst_input)]
            try:
                output = subprocess.check_output(mlst_command)
                output_text = output.decode("utf-8")
                print('output_text',output_text)
            except subprocess.CalledProcessError as e:
                print("Error:", e)
            
            df = pd.read_csv(StringIO(output_text), sep='\t')
            print(df)
            df['FILE'] = filename

            output_filename = os.path.basename(output_name)
            print(output_filename)
            output_dirname = os.path.dirname(output_name)
            print(output_dirname)
            output_name2 = "scheme_ecoli_" + output_filename
            print(output_name2)
            output_dir = os.path.join(output_dirname, output_name2)
            print(output_dir)
            df.to_csv(output_dir, sep='\t', index=False)
            print("Output saved to " + output_dir)


        if df['SCHEME'].values[0] == 'ecoli':
            mlst_command = ['docker', 'run', '--rm', '-v', str(input_docker), '-v', str(wk_dir), 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'mlst_env', 'mlst', '--legacy', '--scheme' ,'ecoli_achtman_4',str(mlst_input)]
            try:
                output = subprocess.check_output(mlst_command)
                output_text = output.decode("utf-8")
                print('output_text',output_text)
            except subprocess.CalledProcessError as e:
                print("Error:", e)
            
            df = pd.read_csv(StringIO(output_text), sep='\t')
            print(df)
            df['FILE'] = filename
            output_filename = os.path.basename(output_name)
            print(output_filename)
            output_dirname = os.path.dirname(output_name)
            print(output_dirname)
            output_name2 = "scheme_ecoli_achtman_4_" + output_filename
            print(output_name2)
            output_dir = os.path.join(output_dirname, output_name2)
            print(output_dir)
            df.to_csv(output_dir, sep='\t', index=False)            
            print("Output saved to " + output_dir)
     

    except subprocess.CalledProcessError as e:
        print("Error:", e)
    mlst_process = subprocess.Popen(mlst_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    

def cgmlst(input_path, scheme_path, output_name):
    import os
    import subprocess
    import pandas as pd
    from io import StringIO
    input_path = os.path.abspath(input_path)
    scheme_path = os.path.abspath(scheme_path)
    filename = os.path.basename(input_path)
    current_dir = os.getcwd()
    input_scheme = scheme_path + ':/opt/docker_ana/'
    input_genome = input_path + ':/tmp/' + filename
    wk_dir = current_dir + ':/wk_dir/'
    output_prefix = '/wk_dir/' + str(output_name)
    output_dir = os.path.join(current_dir, output_name)

    subprocess.run(['docker', 'run', '--rm', '-v', str(input_scheme), '-v', str(input_genome), '-v', str(wk_dir), 'panitchapornt/amore:1', 'micromamba', 'run', '-n', 'chewie', 'chewBBACA.py', 'AlleleCall', '-i', '/tmp/', '-g', '/opt/docker_ana/schema_seed/', '-o', str(output_prefix)], text=True)

    print('Outputs are saved in', output_dir)

