import pandas as pd
from fuzzywuzzy import fuzz

#clust is the dictionary use for the clustering of similar data into one
clust = {'ln':[],'dob':[],'gn':[],'fn':[]}

#fit function takes all the dataset and analyse it and then merge the data then it findes similar,
#it finally returns a dictionary of different objects
#data argument is the DataFrame or dictionary object
# ratio tells how much strict you want your algorithm should be higher ratio means higher strictness while comparing for similar data
def fit(data, ratio):
    for i in range(len(data)):
        flag = True
        for j in range(len(clust['dob'])):
            if(clust['dob'][j] == data['dob'][i] and clust['gn'][j] == data['gn'][i]):
                if(fuzz.ratio(clust['ln'][j], data['ln'][i]) > ratio and
                   fuzz.ratio(clust['fn'][j], data['fn'][i]) > ratio):
                    flag = False
                    break
        if(flag):
            clust['ln'].append(data['ln'][i])
            clust['fn'].append(data['fn'][i])
            clust['gn'].append(data['gn'][i])
            clust['dob'].append(data['dob'][i])
    return clust

#this function predicts the data, and returns most similar data from the clust dictionary
def predict(data):
    max_ratio = 0
    prediction = {'ln':[],'dob':[],'gn':[],'fn':[]}
    for i in range(len(clust['dob'])):
        fn_ratio = fuzz.ratio(clust['fn'][i], data['fn'])
        dob_ratio = fuzz.ratio(clust['dob'][i], data['dob'])
        gn_ratio = fuzz.ratio(clust['gn'][i], data['gn'])
        ln_ratio = fuzz.ratio(clust['ln'][i], data['ln'])
        data_ratio = (fn_ratio + dob_ratio + gn_ratio + ln_ratio) / 4
        if(max_ratio < data_ratio):
            prediction = [clust['ln'][i], clust['dob'][i], clust['gn'][i], clust['fn'][i]]
            max_ratio = data_ratio
    return prediction
                   

#reades the csv file provided
df = pd.read_csv('Deduplication Problem - Sample Dataset1.csv')


cluster = fit(df, 75)
#generates a csv file from output provided by fit function
output_df = pd.DataFrame(cluster, columns = ['ln', 'dob', 'gn', 'fn'])
output_df.to_csv('output.csv', encoding='utf-8', index=False)
print(output_df)

predict_df = pd.DataFrame(columns = ['ln', 'dob', 'gn', 'fn'])
#predicts the names for input data
predict_df = predict_df.append(pd.Series(predict({'ln':['FUNARO'],'dob':['06/12/1937'],'gn':['F'],'fn':['HARRIET']}),
                                         index=['ln', 'dob', 'gn', 'fn']), ignore_index=True)
predict_df = predict_df.append(pd.Series(predict({'ln':[' Frometa G'],'dob':['06/12/1937'],'gn':['M'],'fn':['Vladimir']}),
                                         index=['ln', 'dob', 'gn', 'fn']), ignore_index=True)
predict_df = predict_df.append(pd.Series(predict({'ln':['Frometa Garo'],'dob':['06/12/1937'],'gn':['M'],'fn':['Vladimir A']}),
                                         index=['ln', 'dob', 'gn', 'fn']), ignore_index=True)
predict_df = predict_df.append(pd.Series(predict({'ln':['Frometa'],'dob':['06/12/1937'],'gn':['M'],'fn':['Vladimir']}),
                                         index=['ln', 'dob', 'gn', 'fn']), ignore_index=True)
#Generates a csv file named 'prediction.csv' for the prediction it made
output_df.to_csv('predictions.csv', encoding='utf-8', index=False)
print("\n\nPredictions: \n", predict_df.head())
