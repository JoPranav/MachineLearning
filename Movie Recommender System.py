# install numpy, scipy, lightfm
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data and format it, store it in a dictionary variable
#and split it into training and testing data
data = fetch_movielens(min_rating = 4.0)
#print training and testing data

print(repr(data['train']))
print(repr(data['test']))
# print gives following result with OpenMP support warning
#<943x1682 sparse matrix of type '<class 'numpy.int32'>'
#	with 49906 stored elements in COOrdinate format>
#<943x1682 sparse matrix of type '<class 'numpy.int32'>'
#	with 5469 stored elements in COOrdinate format>
#create model, use warp as a loss function i.e. weighted approximate-rank pairwise
#warp uses content + collaborative i.e Hybrid approach for rating
#warp uses gradient discent to increse accuracy of predictions over time
model = LightFM(loss='warp')
#train model with 30 epoch iterations 
model.fit(data['train'],epochs=30,num_threads=2)
def sample_recommendation(model,data,user_ids):
    #number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:

        #movies they alrady like in compressed sparsed row format using indices
        #lightfm considers rating 5 as positive and 4 or below as negative
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        #arange method of numpy give numbers from 0 to n_items
        scores = model.predict(user_id,np.arange(n_items))
        #rank them in order of most liked to least in descending order -scores by using argsort
        top_items = data['item_labels'][np.argsort(-scores)]
        #print out the results
        print("User %s"% user_id)
        print("known positives:")
        for X in known_positives[:3]:
            print("         %s" %X)
        print("         Recommended:")
        for Y in  top_items[:3]:
            print("         %s" %Y)
sample_recommendation(model, data, [3, 25, 450])
