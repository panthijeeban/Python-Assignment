#!/usr/bin/env python3

import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

#Function to count the observed kmers
def count_kmers(seq, k):
    counts = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] += 1
    return counts

#Function to produce a table in csv format for every sequence
def generate_file(file_name, detail_data, seq_name):
    data = pd.DataFrame([[i[0], i[1], i[2]] for i in detail_data], columns=['k value', 'Observed kmers', 'Possible kmers'])
    data.to_csv('output/data_out/'+ file_name + '_' + seq_name+'.csv', index=False)

#Function to generate a linguistic complexity bar diagram graph of all sequences
def generate_complexity_graph(file_name, seq_name_list, linguistic_complexity_list):       
    plt.plot(seq_name_list, linguistic_complexity_list, 'ro')
    plt.xlabel('Name of the sequence',color='r',fontsize=12)
    plt.ylabel('Linguistic complexity',color='r',fontsize=12)
    plt.title('Linguistic complexity of sequences',color='b',fontsize=12)
    graph_name = file_name + '_complexity.png'
    plt.savefig('output/image_out/'+graph_name)

#Function to generate possible and observed kmers of all sequence of all possible value of k
def generate_kmers_graph(file_name, seq_name_list, possible_total_list, observed_total_list):
    fig, ax = plt.subplots()
    index = np.arange(len(seq_name_list))
    bar_width = 0.5
    opacity = 0.75
    rects1 = plt.bar(index, possible_total_list, bar_width,alpha=opacity,color='r',label='Possible K-mers')
    rects2 = plt.bar(index + bar_width, observed_total_list, bar_width,alpha=opacity,color='b',label='Observed K-mers')
    plt.xlabel('Name of the sequence')
    plt.ylabel('K-mers')
    plt.title('K-mers for each sequence')
    plt.xticks(index + bar_width, seq_name_list)
    plt.legend()
    plt.tight_layout()
    graph_name = file_name + '_kmers.png'
    plt.savefig('output/image_out/'+graph_name)

#Function to find the wrong DNA characters (other than ATGC)
def check_seq_format(seq):
    bad_chars = {}
    for i in seq:
        if i not in 'AGCT':
            if i in bad_chars: bad_chars[ i ] += 1
            else: bad_chars[ i ] = 1
    if bad_chars != {}: return bad_chars

#Function to generate wrong DNA for each sequence  
def generate_wrong_dna_graph(file_name, data, seq_name):
    plt.clf()
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()))
    graph_name = 'wrong_DNA_'+ file_name + '_' + seq_name + '.png'
    plt.savefig('output/image_out/'+graph_name)

#Main function
if __name__ == "__main__":
    file_name=sys.argv[1]    #1 means end user can provide only the file, not the value of k.
    if file_name in glob.glob('*.fasta'): #limited only to .fasta format
        f = open(file_name,'r')
        seq = f.readlines()
        file_name = file_name.replace('.', '_') #replaced . with _ in file names
        seq_name_list = []
        observed_total_list = []
        possible_total_list = []
        linguistic_complexity_list = []
        for line_num, line in enumerate(seq[0:len(seq)]):
            if len(line) > 1 :
                if '>' in line :
                    line = line.replace(">", "") #Removing > sign that appears in front of each sequence name
                    seq_name = line.rstrip()
                    seq_name_list.append(seq_name) #append is to add
                else:
                    seq = line.rstrip()
#Check per each sequence name, the sequence format
                    seq_format = check_seq_format(seq)  
                    k_list = []
                    possible_list = []
                    observed_list = []
                    for k in range(1,len(seq)+1):
                        #check the possible kmers
                        if 4**k < len(seq):
                            possible = 4**k 
                        else:
                            possible = len(seq) - k + 1   #The logic is if 4**k is less than the length of sequence, possible is 4*k, otherwise length of the sequence-k+1                      
                        #get the kmers
                        counts = count_kmers(seq, k)
                        #get the observed kmers  
                        observed = len(counts)
                        k_list.append(k)
                        possible_list.append(possible)                          
                        observed_list.append(observed)                        
                    #get the total possible kmers                        
                    possible_total = sum(possible_list)  
                    possible_list.append(possible_total)
                    possible_total_list.append(possible_total)
                    #get the total observed kmers
                    observed_total = sum(observed_list)
                    observed_list.append(observed_total)

                    observed_total_list.append(observed_total)
                    k_list.append('Total sum'); 
                    
#Merge kmers-data for all the sequence
                    print(observed_list)
                    detail_data = list(zip(k_list, observed_list, possible_list))
#Function to generate file per each sequence name                      
                    detail = generate_file(file_name, detail_data, seq_name)
                    #Compute the linguistic complexity
                    linguistic_complexity = observed_total/possible_total
                    linguistic_complexity_list.append(linguistic_complexity)
        summary_linguistic_complexity = generate_complexity_graph(file_name, seq_name_list, linguistic_complexity_list)
        if seq_format != None:
            wrong_seq_graph = generate_wrong_dna_graph(file_name, seq_format, seq_name)
            print('You have wrong DNA characters in ', seq_name, ' detail:', seq_format)        
        summary_kmers = generate_kmers_graph(file_name, seq_name_list, possible_total_list, observed_total_list)           
        print('You have sucessfully generated output files and graphs. Check data_out folder to check kmers and graph_out to check graphs. These two folders are into a folder called "output"') 
        
    else:
        print('The data file should only be in .fasta format')