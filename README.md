# Intermediate-Logic-S22-Project
## Knights and Knaves Puzzle Generator and Solver

### By Ray Shi and Jenny Shen

## What This Is
This project is a Knight and Knave problem solver, 
you can input sentences that are in logic expression form and this 
program will tell you all the combination of which each variable
is a knight or knave.

## How it Works
After all the sentences are added, it is feed into a parser which makes 
the sentences into expression trees, each node being a symbol and the sub-tree. 
(as you can see in the expression_tree_nodes.py)
After expressions are formed, there will be a list generated of all the variables, 
which is feed into the generate_all_combinations list, which generates a list of 
dictionaries with variables as keys and boolean values as values.
Lastly for the set of expressions we evaluate them using each combination, and 
if the combination comes out to true for all expression in that set it expressions
then we know that this is a solution since there are no contradictions. 

## How to Use it 
1. Run parse.py
2. Translate your Knight and Knave into logic sentences
3. When prompted for input, input logic sentences,
for each sentence, when finished input, press enter. 
4. When you want to finish input, type "end" and then enter.
5. It will then ask if you would like to display the tree
for each expression, if you type Y or y, then it will display 
a tree for each sentence, otherwise nothing will change.
6. The solutions will show up! (if there is one)

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

## Writeup and Reflection
This Knights and Knaves Solver is definitely not easy to make. And granted I 
am still not that good with recursion. But through planning together and 
trying to come up with data strctures and details together we learned a lot. 

Some of the hardest parts was to figure out how to structure our data and how 
we would go about solving it. We talked it over and decided on a tree structure,
and each nodes would be the symbol. 

Another thing that was really hard was the parsing of parenthesis, because the 
prioirty would be parenthesis, there has to be a special way to parse them. It 
took me a while to figure all the kinks out, because the way Python works is to 
pass everything by reference, it's sometimes hard to figure out where it went wrong. 
I certainly improved further my debugging skills. 

Overall it was a great project! We had a lot of fun planning and implementing it. 
Even though we know there are definitely features that can be improved like adding 
an interface, and better error handling. (Right now it throws an error if the logic
sentence is entered wrong, but I wish there was a more elegant way to handle it, like
having the user retype)

(And if you would like to see the tree structure, you can uncomment line 206, which
will display the tree structure for the last sentence entered)


