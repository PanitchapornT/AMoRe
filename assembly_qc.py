import os
from Bio import SeqIO
from io import StringIO
import pandas as pd
import numpy as np
    
def input_qc(input_path, output_name):
    sequence = SeqIO.parse(input_path, "fasta")
    number_of_contigs = 0
    total_length = 0
    g_count = 0
    c_count = 0
    list_length = []
    n50 = 0
    n75 = 0
    length_50 = 0
    length_75 = 0
    number_of_contigs_50 = 0
    number_of_contigs_75 = 0

    for contig in sequence:
        number_of_contigs += 1
        total_length += len(contig)
        g_count += contig.seq.upper().count("G")
        c_count += contig.seq.upper().count("C")
        l = len(contig)
        list_length.append(l)

    gc_content = (g_count + c_count)/total_length*100
    list_length = sorted(list_length, reverse=True)
    avg_length = total_length/number_of_contigs

    half_length = total_length/2
    for i in list_length:
        length_50 += i
        number_of_contigs_50 += 1
        if length_50 >= half_length:
            n50 = i
            break

    seventy_five_length = total_length/2
    for j in list_length:
        length_75 += j
        number_of_contigs_75 += 1
        if length_75 >= seventy_five_length:
            n75 = j
            break

    output = ( f"Number of contigs: {int(number_of_contigs)}\n"
    f"Sequence length: {int(total_length)}\n"
    f"Average sequence length: {avg_length:.2f}\n"
    f"Minimal sequence length: {int(list_length[-1])}\n"
    f"Maximal sequence length: {int(list_length[0])}\n"
    f"GC%: {gc_content:.2f}\n"
    f"N50: {int(n50)}\n"
    f"L50: {int(number_of_contigs_50)}\n"
    f"N75: {int(n75)}\n"
    f"L75: {int(number_of_contigs_75)}\n" )

    print(output)

    data = {'Number of contigs':int(number_of_contigs), 'Sequence length':int(total_length),
            'Average sequence length':round(avg_length,2), 'Minimal sequence length':int(list_length[-1]),
            'Maximal sequence length':int(list_length[0]), 'GC%':round(gc_content,2), 'N50':int(n50),
            'L50':int(number_of_contigs_50), 'N75':int(n75), 'L75':int(number_of_contigs_75)}
    qc_output = pd.DataFrame(data, index=[0])
    #print(qc_output)

    input_path = os.path.abspath(input_path)
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir , output_name)

    qc_output.to_csv(output_dir , sep='\t', index=False)
    print("Output saved to " + output_dir)

    



