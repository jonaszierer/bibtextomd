BibTeX to markdown formatter
---

This python script takes a BibTeX bibliography file and converts the 
entries to the format used by my website, [bryanwweber.com](http://bryanwweber.com).
The BibTeX file for testing was generated by export from Mendeley, 
although Mendeley is fairly standards conforming, so most standard
BibTeX files should work as well. bibtextomd is Python 3 ONLY!

Usage
---

From the command line,

    py bib.py [options]

runs the script. Running with no options specified prints the help. 
The default file names for the BibTeX input and 
markdown output are `refs.bib` and `pubs.md` respectively. 

Options
---

    -h, --help: Print the help and exit
    
    -o filename, --output=filename: Set the filename of the markdown output. Default: pubs.md
    
    -b filename, --bibfile=filename: Set the filename of the BibTeX input. Default: refs.bib
    
    -a 'author', --author='f.a. name': Set the name of the author to be highlighted. Default: 
    "F.A. Author". Name should be specifed between double quotes: "F.A. Author"