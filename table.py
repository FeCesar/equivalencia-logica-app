import ttg
import dataframe_image as dfi

def generate_truth_table_without_expression(prepositions):
    df = ttg.Truths(bases=prepositions, ints=False).as_pandas()
    dfi.export(df, "./static/images/figure.png")

def generate_truth_table_with_expressions(prepositions, expressionsSTR):
    expressions = []

    for expression in expressionsSTR.split(','):
        expressions.append(expression.lstrip())

    df = ttg.Truths(bases=prepositions, phrases=expressions, ints=False).as_pandas()
    dfi.export(df, "./static/images/figure.png")


def generate_truth_table(form):
    prepositions = []

    for preposition in form:
        prepositions.append(preposition)

    prepositions.remove('expression')

    if form['expression'] == '':
        generate_truth_table_without_expression(prepositions)
    
    else:
        generate_truth_table_with_expressions(prepositions, form['expression'])

    
