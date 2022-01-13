# This project is extracting the keywords from the sentences or from the strings
# This project contains the module named rake-nltk the module extracting the keywords from the sentence
# First user have to install this module from this official site and the project will run otherwise it won't

from rake_nltk import Rake
rake_nltk_var = Rake()

text = """ I am a programmer from India, and I am here to guide you 
with Data Science, Machine Learning, Python, and C++ for free. 
I hope you will learn a lot in your journey towards Coding, 
Machine Learning and Artificial Intelligence with me."""

rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases_with_scores()
print(keyword_extracted)
