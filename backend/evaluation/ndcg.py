import math

def dcg(relevances, k=10):

    relevances = relevances[:k]

    score = 0

    for i, rel in enumerate(relevances):

        score += rel / math.log2(i + 2)

    return score

def ndcg_at_k(true_relevances, predicted_relevances, k=10):

    ideal = sorted(
        true_relevances,
        reverse=True
    )

    ideal_dcg = dcg(ideal, k)

    if ideal_dcg == 0:
        return 0

    predicted_dcg = dcg(
        predicted_relevances,
        k
    )

    return predicted_dcg / ideal_dcg