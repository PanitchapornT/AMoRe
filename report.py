import pandas as pd
import datetime
import matplotlib.pyplot as plt
import sqlite3
import os
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.io as pio
import mpld3
import matplotlib.pyplot as plt


def metadata(input_metadata):
    filename = input("Please input filename: ")
    isolate_name = input("Please input isolate name: ")
    species_name = input("Please input species: ")
    isolation_source = input("Please input isolation source: ")
    country = input("Please input country: ")
    city = input("Please input city: ")
    if input_metadata==True:
        while True:
            collection_date_str = input("Please input collection date in this format yyyy-mm-dd: ")
            try:
                collection_date = datetime.datetime.strptime(collection_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use yyyy-mm-dd.")
    collection_by = input("Please input collection by: ")
    
    print('\nPlease check:')
    print('filename:' , filename)
    print('Isolate name:', isolate_name)
    print('Species:', species_name)
    print('Isolation source:', isolation_source)
    print('Country:', country)
    print('City:', city)
    print('Collection date:', collection_date)
    print('Collection by:', collection_by)
    
    check = input("Is the information correct? (Y/N): ")
    
    if check.upper() == 'Y':
        print("Metadata is confirmed.")
    elif check.upper() == 'N':
        rounds = int(input('How many inputs were wrong? '))
        for _ in range(rounds):
            wrong_input = input("What information was wrong? Please enter the correct value: ")
            if wrong_input == 'filename' :
                filename = input("Please input filename: ")
            if wrong_input == 'isolate name':
                isolate_name = input("Please input isolate name again: ")
            elif wrong_input == 'species_name':
                species_name = input("Please input species again: ")
            elif wrong_input == 'isolation source':
                isolation_source = input("Please input isolation source again: ")
            elif wrong_input == 'country':
                country = input("Please input country again: ")
            elif wrong_input == 'city':
                city = input("Please input isolate city again: ")
            elif wrong_input == 'collection date':
                while True:
                    collection_date_str = input("Please input collection date again in this format yyyy-mm-dd: ")
                    try:
                        collection_date = datetime.datetime.strptime(collection_date_str, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Invalid date format. Please use yyyy-mm-dd.")
            elif wrong_input == 'collection by':
                collection_by = input("Please input collection by again: ")
            else:
                print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
    
    print("\nMetadata:")
    print('filename: ' , filename )
    print('Isolate name:', isolate_name)
    print('Species:', species_name)
    print('Isolation source:', isolation_source)
    print('Country:', country)
    print('City:', city)
    print('Collection date:', collection_date)
    print('Collection by:', collection_by)

    return filename,isolate_name, species_name, isolation_source, country, city, collection_date, collection_by


def html_metadata(filename, isolate_name, species, isolation_source, country, city, collection_date, collection_by):
    html_metadata_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        h1 {{
            color:#1E3F66;
            }}
        h2 {{
            color:#1E3F66;
            }}    
        h3 {{
            color:#1E4776;
            }}
    * {{
    box-sizing: border-box;
    }}

    /* Create two equal columns that floats next to each other */
    .column {{
    float: left;
    width: 33.33%;
    padding: 10px;
    height: 80px; /* Should be removed. Only for demonstration */
    }}

    /* Clear floats after the columns */
    .row:after {{
    content: "";
    display: table;
    clear: both;
    }}

    /* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
    @media screen and (max-width: 600px) {{
    .column {{
        width: 100%;
    }}
    }}
    </style>
    </head>
    <body>
    """

    html_metadata_content += f"<h1>File: {filename}</h1>"
    
    html_metadata_content += """
    <h2><u>Metadata</u></h2>
    <div class="row">
    <div class="column" >
        <h3>Isolate name</h3>
    """
    html_metadata_content += f"<p>{isolate_name}</p>"

    html_metadata_content += """
    </div>
    <div class="column" >
        <h3>Species</h3>
    """
    html_metadata_content += f"<p>{species}</p>"

    html_metadata_content += """
    </div>
    <div class="column" >
        <h3>Isolation source</h3>
    """
    html_metadata_content += f"<p>{isolation_source}</p>"

    html_metadata_content += """
    </div>
    <div class="column" >
        <h3>Country</h3>
    """
    html_metadata_content += f"<p>{country}</p>"

    html_metadata_content += """
    </div>
    <div class="column" >
        <h3>City/Region</h3>
    """
    html_metadata_content += f"<p>{city}</p>"

    html_metadata_content += """
    </div>
    </div>
    <div class="row">
    <div class="column" >
        <h3>Collection date</h3>
    """
    html_metadata_content += f"<p>{collection_date}</p>"

    html_metadata_content += """
    </div>
    <div class="column" >
        <h3>Collected by</h3>
    """
    html_metadata_content += f"<p>{collection_by}</p>"

    html_metadata_content += """
    </div>
    <div class="column" >
        <h3></h3>
        <p></p>
    </div>
    <p>&nbsp;</p> 
    <p></p> 
    </body>
    </html>
    """
    
    return html_metadata_content


def html_assembly_stats(input_qc):
    asm_qc = pd.read_csv(input_qc, sep='\t')
    contig = str(asm_qc['Number of contigs'].values[0])
    sequence_length = str(asm_qc['Sequence length'].values[0])
    avg_sequence_length = str(asm_qc['Average sequence length'].values[0])
    min_sequence_length = str(asm_qc['Minimal sequence length'].values[0])
    max_sequence_length = str(asm_qc['Maximal sequence length'].values[0])
    gc = str(asm_qc['GC%'].values[0])
    n50 = str(asm_qc['N50'].values[0])
    l50 = str(asm_qc['L50'].values[0])
    n75 = str(asm_qc['N75'].values[0])
    l75 = str(asm_qc['L75'].values[0])
    html_assembly_content = """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        h1 {
            color:#1E3F66;
            }
            h2 {
            color:#1E3F66;
            }  
        h3 {
            color:#1E4776;
            }
    * {
    box-sizing: border-box;
    }

    /* Create two equal columns that floats next to each other */
    .column {
    float: left;
    width: 33.33%;
    padding: 10px;
    height: 80px; /* Should be removed. Only for demonstration */
    }

    /* Clear floats after the columns */
    .row:after {
    content: "";
    display: table;
    clear: both;
    }

    /* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
    @media screen and (max-width: 600px) {
    .column {
        width: 100%;
    }
    }
    </style>
    </head>
    
    
    <body>
    <h2><u>Assembly stats</u></h2>
    <div class="row">
    <div class="column" >
        <h3>Number of contigs</h3>
        """
    html_assembly_content += "<p>"
    html_assembly_content += format(int(contig),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>Sequence length</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(int(sequence_length),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>Average sequence length</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(float(avg_sequence_length),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>Minimal sequence length</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(int(min_sequence_length),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>Maximal sequence length</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(int(max_sequence_length),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>GC%</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(float(gc),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>N50</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(int(n50),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>L50</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(int(l50),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>N75</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(int(n75),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3>L75</h3>
    """
    html_assembly_content += "<p>"
    html_assembly_content += format(int(l75),",")
    html_assembly_content += "</p>"
    html_assembly_content += """
    </div>
    <div class="column" >
        <h3></h3>
        <p></p>
    </div>
    <div class="column" >
        <h3></h3>
        <p></p>
    </div>
    <p>&nbsp;</p> 
    <p></p>
    </body>
    </html>
    """
    
    return html_assembly_content


def remove_multiple_allleles(df):
    l = len(list(df.split(",")))
    mp = []
    st = ''
    n = 0
    if l == 1:
        return df.split(",")[0]
    else:
        for n in range(l):
            if n == 0:
                mp.append(str(df.split(",")[n]))
                st = df.split(",")[n]
            else:
                if n < l:
                    if str(df.split(",")[n]) not in mp:
                        mp.append(df.split(",")[n])
                        st = st + "," + df.split(",")[n]  
                        n += 1
        return st


def html_mlst(mlst, conn):
    df_mlst = pd.read_csv(mlst, sep='\t')
    df_mlst = df_mlst.astype(str)
    loci = df_mlst.columns.to_list()
    loci = loci[3:]

    for locus in loci:
        df_mlst[locus] = df_mlst[locus].map(remove_multiple_allleles)

    allele1 = df_mlst[loci[0]][0]
    allele2 = df_mlst[loci[1]][0]
    allele3 = df_mlst[loci[2]][0]
    allele4 = df_mlst[loci[3]][0]
    allele5 = df_mlst[loci[4]][0]
    allele6 = df_mlst[loci[5]][0]
    allele7 = df_mlst[loci[6]][0]
    scheme = df_mlst['SCHEME'][0]

    if df_mlst['ST'][0] == '-':
        if scheme == 'ecoli':
            allele8 = df_mlst[loci[7]][0]
            profile_sql = f"SELECT sequence_type FROM MLST \
                            WHERE scheme='{str(scheme)}' \
                            AND allele1='{str(allele1)}' \
                            AND allele2='{str(allele2)}' \
                            AND allele3='{str(allele3)}' \
                            AND allele4='{str(allele4)}' \
                            AND allele5='{str(allele5)}' \
                            AND allele6='{str(allele6)}' \
                            AND allele7='{str(allele7)}' \
                            AND allele8='{str(allele8)}' \
                            LIMIT 1;"
            profile = pd.read_sql_query(profile_sql, conn)
            st = profile['sequence_type'][0]
        else:
            profile_sql = f"SELECT sequence_type FROM MLST \
                            WHERE scheme='{str(scheme)}' \
                            AND allele1='{str(allele1)}' \
                            AND allele2='{str(allele2)}' \
                            AND allele3='{str(allele3)}' \
                            AND allele4='{str(allele4)}' \
                            AND allele5='{str(allele5)}' \
                            AND allele6='{str(allele6)}' \
                            AND allele7='{str(allele7)}' \
                            LIMIT 1 ;"
            profile = pd.read_sql_query(profile_sql, conn)
            if profile.empty == False:
                st = profile['sequence_type'][0]
                df_mlst['ST'][0] = st
            else:
                st = '-'
                df_mlst['ST'][0] = st

    if scheme=='ecloacae':
        enterobacter = pd.read_sql_query("SELECT * FROM MLST_enterobacter", conn)
        if st in enterobacter['sequence_type'].values:
            species = enterobacter['species'][enterobacter['sequence_type']==st][0]
        else:
            asm_sql = f"SELECT asm_acc FROM MLST WHERE scheme='{scheme}' LIMIT 1;"
            asm_df = pd.read_sql_query(asm_sql, conn)
            asm = asm_df['asm_acc'][0]
            species_sql = f"SELECT species FROM Metadata WHERE asm_acc='{asm}' LIMIT 1;"
            species_df = pd.read_sql_query(species_sql, conn)
            species_name = species_df['species'][0]
    else:
        asm_sql = f"SELECT asm_acc FROM MLST WHERE scheme='{scheme}' LIMIT 1;"
        asm_df = pd.read_sql_query(asm_sql, conn)
        asm = asm_df['asm_acc'][0]
        species_sql = f"SELECT species FROM Metadata WHERE asm_acc='{asm}' LIMIT 1;"
        species_df = pd.read_sql_query(species_sql, conn)
        species_name = species_df['species'][0]

    html_mlst_table = df_mlst.to_html(index=False)

    html_mlst = f"""
    <html>
    <head>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #E1EDFA;
            }}
        </style>
    </head>
    <body>
        <h2><u>MLST</u></h2>
        {html_mlst_table}
    </body>
    </html>
    """
    
    return html_mlst, species_name, df_mlst


def mlst_report_graph (df_mlst, conn):

    scheme = df_mlst['SCHEME'][0]
    st = df_mlst['ST'][0]
    mlst = pd.read_sql_query(f"SELECT asm_acc FROM MLST WHERE scheme = '{scheme}' AND sequence_type = '{st}' ;", conn)
    mlst_values = mlst['asm_acc'].unique()
    df_mlst_metadata = pd.read_sql_query(f"SELECT geo_name, collection_year FROM Metadata WHERE asm_acc IN {tuple(mlst_values)};", conn)

    country_counts = df_mlst_metadata['geo_name'].value_counts().reset_index()
    country_counts.columns = ['geo_name', 'count']
    country_counts = country_counts[country_counts['geo_name']!='not provided']
    country_counts = country_counts.head(10)

    year_counts = df_mlst_metadata['collection_year'].value_counts().reset_index()
    year_counts.columns = ['collection_year', 'count']
    year_counts = year_counts[year_counts['collection_year']!='-']
    year_counts = year_counts.sort_values(by='collection_year', ascending=True)

    trace1 = go.Bar(
        x=country_counts['geo_name'],
        y=country_counts['count'],
        name='Plot 1'
    )
    trace2 = go.Bar(
        x=year_counts['collection_year'],
        y=year_counts['count'],
        name='Plot 2'
    )

    layout_country = go.Layout(
        title='Number of isolates per country',
        xaxis=dict(title='Country'),
        yaxis=dict(title='Count')
    )
    layout_year = go.Layout(
        title='Number of isolates per year',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Count')
    )

    fig1 = go.Figure(data=[trace1], layout=layout_country)

    fig2 = go.Figure(data=[trace2], layout=layout_year)

    plot_div1 = plot(fig1, output_type='div', include_plotlyjs=False)
    plot_div2 = plot(fig2, output_type='div', include_plotlyjs=False)

    html_plot_mlst = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTML Page with Two Bar Plots</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <style>
            .plot-container {{
                display: flex;
                justify-content: space-between;
            }}
            .plot {{
                width: 45%; /* Adjust width as needed */
            }}
        </style>
    </head>
    <body>
        <!-- Container for plots -->
        <div class="plot-container">
            <!-- Plot 1 -->
            <div class="plot" id="plot_div1">
                {plot_div1}
            </div>

            <!-- Plot 2 -->
            <div class="plot" id="plot_div2">
                {plot_div2}
            </div>
        </div>
    </body>
    </html>
    """

    return html_plot_mlst

def length_plot(species, mlst, input_qc, conn):
    
    asm_qc = pd.read_csv(input_qc, sep='\t')
       
    df_length = pd.read_sql_query(f"SELECT * FROM length_stat WHERE species = '{species}' ", conn)
    df_gc = pd.read_sql_query(f"SELECT * FROM gc_stat WHERE species = '{species}'", conn)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    ax1.boxplot([[], [df_length['q1'][0], df_length['q2'][0], df_length['q3'][0]], []], showfliers=False, widths=0.5)
    ax1.scatter([2], asm_qc['Sequence length'][0], color='red', label='Genome length')
    ax1.set_xticks([])
    ax1.set_ylabel('Sequence length')
    ax1.set_title('Sequence length')
    ax1.legend()
    
    ax2.boxplot([[], [df_gc['q1'][0], df_gc['q2'][0], df_gc['q3'][0]], []], showfliers=False, widths=0.5)
    ax2.scatter([2], asm_qc['GC%'][0], color='red', label='GC%')
    ax2.set_xticks([])
    ax2.set_ylabel('GC%')
    ax2.set_title('GC%')
    ax2.legend()
    
    length_gc_html_plot = mpld3.fig_to_html(fig)
    return length_gc_html_plot


def html_plasme_amr(plasme, amr):
    df_plasme = pd.read_csv(plasme, sep='\t')
    df_amr = pd.read_csv(amr, sep='\t')

    df_plasme = df_plasme.rename(columns={'contig':'contig_id'})
    df_plasme['Molecule type']='Plasmid'

    df_amr =df_amr.rename(columns={'Contig id':'contig_id'})

    df = df_plasme.merge(df_amr, on ='contig_id', how='right')
    df['Molecule type'] = df['Molecule type'].fillna('Chromosome')

    df_amr_analysis = df[['Gene symbol', 'Class', 'Molecule type']]
    df_amr_analysis = df_amr_analysis.rename(columns={'Class':'Drug class'})
    df_amr_analysis = df_amr_analysis.drop_duplicates()

    html_amr_table = df_amr_analysis.to_html(index=False)
    html_amrfinder = f"""
    <html>
    <head>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #E1EDFA;
            }}
        </style>
    </head>
    <body>
        <h2><u>AMR analysis</u></h2>
        {html_amr_table}
    </body>
        <body>
        <h2><u>Plasmid typing</u></h2>
    </body>
    </html>
    """
    return html_amrfinder


def plasmid_typing(species, plasme, conn):
    plsdb = pd.read_sql_query(f"SELECT * FROM plsdb", conn)
    df_plasme = pd.read_csv(plasme, sep='\t')
    if df_plasme.empty == False:
   
        check_length = df_plasme[(df_plasme['length'] <= 350000) & (df_plasme['length'] >= 1000)]
        check_length = check_length.rename(columns={'length':'plasme_length'})
        plsdb = plsdb.rename(columns={'NUCCORE_Length':'ref_length'})
        plsdb = plsdb.rename(columns={'NUCCORE_ACC':'reference'})
        df_coverage_plsdb = check_length.merge(plsdb, on = 'reference', how = 'inner')

        df_coverage_plsdb['coverage'] = df_coverage_plsdb['plasme_length']/df_coverage_plsdb['ref_length']

        iqr = df_coverage_plsdb.copy()
        iqr = iqr.drop_duplicates()

        ref = iqr['reference'].unique()
        if len(ref) > 1:
            query = f"""
            SELECT PLASMe.asm_acc, PLASMe.reference ,PLASMe.length FROM PLASMe WHERE PLASMe.reference IN {tuple(ref)} 
            AND PLASMe.asm_acc IN (SELECT METADATA.asm_acc FROM METADATA WHERE METADATA.species ='{species}')"""
        else:

            query = f"""
            SELECT PLASMe.asm_acc, PLASMe.reference ,PLASMe.length FROM PLASMe WHERE PLASMe.reference='{ref[0]}' 
            AND PLASMe.asm_acc IN (SELECT METADATA.asm_acc FROM METADATA WHERE METADATA.species ='{species}')"""
        df_db = pd.read_sql_query(query, conn)

        df_db = df_db.rename(columns={'length':'db_length'})
        df_coverage_db = iqr.merge(df_db, on = 'reference', how = 'inner')

        df_coverage_db['coverage_db'] = df_coverage_db['db_length']/df_coverage_db['plasme_length']
        df_coverage_db['coverage2_db'] = df_coverage_db['plasme_length']/df_coverage_db['db_length'] 

        df_plasme_done = df_coverage_db[df_coverage_db['coverage2_db'] >= 0.9]

        ref_plasme = df_plasme_done['asm_acc'].unique()
        df_plasme_metadata = pd.read_sql_query(f"SELECT asm_acc, geo_name, collection_year FROM Metadata WHERE asm_acc IN{tuple(ref_plasme)};", conn)
        plasmid_typing = df_plasme_done.merge(df_plasme_metadata, on='asm_acc', how='left')
        
        plasmid_typing2 = plasmid_typing.dropna(subset=['geo_name', 'collection_year'])
        df = plasmid_typing2.copy()
        df = df[['asm_acc','contig','reference','geo_name', 'collection_year']]
        df = df.drop_duplicates()
        year = df.groupby(['reference', 'collection_year']).size().reset_index(name='count')
        year = year[year['collection_year']!='-']
        geo_name = df.groupby(['reference', 'geo_name']).size().reset_index(name='count')
        geo_name = geo_name.sort_values(by=['reference', 'count'], ascending=[True, False])
        geo_name = geo_name[geo_name['geo_name']!='not provided']
        top_10_geo = geo_name.groupby('reference').head(10).reset_index(drop=True)

        return year, top_10_geo
    else:
        year=False
        top_10_geo=False
        return year, top_10_geo


def plot_plasmid_typing(ref, plasmid_country, plasmid_year):
    
    html_plot_plasmid_typing = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Plasmid typing</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            <style>
                .plot-container {{
                    display: flex;
                    justify-content: space-between;
                }}
                .plot {{
                    width: 45%; /* Adjust width as needed */
                }}
            </style>
        </head>
        <body>
            <h3>{ref}</h1>
            
            <!-- Container for plots -->
            <div class="plot-container">
                <!-- Plot 1 -->
                <div class="plot" id="plot_div1">
                    {plasmid_country}
                </div>

                <!-- Plot 2 -->
                <div class="plot" id="plot_div2">
                    {plasmid_year}
                </div>
            </div>
        </body>
        </html>
        """

    return html_plot_plasmid_typing


def custom_convert(value):
    try:
        return str(int(value))
    except ValueError:
        return '-'


def hamming_distance(str1, str2):
    return np.sum(str1 != str2)


def closest_hamming_distance(target, database):
    min_distance = float('inf')
    outidx = None
    closest_dist = []
    closest_idx = []
    closest_db = None
    for idx, db in enumerate(database):
        distance = hamming_distance(target, db)
        if distance <= 100:
            closest_dist.append(distance)
            closest_idx.append(idx)
            if distance < min_distance:
                min_distance = distance
                closest_db = db
                outidx = idx
    return min_distance, closest_db, outidx, closest_dist, closest_idx


def closest_genome(mlst, cgmlst, species, conn):

    mlst_data =pd.read_csv(mlst ,sep ='\t')
    species_to_cgmlst = {
        "cgmlst": ["cgMLST_acinetobacter_baumannii", "cgMLST_enterococcus_faecium", "cgMLST_escherichia_coli" ,"cgMLST_klebsiella_pneumoniae",
                  "cgMLST_pseumonas_aeruginosa","cgMLST_staphylococcus_aureus","cgMLST_streptococcus_pneumoniae" ],
        "species" : ["Acinetobacter baumannii",  "Enterococcus faecium","Escherichia coli", "Klebsiella pneumoniae" , "Pseudomonas aeruginosa",
                    "Staphylococcus aureus" , "Streptococcus pneumoniae"]}
    df_species_to_cgmlst = pd.DataFrame(species_to_cgmlst)

    if species in species_to_cgmlst['species']:
        scheme_name = df_species_to_cgmlst.loc[df_species_to_cgmlst['species'] == species, 'cgmlst'].iloc[0]
        scheme_sql = f"SELECT * FROM {scheme_name}"
        df_cgmlst = pd.read_sql_query(scheme_sql, conn)
        df_cgmlst2 = df_cgmlst.drop(columns=['asm_acc'])
        df_cgmlst2['set_profile'] = df_cgmlst2['set_profile'].apply(eval)

    cgmlst_report = pd.read_csv(cgmlst, sep='\t')
    cgmlst_report = cgmlst_report.drop(columns=['FILE'])

    alleles_index = pd.read_sql_query(f"SELECT * FROM alleles_index;", conn)
    alleles_index['alleles_index'] = alleles_index['alleles_index'].apply(eval)

    if species in species_to_cgmlst['species']:
        set_alleles = np.array(alleles_index['alleles_index'][alleles_index['species'] == species].tolist())
        loci = set_alleles[0]
        number_loci = len(loci)
        #cgmlst_report = cgmlst_report[loci]

    for col in cgmlst_report.columns:
        cgmlst_report[col] = cgmlst_report[col].apply(custom_convert)
        
    cgmlst_report['set_profile'] = cgmlst_report.values.tolist()
    
    set_profiles = np.array(df_cgmlst2['set_profile'].tolist())
    targets = np.array(cgmlst_report['set_profile'].tolist())

    min_distance, closest_db, outidx, closest_dist, closest_idx = closest_hamming_distance(targets, set_profiles)

    if len(closest_idx) != 0:
        closest_genome = df_cgmlst['asm_acc'][outidx]
        closest_genome50 = []
        for i in closest_idx:
            closest_genome50.append(df_cgmlst['asm_acc'][i])
        closeset_sql = f"SELECT asm_acc, geo_name, collection_year FROM Metadata WHERE SUBSTRING(asm_acc, 1, 13) IN {tuple(closest_genome50)};"
        df_cgmlst_metadata = pd.read_sql_query(closeset_sql, conn)
        df_cgmlst_metadata['geo_name'][df_cgmlst_metadata['geo_name']=='not provided'] = '-'
        df_cgmlst_metadata['Distance'] = closest_dist
        df_cgmlst_metadata = df_cgmlst_metadata.sort_values(by='Distance', ascending=True).reset_index(drop=True)
        df_cgmlst_metadata = df_cgmlst_metadata.head(10)
        asm = df_cgmlst_metadata['asm_acc'].to_list()
        mlst_sql = f"SELECT asm_acc, scheme, sequence_type FROM MLST WHERE asm_acc IN{tuple(asm)}"
        df_mlst = pd.read_sql_query(mlst_sql, conn)
        scheme_list = df_mlst['scheme'].unique().tolist()
        if len(scheme_list) == 1:
            df_mlst = df_mlst.drop(columns=['scheme'])
            df_cgmlst_metadata = df_cgmlst_metadata.merge(df_mlst, on='asm_acc')
            df_cgmlst_metadata = df_cgmlst_metadata.rename(columns={'asm_acc':'Assembly accession number','geo_name':'Country','collection_year':'Collection year','sequence_type':f'ST (MLST: {scheme_list[0]})'})
            df_cgmlst_metadata = df_cgmlst_metadata[['Assembly accession number', 'Distance', 'Country', 'Collection year', f'ST (MLST: {scheme_list[0]})']]
        else:
            scheme1 = df_mlst[df_mlst['scheme']==scheme_list[0]]
            scheme1 = scheme1.drop(columns=['scheme'])
            scheme2 = df_mlst[df_mlst['scheme']==scheme_list[1]]
            scheme2 = scheme2.drop(columns=['scheme'])
            df_cgmlst_metadata = df_cgmlst_metadata.merge(scheme1, on='asm_acc')
            df_cgmlst_metadata = df_cgmlst_metadata.merge(scheme2, on='asm_acc')
            df_cgmlst_metadata['Distance'] = df_cgmlst_metadata['Distance'].astype(str) + "/" + str(number_loci)
            df_cgmlst_metadata = df_cgmlst_metadata.rename(columns={'asm_acc':'Assembly accession number','geo_name':'Country','collection_year':'Collection year','sequence_type_x':f'ST (MLST: {scheme_list[0]})', 'sequence_type_y':f'ST (MLST: {scheme_list[1]})'})
            df_cgmlst_metadata = df_cgmlst_metadata[['Assembly accession number', 'Distance', 'Country', 'Collection year', f'ST (MLST: {scheme_list[0]})', f'ST (MLST: {scheme_list[1]})']]

        html_closest_table = df_cgmlst_metadata.to_html(index=False)
    else:
        html_closest_table = '<h3>Not found</h3>'
    html_closest = f"""
    <html>
    <head>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #E1EDFA;
            }}
        </style>
    </head>
    <body>
        <h2><u>Closest genome</u></h2>
        {html_closest_table}
    </body>
    </html>
    """

    return html_closest


#----------------------------------------------------------------------------------------------------
def amr_analysis_report(asm_qc, mlst, cgmlst, plasme, amr, output_name, db, mlst2=False, input_metadata = False):
    import pandas as pd
    import datetime
    import matplotlib.pyplot as plt
    import sqlite3
    import os
    import numpy as np
    import plotly.graph_objs as go
    from plotly.offline import plot
    import plotly.io as pio
    import mpld3
    import matplotlib.pyplot as plt
    conn = sqlite3.connect(db)
    current_dir = os.getcwd()
    report_path = os.path.join(current_dir, f"{output_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html")
    with open(report_path, 'w') as f:
        if input_metadata == True:
            filename, isolate_name, species_name, isolation_source, country, city, collection_date, collection_by = metadata(input_metadata)
            html_content_metadata = html_metadata(filename, isolate_name, species_name, isolation_source, country, city, collection_date, collection_by)
            f.write(html_content_metadata)
        html_content_qc = html_assembly_stats(asm_qc)
        html_content_mlst, species_name, df_mlst = html_mlst(mlst, conn)
        html_graph_qc = length_plot(species_name, mlst, asm_qc, conn)
        html_graph_mlst = mlst_report_graph(df_mlst, conn)
        print("Assembly stats.....")
        f.write(html_content_qc)
        f.write(html_graph_qc)
        print("MLST.....")
        f.write(html_content_mlst)
        f.write(html_graph_mlst)
        if mlst2!=False:
            html_content_mlst2, species_name2, df_mlst2 = html_mlst(mlst2, conn)
            html_graph_mlst2 = mlst_report_graph(df_mlst2, conn)
            f.write(html_content_mlst2)
            f.write(html_graph_mlst2)

        html_content_amr = html_plasme_amr(plasme, amr)
        print("AMR analysis.....")
        f.write(html_content_amr)
        
        year, top_5_geo = plasmid_typing(species_name, plasme, conn)
        print("Plasmid typing.....")
        if (year!=False) & (top_5_geo!=False):
            for ref in year['reference'].unique():

                trace1 = go.Bar(
                x=top_5_geo['geo_name'][top_5_geo['reference']==ref],
                y=top_5_geo['count'][top_5_geo['reference']==ref],
                name='Plot 1')

                trace2 = go.Bar(
                x=year['collection_year'][year['reference']==ref],
                y=year['count'][year['reference']==ref],
                name='Plot 2')

                layout_country = go.Layout(
                title='Number of isolates per country',
                xaxis=dict(title='Country'),
                yaxis=dict(title='Count'))

                layout_year = go.Layout(
                title='Number of isolates per year',
                xaxis=dict(title='Year'),
                yaxis=dict(title='Count'))

                fig1 = go.Figure(data=[trace1], layout=layout_country)
                fig2 = go.Figure(data=[trace2], layout=layout_year)

                plot_div1 = plot(fig1, output_type='div', include_plotlyjs=False)
                plot_div2 = plot(fig2, output_type='div', include_plotlyjs=False)
                html_plasmid_typing = plot_plasmid_typing(ref, plot_div1, plot_div2)
                f.write(html_plasmid_typing)
        print("Closest genome.....")
        html_content_closeset_genome = closest_genome(mlst, cgmlst, species_name, conn)
        f.write(html_content_closeset_genome)

        print("Output saved to " + report_path)
        
    conn.close()

