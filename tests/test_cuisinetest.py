import json
import argparse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.pipeline import Pipeline
import pytest


def test_cuisine_predictor_functionality():
    # prepare test arguments
    test_args = ['--N', '2',  '--ingredient', 'paprika', '--ingredient', 'banana',  '--ingredient', 'rice krispies']
    #Dealing with taking inputs from command line
    parser = argparse.ArgumentParser(description='Cuisine Predictor')
    parser.add_argument('--N', type=int, default=5, help='Number of top-N closest foods to return')
    parser.add_argument('--ingredient', nargs='+', action='append', help='List of ingredients')
    args = parser.parse_args(test_args)

    # LOAD DATA SET
    with open("docs/yummly.json", 'r') as f:
        data = json.load(f)

    #DATASET THAT CONTAINS JUST THE INGREDIENTS FROM THE JSON FILE
    corpus = [' '.join(d['ingredients']) for d in data]

    #THIS IS A LIST OF THE DIFFERENT INPUTTED INGREDIENTS
    new_recipe =[string for sublist in args.ingredient for string in sublist]
    new_recipe_string = ", ".join(new_recipe)

    #COMBINED THE LIST OF INGREDIENTS FROM THE JSON FILE AND THE LIST OF INPUTTED INGREDIENTS
    combined_corpus = corpus + [new_recipe_string]

    #USING TFIDF VECTORIZER FOR VECTORIZATION OF THE DIFFERENT WORDS.
    vectorizer = TfidfVectorizer()
    combined_ingredients_matrix = vectorizer.fit_transform(combined_corpus)

    ingredients_vector = combined_ingredients_matrix[:len(corpus)]
    recipe_vector = combined_ingredients_matrix[-1]

    similarities = cosine_similarity(ingredients_vector, recipe_vector)
    sorted_similarities_index = np.argsort(-similarities[:,0])
    sorted_similarities = similarities[sorted_similarities_index]

    #PROCESS FOR GETTING THE TOP N CUISINE MATCHES.
    top_n_scores = []

    for i in range(args.N + 1):
        similar_scores = sorted_similarities[i]
        similar_scores_string = str(similar_scores)
        next_scores = similar_scores_string[1:-1]
        top_n_scores.append(next_scores)
    cusine_match = data[sorted_similarities_index[0]]['cuisine']

    #FINDING SCORE FOR THE CLOSEST CUISINE
    score_of_match = sorted_similarities[0] #THIS IS THE SCORE OF THE CLOSEST CUISINE FROM THE GIVEN INGREDIENTS.
    score_of_match_string = str(score_of_match) #CONVERT TO STRING
    editted_score_of_match = score_of_match_string[1:-1] #STRING SLICING TO TAKE OUT THE BRACKETS.

    #FORMAT FOR OUTPUT
    solution_format = {
        "cuisine" : cusine_match,
        "score" :   editted_score_of_match,
        "closest" :  [
            {
            }]}

    #ARRANGES THE N CLOSEST FOUND CUISINES
    solution_format["closest"] = [{'id': data[sorted_similarities_index[i]]['id'], 'score': top_n_scores[i]} for i in range(1, args.N + 1)]

    #CHANGE TO JSON FORMAT
    json_data = json.dumps(solution_format, indent=2)
    expected_output = {
    "cuisine": "southern_us",
    "score": "0.42441106",
    "closest": [
        {"id": 9944, "score": '0.40808987'},
        {"id": 49233, "score":'0.39504891'},
    ]
}
    assert json.loads(json_data) == expected_output








