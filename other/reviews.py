reviews = {"India Palace": ["Delicious food", "Noisy ambiance"],
           "Tasty Korean": ["OK meal", "Best meal ever!"], 
           "Picha": ["Authentic flavors"]
          }

output = []

# Preprocessing - inverted index (go through and get restaurants for all tokens)


# O(n^2)
def search(reviews, key):
    for restaurant in reviews.keys():
        for review in reviews[restaurant]:
            if key in review.split():
                output.append(restaurant)

# O(n)
# Set for every restaurant


# O(k) 
# inverted index

search(reviews, 'food')

print(output)

'''
Reviewer

Test as you go

Extensions
- case sensitive
- multiple search terms
- weighting
'''
