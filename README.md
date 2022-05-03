# Intermediate-Logic-S22-Project
## Knights and Knaves Puzzle Generator and Solver

### By Ray Shi and Jenny Shen

## What This Is

This project is a Knight and Knave problem solver, 
you can input sentences that are in logic expression form and this 
program will tell you all the combination of which each variable
is a knight or knave.

## How to Use it 

1. Run parse.py
2. Translate your Knight and Knave into logic sentences
3. When prompted for input, input logic sentences,
for each sentence, when finished input, press enter. 
4. When you want to finish input, type "end" and then enter
5. The solutions will show up (if there is one)

## Example Input:
### Problem: 
"Alice says that Rex is a knave. Rex says that it's false 
that Bob is a knave, Bob says I am a knight or Alice is a knight."

### Translated Input: 
Alice % ~Rex

Rex % ~~Bob 

Bob % (Bob | Alice) 

end

### Output:
Alice  is a knave

Rex  is a knight

Bob  is a knight

## Input & Symbol Guide

### Symbol &  Meaning Table

-------------------
	~	|	not
	&	|	and
	|	|	or
	%	|	iff
	$	|	implies






