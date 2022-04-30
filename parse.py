
from expression_tree_nodes import * 
from typing import List
import copy
# returns an expression
# returns a list of all variables

def find_close_parenthesis(sen, ind_open):
    depth = 1
    i=0
    ind = 0
    while(depth!=0):
        if sen[i] == '(':
            depth +=1
        elif sen[i] == ')':
            depth -=1
            ind = i
        i+=1
    return ind


def parse_parenthesis(sen):
    # if find no more parenthesis (not going to happen)
    ind_open = sen.find('(')

    return 1


def parse(sen, varL:List):
    """ Should return a list of variables(vars) too to feed into map of true and false
        Should return an expression """
    # if there is a parenthesis on the outside, delete it 
    
    if sen.strip()[0] == '(' and sen[len(sen)-1] == ')':
        parse(sen[1:len(sen)-1].strip(), varL)

    # parenthesis > iff > then > and > or > not
    # parenthesis 
    if sen.find('(') != -1:
        
        p_open = sen.find('(')
        
        # if the parenthesis is the first expression
        
        # if the parenthesis is the second expression
    
    # iff 
    elif sen.find('%') != -1:
        ind = sen.find('%')
        sen1 = sen[0:ind]
        exp1 = parse(sen1, varL)
        sen2 = sen[ind+1:]
        exp2 = parse(sen2, varL)
        return IFF(exp1, exp2)
    # if then
    elif sen.find('$') != -1:
        ind = sen.find('$')
        sen1 = sen[0:ind]
        exp1 = parse(sen1, varL)
        sen2 = sen[ind+1:]
        exp2 = parse(sen2, varL)
        return THEN(exp1, exp2)
    # and
    elif sen.find('&'):
        ind = sen.find('&')
        sen1 = sen[0:ind]
        exp1 = parse(sen1, varL)
        sen2 = sen[ind+1:]
        exp2 = parse(sen2, varL)
        return AND(exp1, exp2)
    # or 
    elif sen.strip().find('|'):
        ind = sen.find('|')
        sen1 = sen[0:ind]
        exp1 = parse(sen1, varL)
        sen2 = sen[ind+1:]
        exp2 = parse(sen2, varL)
        return OR(exp1, exp2)
    # not
    elif sen.find('~'):
        sen1 = sen[1:]
        exp1 = parse(sen1, varL)
        return NOT(exp1)
    # return variables
    varL.append(sen.strip())
    return VAR(sen.strip())

def generate_permutations_recurse(pos,curr_pos, curr_list, all_permutations):
    if curr_pos == pos:
        all_permutations.append(curr_list)
        return

    curr_list.append(0)
    new_list = copy.deepcopy(curr_list)
    new_list[-1]=1
    generate_permutations_recurse(pos, curr_pos+1, new_list, all_permutations)
    generate_permutations_recurse(pos, curr_pos+1, curr_list, all_permutations)


# wrapper for generate permutations
def generate_permutations(pos):
    all_permutations = []
    generate_permutations_recurse(pos, 0, list(), all_permutations)
    return all_permutations

# generate a list of dictionaries
def generate_all_combinations(varL:List):
    all_combination = []
    all_perm = generate_permutations(len(varL))
    for one_perm in all_perm:
        one_comb = dict()
        for i in range(len(varL)):
            if one_perm[i] == 1:
                one_comb[varL[i]] = True
            else:
                one_comb[varL[i]] = False
        all_combination.append(one_comb)
    return all_combination

def solve_puzzle(sen_list):
    varList = list()
    expression_list = list()
    

    for sen in sen_list:
        expression_list.append(parse(sen, varList))
    num_expressions = len(expression_list)

    # do multiple expressions
    all_combination = generate_all_combinations(varList)

    # 
    truth_ct = 0
    sol_list = list()

    for comb in all_combination:
        for expression in expression_list:
            if expression.evaluate(comb):
                truth_ct+=1
                if truth_ct == num_expressions:
                    sol_list.append(comb)
        truth_ct = 0      # am I at right level?   
            
    return sol_list

if __name__ == "__main__":
    '''
    exp = parse("A%B")
    v = exp.evaluate({"A": True, "B":True})    
    
    print(v)'''
    
    for each in all:
        print('\n')
        for i in each:
            print(i, end = '')
        
        
        