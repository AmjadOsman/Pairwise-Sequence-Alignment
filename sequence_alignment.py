from collections import defaultdict
from typing import Sequence # used for extractmatrix


codon_chart={'F':['UUU','UUC'],#Pheylalanine
'L':['UUA','UUG','CUU','CUC','CUA','CUG' ],#Leucine
'I':['AUU','AUC','AUA'],#Isoleucine
'M':['AUG'],#Methionine - start codon
'V':['GUU','GUC','GUA','GUG'],#valine
'S':['UCU','UCC','UCA','UCG','AGU','AGC'],#serine
'P':['CCU','CCC','CCA','CCG'],#proline
'T':['ACU','ACC','ACA','ACG'],#threonine 
'A':['GCU','GCC','GCA','GCG'],#Alanine
'Y':['UAU','UAC'],#Tyrosine
'*':['UAA','UAG','UGA'],#Stop codon
'H':['CAU','CAC',],#Histidine
'Q':['CAA','CAG'],#Glutamine
'N':['AAU','AAC'],#Asparagine
'K':['AAA','AAG'],#Lysine
'D':['GAU','GAC'],#Aspartic acid
'E':['GAU','GAC'],#glutamic acid
'C':['UGU','UGC'],#cysteine
'R':['CGU','CGC','CGA','CGG','AGA','AGG'],#arginine 
'G':['GGU','GGC','GGA','GGA']}#glycine

def printMatrix(matrix):
	
	#function to print the matrix 
	for i in range(len(matrix)):
		print(matrix[i])
	print()

    
def transcription(sequence): # converting Dna to rna 
    rna_seq=sequence.replace('T','U')
    return rna_seq

def translation(rna_strand): # converting rna to protein 
    rna_strand=[rna_strand[i:i+3] for i in range(0,len(rna_strand),3)] 
    protein_seq=''
    for protein in rna_strand:
        for key, value in codon_chart.items():
            if protein in value:
                protein_seq += key 
    return protein_seq

def get_file(): # getting and opening file 
    inp1=input('Enter filename for first sequence:')
    try:
        with open(inp1,'r') as f:
            pass
    except FileNotFoundError:
        print('.txt not valid')
        exit()
    
    inp2=input('Enter filename for second sequence:')
    try:
        with open(inp2,'r') as f:
            pass
    except FileNotFoundError:
        print('.txt not valid')
        exit()



# extracting the sequence 
def extract_seq(file):
    with open(file) as A:
        line= A.readlines()
        lines=line[1].strip()
    return lines 


#making a zero filled matrix based on sequence size 
def matrix(x,y):
    return [[0]*y for i in range(x)]


# extracts the matrix and saves it in a dictionary
def extractmatrix(file):
    matrix=defaultdict(dict)

    with open (file,'r') as f: 
        line= f.readlines()
        nucleotide= line[1].strip().split(',')
        lines=[j.strip().split(',') for j in line] # you took out the [] out of the j 
        lines=lines[2:]
        lines=[[int((x))for x in lst]for lst in lines]

        for dna in nucleotide:
            # print(f'this is dna {dna}')
            for number in lines:

                matrix[dna]=number
                lines.remove(number)
                break
            
        return matrix
                     


    
match_score = 1 
mismatch_score=-1




def global_alignment(x,y,gap):

    n_matrix=matrix(len(x)+1,len(y)+1) 
    main_matrix= matrix(len(x)+1,len(y)+1)
    trace_back=matrix(len(x)+1,len(y)+1)
   

    for i in range(len(x)): # match mismatch matrix 
        for j in range(len(y)):
            if x[i]==y[j]:
                n_matrix[i][j]=match_score
 
            else:
                n_matrix[i][j]=mismatch_score


    for i in range(len(x)+1): # gap score matrix 
        main_matrix[i][0]=gap*i
    for j in range(len(y)+1):
        main_matrix[0][j]=gap*j
    # print(f'main-{main_matrix}')

    for i in range(1,len(x)+1): #finalizing the scoring matrix
        for j in range(1,len(y)+1):
            left=main_matrix[i][j-1]+gap
            up=main_matrix[i-1][j]+gap
            diagonal= main_matrix[i-1][j-1]+n_matrix[i-1][j-1]
            main_matrix[i][j]=max(main_matrix[i-1][j-1]+n_matrix[i-1][j-1],max(main_matrix[i-1][j]+gap,main_matrix[i][j-1]+gap))
            if main_matrix[i][j]==left:
                trace_back[i][j]='left'
            elif main_matrix[i][j]==up:
                trace_back[i][j]='up'
            elif main_matrix[i][j]==diagonal:
                trace_back[i][j]='diag'
    print('Scoring matrix:')
    printMatrix(main_matrix)

    #traceback
    
    align1 =[]
    align2=[]
    i=len(x)    
    j=len(y)  
    while(i > 0 or j > 0):
        if trace_back[i][j] == 'diag':
			# Diag 
            align1.append(x[i-1])
            align2.append(y[j-1])
            i=i-1
            j=j-1
        elif trace_back[i][j] == 'left':
			# Left 
            align1.append('-')
            align2.append(y[j-1])
            j=j-1

        else:
			# Up 
            align1.append(x[i-1])
            align2.append('-')
            i = i-1
			

    print(*align1[::-1])
    print(*align2[::-1])
def semi_global(x,y,gap):
    main_matrix=matrix(len(x)+1,len(y)+1)
    traceback=matrix(len(x)+1,len(y)+1)

    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            # main_matrix[i][j]=np.max(main_matrix[i-1][j-1]+n_matrix[i-1][j-1],max(main_matrix[i-1][j]+gap_score,main_matrix[-1][i-1][j]+terminal_gap),max(main_matrix[i][j-1]+gap_score,main_matrix[:,-1][i][j-1]+terminal_gap))
            matrix1=main_matrix[i-1][j]+gap,main_matrix[i][j-1]+gap,[-1,1][x[i-1]==y[j-1]]
            main_matrix[i][j]=max(matrix1)
            traceback[i][j]=matrix1.index(main_matrix[i][j])
    print(main_matrix)
            

    lastcol= max(range(len(x)+1),key=lambda z: main_matrix[z][len(y)])
    lastrow=max(range(len(y)+1),key=lambda z: main_matrix[len(x)][z])

    if main_matrix[len(x)][lastrow]>=main_matrix[lastcol][len(y)]:
        i=len(x)
        j=lastrow
    else:
        i=lastcol
        j=len(y)

    indel = lambda word, i: word[:i] + '-' + word[i:]

    xalign,yalign=x,y
    
    for n in range(len(x)-i):
        yalign+= '-'
    for n in range(len(y)-j):
        xalign+='-'
    
    while i*j !=0:
        if traceback[i][j]==0:
            i-=1
            yalign=indel(yalign,j)
        elif traceback[i][j]==1:
            j-=1
            xalign=indel(xalign,i)
        else:
            i-=1
            j-=1
    
    for n in range (i):
        yalign=indel(yalign,0)
    for n in range(j):
        xalign=indel(xalign,0)
    
    print(yalign)
    print(xalign)



def local_alignment(x,y,gap):

    l_matrix=matrix(len(x)+1,len(y)+1)
    final_matrix= matrix(len(x)+1,len(y)+1)
   
    best=0
    opt=(0,0)

    for i in range(len(x)): # match mismatch matrix 
        for j in range(len(y)): 
            if x[i]==y[j]:
                l_matrix[i][j]=match_score
            else:
                l_matrix[i][j]=mismatch_score
    

    for i in range(len(x)+1): gap_score matrix 
            final_matrix[i][0]=i*gap
    for j in range(len(y)+1):
        final_matrix[0][j]=j*gap
    

    for inside,outside in enumerate(final_matrix): #coverting negative values to zero
        for inner,outer in enumerate(outside):
            if outer<0:
                final_matrix[inside][inner]=0
    

    for i in range(1,len(x)+1): #forming the scoring matrix 
        for j in range(1,len(y)+1):
            diagonal= final_matrix[i-1][j-1]+l_matrix[i-1][j-1]
            left=final_matrix[i][j-1]+gap
            up=final_matrix[i-1][j]+gap
            final_matrix[i][j]=max(0,diagonal,left,up)
            
            if final_matrix[i][j]>=best: #find higest score
                best= final_matrix[i][j]
                optloc=(i,j) # this find the location of it 
    print('Scoring matrix:')
    printMatrix(final_matrix)

    #traceback
    sequence=''

    i=optloc[0]
    j=optloc[1]

    while (i>0 and j>0):
        diag=final_matrix[i-1][j-1]+l_matrix[i-1][j-1]
        left1= final_matrix[i][j-1]+gap
        up1= final_matrix[i-1][j]+gap

        if min(diag,left1,up1) ==diag:
            break 
        else:
            i-=1
            j-=1
            sequence= sequence +y[j]
    
    print(sequence[::-1])




#driver code
if __name__ == "__main__":
    protein1=''
    protein2= ''
    input2=input('nucleotide or peptide sequence or convert dna to protein? (answer n or p or c ):') 
    sequence1,sequence2=get_file()
    seq1=extract_seq(sequence1)
    seq2=extract_seq(sequence2)
    
    alignType = input("Which alignment would you like to use? Global,or local? (g,l):")
    gap=int(input('Enter gap penalty:'))
    if input2.lower()=='c':
        rna1=transcription(seq1)
        rna2=transcription(seq2)
        protein1=translation(rna1)
        protein2=translation(rna2)
        if alignType.lower()=='g':
            global_alignment(protein1,protein2,gap)
        elif alignType.lower()=='l':
            local_alignment(protein1,protein2,gap)
        elif alignType.lower()=='s':
            semi_global(protein1,protein2,gap)
        else: 
            raise ValueError('Invalid input')
            exit()
    else:
        if alignType.lower()=='g':
            global_alignment(seq1,seq2,gap)
        elif alignType.lower()=='l':
            local_alignment(seq1,seq2,gap)
        elif alignType.lower()=='s':
            semi_global(seq1,seq2,gap)
        else: 
            raise ValueError('Invalid input')


       

