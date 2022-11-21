import ttg

def generate_truth_table_without_expression(prepositions):
    return str(ttg.Truths(bases=prepositions, ints=False)).strip()

def generate_truth_table_with_expressions(prepositions, expressionsSTR):
    expressions = []

    for expression in expressionsSTR.split(','):
        expressions.append(expression.lstrip())

    print(expressions)

    return str(ttg.Truths(bases=prepositions, phrases=expressions, ints=False)).strip()

    

def generate_truth_table(form):
    prepositions = []

    for preposition in form:
        prepositions.append(preposition)

    prepositions.remove('expression')

    if form['expression'] == '':
        return generate_truth_table_without_expression(prepositions)

    return generate_truth_table_with_expressions(prepositions, form['expression'])

    
