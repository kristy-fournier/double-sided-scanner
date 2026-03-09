# Double Sided Scanner

Allows creating a complete inorder pdf from 2 "sides" of a physical scanned document

## Basic use instructions

1. Scan the odds (fronts) of your document and put the file in the same directory with the name `odds.pdf`
2. Flip the stack over and scan the evens (backs) in the order they are oriented
    - This means the created scan will be backwards, this will be fixed in the program
3. Put the resulting scan in a file named `evens.pdf`
4. Run the `doubleSidedScanMerger.py` and it will create a `final.pdf` of the combined pages
