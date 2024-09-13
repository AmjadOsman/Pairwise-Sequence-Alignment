

# Bioinformatics Sequence Alignment Tool

This is a Python-based tool for performing various sequence alignment tasks on DNA, RNA, and protein sequences. The tool supports global, local, and semi-global alignments, as well as converting DNA sequences to RNA and protein sequences. It can be used to align nucleotide sequences or peptide sequences and calculate the alignment score based on a user-specified gap penalty.

## Features

- **Global alignment**: Align two sequences from start to end using Needleman-Wunsch algorithm.
- **Local alignment**: Perform local alignment to find the best matching region between two sequences using Smith-Waterman algorithm.
- **Semi-global alignment**: Similar to global alignment, but does not penalize gaps at the start or end of sequences.
- **DNA to RNA transcription**: Converts a DNA sequence to its corresponding RNA sequence.
- **RNA to protein translation**: Converts an RNA sequence to a protein sequence based on the standard genetic code.

## Getting Started

### Prerequisites

Ensure that Python 3.x is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/bioinformatics-alignment-tool.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd bioinformatics-alignment-tool
   ```

3. **Install any required dependencies (if applicable)**. Currently, no external libraries are required, but you can install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Tool

To run the tool, use the following command:

```bash
python main.py
```

You will be prompted to provide several inputs:

1. **Input Type**:
   - `'n'` for nucleotide sequences (DNA/RNA)
   - `'p'` for peptide sequences (protein)
   - `'c'` to convert DNA to protein before aligning

2. **File Names**: Provide the filenames of the sequences you want to align. The files should be in FASTA format, with the sequence starting on the second line.

3. **Gap Penalty**: Input the gap penalty for the alignment algorithm (e.g., `-2`).

4. **Alignment Type**: Choose either `'g'` for global alignment or `'l'` for local alignment.

### Example

If you have two DNA sequences in `sequence1.fasta` and `sequence2.fasta` and want to perform a global alignment with a gap penalty of `-2`, follow these steps:

1. Run the program:
   ```bash
   python main.py
   ```

2. Input the following options:
   ```
   Nucleotide or peptide sequence or convert DNA to protein? (n/p/c): n
   Enter filename for first sequence: sequence1.fasta
   Enter filename for second sequence: sequence2.fasta
   Enter gap penalty: -2
   Which alignment would you like to use? Global or local? (g/l): g
   ```

The program will then output the aligned sequences and the alignment score.

### File Format

The sequence files must be in the FASTA format:

```text
>Sequence description
AGCTAGCTAGCTAGCTA
```

### Codon Table

For RNA-to-protein translation, the tool uses a standard codon table where each codon (set of 3 nucleotides) is translated into a corresponding amino acid.

## Code Structure

- **`main.py`**: The main driver script that handles user input and sequence alignment logic.
- **Functions**:
  - `transcription`: Converts DNA sequences into RNA.
  - `translation`: Converts RNA sequences into protein sequences.
  - `global_alignment`: Performs global alignment using the Needleman-Wunsch algorithm.
  - `local_alignment`: Performs local alignment using the Smith-Waterman algorithm.
  - `semi_global_alignment`: Performs semi-global alignment (implementation is currently pending).
  - `print_matrix`: Prints the alignment matrix for debugging or visual inspection.

## Future Work

- Implement semi-global alignment.
- Add support for scoring matrices such as BLOSUM or PAM for protein alignment.
- Improve performance for large sequences.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Bug reports and feature requests can be submitted via the [issue tracker](https://github.com/your-repo/bioinformatics-alignment-tool/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
