# Python-Assignment
This is working folder for my Python assignment under URI Spring 2018 Bio-539 'Big Data Analysis' class. The task is to count the possible and observed kmers from the file nd2.fasta, compute the linguistic complexity and produce graphs and dataframe for observed vs possible kmers for every sequence of the file. 

I subset the nd2.fasta file and made jeeban.fasta taking only 4 sequences from the original file for handling it easily, but the .py script can handle any .fasta files. 

There were few non-DNA characters (other than ATGC), I have written a code into the main command file (python_script_Jeeban.py) which counts those characters and produce graphs if that is applicable to a sequence.

If you need any information from this project, you can write me at jeeban_panthi@uri.edu

To run the script:
python scrip_name data_file

For my case it is: python python_script_Jeeban.py jeeban.fasta
This works only for the .fasta file. You can change the code to work with other format of data. 

To check the outputs: Go to the output folder, there are two folder into it: one is for the data outputs and the other is for the graphs. 

