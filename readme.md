# Double Sided Scanner

Allows creating a complete inorder pdf from 2 "sides" of a physical scanned document

## Basic use instructions

*I intend to make this easier sometime soon, but for now the doubleSidedScanMerger can be used as is*

1. Scan the odds (fronts) of your document and put the file in the same directory with the name `odds.pdf`
2. Flip the stack over, then deal the papers down
    - You are flipping the pages while keeping the order, at the end the reverse side of 1 is on top, then reverse of 2 and so on
3. Scan these pages and put the resulting scan named `evens.pdf`
4. Run the `doubleSidedScanMerger.py` and it will create a `final.pdf` of the combined pages
