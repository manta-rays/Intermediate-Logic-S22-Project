from expression_tree_nodes import *
from typing import List
import copy

"""
Knights and Knave project, written by Jenny Shen and Ray Shi
Intermediate Logic with Professor Bram, Spring 2022
"""

"""print tree method"""
def print_trees(expression_list, sen_list):
    for i in range(len(sen_list)):
        print(sen_list[i])
        expression_list[i].print_tree()
        print('\n')



"""print out the list of solutions"""
def print_solution(sol_list):
    if len(sol_list) == 0:
        print("Solution doesn't exist")
        return
    print("Solution(s) as follows:")
    for sol in sol_list:
        for name, iden in sol.items():
            if iden:
                print(name, " is a knight")
            else:
                print(name, " is a knave")
        print("\n")


"""given a sentence and an index for open parenthesis, 
returns the index for closing parenthsis """
def find_close_parenthesis(sen, ind_open):
    depth = 1
    i = 0
    ind = 0
    tmp_sen = sen[ind_open + 1:]
    # when depth is 0 that is when you find the closing parenthesis
    # if depth is never 0 then there is a missing parenthesis
    while (depth != 0):
        if (depth != 0 and i == len(tmp_sen) - 1 and tmp_sen[-1] != ')'):
            raise Exception("Missing Parenthesis")
        if tmp_sen[i] == '(':
            depth += 1
        elif tmp_sen[i] == ')':
            depth -= 1
            ind = i + ind_open + 1
        i += 1
    # return ind + ind_open+1
    return ind


"""tells you if there is an open parenthesis in the sentence"""
def parenthesis(sen):
    if sen.find('(') == -1:
        return False
    return True


"""if there are parenthesis, call this function
returns the substring within the parenthesis """
def parse_parenthesis(sen):
    ind_open = sen.find('(')
    ind_close = find_close_parenthesis(sen, ind_open)
    return [sen[ind_open:ind_close + 1], (ind_open, ind_close)]


def parse(sen, varL: List):
    """ Should return a list of variables(vars) too to feed into map of true and false
        Should create an expression tree """
    # strip the sentence of white spaces, also strip everytime I substring
    sen = sen.strip()
    # if there is a big parenthesis on the outside, delete it
    if sen[0] == '(' and find_close_parenthesis(sen, 0) == len(sen) - 1:
        sen = sen[1:len(sen) - 1]

    # parenthesis > iff > then > and > or > not
    # parenthesis 
    if parenthesis(sen):
        sen = sen.strip()
        ret_list = parse_parenthesis(sen)
        ind_open = ret_list[1][0]
        ind_close = ret_list[1][1]
        sen1 = ret_list[0]
        # if sen1 is in the middle then throw an error
        if (ind_open != 0 and ind_close != len(sen) - 1):
            raise Exception("Parsing Wrong, must add parenthesis")
        # determine sentence2 and the symbol, then parse these sentences
        if ind_open == 0:
            sen2 = sen[ind_close + 1:]
            sen2 = sen2.strip()
            # find the symbol
            symb = sen2[0]
            # find sentence 2 
            sen2 = sen2[1:].strip()
        elif ind_close == len(sen) - 1:
            sen2 = sen[0:ind_open]
            sen2 = sen2.strip()
            symb = sen2[-1]
            sen2 = sen2[0:ind_open - 2].strip()
        else:
            raise Exception("Parsing Wrong, must add parenthesis")

        # now that we have sen1, sen2 and symb, check what symb is
        # and summon the correct thing
        if symb == '%':
            exp1 = parse(sen1, varL)
            exp2 = parse(sen2, varL)
            return IFF(exp1, exp2)
        elif symb == ('$'):
            exp1 = parse(sen1, varL)
            exp2 = parse(sen2, varL)
            return THEN(exp1, exp2)
        elif symb == ('&'):
            exp1 = parse(sen1, varL)
            exp2 = parse(sen2, varL)
            return AND(exp1, exp2)
        elif symb == ('|'):
            exp1 = parse(sen1, varL)
            exp2 = parse(sen2, varL)
            return OR(exp1, exp2)
        else:
            raise Exception("wrong symb: ", symb)

    # this is for if there is no parenthesis
    # iff 
    elif sen.find('%') != -1:
        ind = sen.find('%')
        sen1 = sen[0:ind].strip()
        exp1 = parse(sen1, varL)
        sen2 = sen[ind + 1:].strip()
        exp2 = parse(sen2, varL)
        return IFF(exp1, exp2)
    # if then
    elif sen.find('$') != -1:
        ind = sen.find('$')
        sen1 = sen[0:ind].strip()
        exp1 = parse(sen1, varL)
        sen2 = sen[ind + 1:].strip()
        exp2 = parse(sen2, varL)
        return THEN(exp1, exp2)
    # and
    elif sen.find('&') != -1:
        ind = sen.find('&')
        sen1 = sen[0:ind].strip()
        exp1 = parse(sen1, varL)
        sen2 = sen[ind + 1:].strip()
        exp2 = parse(sen2, varL)
        return AND(exp1, exp2)
    # or 
    elif sen.find('|') != -1:
        ind = sen.find('|')
        sen1 = sen[0:ind].strip()
        exp1 = parse(sen1, varL)
        sen2 = sen[ind + 1:].strip()
        exp2 = parse(sen2, varL)
        return OR(exp1, exp2)
    # not
    elif sen.find('~') != -1:
        sen1 = sen[1:].strip()
        exp1 = parse(sen1, varL)
        return NOT(exp1)
    # return variables
    if sen not in varL:
        varL.append(sen)

    return VAR(sen)


"""generate all possible permutations for each variable, 
for example, if there are two variables then the permutations are {00, 01, 10, 11}
"""


def generate_permutations_recurse(pos, curr_pos, curr_list, all_permutations):
    if curr_pos == pos:
        all_permutations.append(curr_list)
        return

    curr_list.append(0)
    new_list = copy.deepcopy(curr_list)
    new_list[-1] = 1
    generate_permutations_recurse(pos, curr_pos + 1, new_list, all_permutations)
    generate_permutations_recurse(pos, curr_pos + 1, curr_list, all_permutations)


"""wrapper for generate permutations"""


def generate_permutations(pos):
    all_permutations = []
    generate_permutations_recurse(pos, 0, list(), all_permutations)
    return all_permutations


"""with the list of all permutations, create a list of dictionaries where each
dictionary has variable names as key and bool value as value to indicate 
that if they're possibly knight or knave"""


def generate_all_combinations(varL: List):
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


"""solve the puzzle, """


def solve_puzzle(sen_list, display_tree = False):
    varList = list()
    expression_list = list()
    # for every sentence in sentence list
    for sen in sen_list:
        expression_list.append(parse(sen, varList))
        # expression_list[-1].print_tree()
    num_expressions = len(expression_list)

    # do multiple expressions
    all_combination = generate_all_combinations(varList)

    # find all combinations where answers to all true
    truth_ct = 0
    sol_list = list()
    for comb in all_combination:
        for expression in expression_list:
            if expression.evaluate(comb):
                truth_ct += 1
                if truth_ct == num_expressions:
                    sol_list.append(comb)
        truth_ct = 0
    if display_tree:
        print_trees(expression_list, sen_list)
    print_solution(sol_list)
    return sol_list


if __name__ == "__main__":

    # prompt input for input of sentence
    sen_list = list()
    sen = ""
    print("Input your sentences: (to finish input type \"end\")")
    while (sen != "end"):
        sen = input()
        sen_list.append(sen)

    # prompt input for if you want to print the trees for each expression
    display_trees = False
    decision = input("Would you like to display the trees for each expression? (Y/N)")
    decision = decision.upper()

    # remove empty items and "end" from the list
    if "" in sen_list:
        while "" in sen_list:
            sen_list.remove("")
    sen_list.remove("end")
    # solve puzzle and print it out
    if decision == 'Y':
        display_trees = True
    solve_puzzle(sen_list, display_trees)
