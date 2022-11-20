def get_logical_equivalences_by(expression):
    results = equivalences.get(expression.replace(" ", "").replace("∧", "^"))

    if(results is None):
        results = ["Sem equivalências lógicas por aqui"]

    return results

def get_all():
    return equivalences

equivalences = {
    "p->q": [
        "~p v q",
        "~q -> ~p"
    ],

    "~pvq": [
        "p -> q",
        "~q -> ~p"
    ],

    "~q->~p": [
        "p -> q",
        "~p v q"
    ],

    "~(pvq)": [
        "~p ∧ ~q"
    ],

    "~p^~q": [
        "~ (p v q)"
    ],

    "~(~p)": [
        "p"
    ],

    "p": [
        "~ (~p)"
    ],

    "~(p^q)": [
        "~p v ~q"
    ],

    "~pv~q": [
        "~ (p ∧ q)"
    ],

    "~(p->q)": [
        "p ∧ ~q"
    ],

    "p^~q": [
        "~ (p -> q)"
    ],

    "p<->q": [
        "(p->q) ∧ (q->p)",
        "(~p v q) ∧ (~p v q)"
    ],

    "(p->q)^(q->p)": [
        "p <-> q",
        "(~p v q) ∧ (~p v q)"
    ],

    "(~pvq)^(~pvq)": [
        "p <-> q",
        "(p->q) ∧ (q->p)"
    ]
}