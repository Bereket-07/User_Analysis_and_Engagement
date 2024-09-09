import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

class UserSatisfaction:
    def __init__(self,customer_engagement,customer_experience):
        self.customer_engagement = customer_engagement
        self.customer_experience = customer_experience
    def calculate_engagemnt_score(self):
        #  identify the least engaged cluster  cluster 0
        least_engaged_cluster = self.customer_engagement[self.customer_engagement['cluster'] == 0]
        least_engaged_centroid = least_engaged_cluster[['Session Frequency','Session Duration','Total Traffic']].mean()

        # calculate Euclidean distance for each user
        self.customer_engagement['engagement_score'] = np.linalg.norm(
            self.customer_engagement[['Session Frequency','Session Duration','Total Traffic']] - least_engaged_centroid,
            axis=1
        )

        return self.customer_engagement[['MSISDN/Number', 'engagement_score']]
    def calculate_experiance_score(self):
        # Identify the worst experience cluster cluster 0
        worst_experience_cluster = self.customer_experience[self.customer_experience['Cluster'] == 0]
        worst_experience_centroid = worst_experience_cluster[['Average TCP Retransmission','Average RTT','Average Throughput']].mean()

        # calculate Eucliden diatance for each user
        self.customer_experience['experience_score'] = np.linalg.norm(
            self.customer_experience[['Average TCP Retransmission','Average RTT','Average Throughput']] - worst_experience_centroid,
            axis=1
        )
        return self.customer_experience[['MSISDN/Number', 'experience_score']]
    def calculate_satisfaction_score(self):
        # merge the scores 
        self.combined_scores = pd.merge(self.customer_engagement[['MSISDN/Number', 'engagement_score']],
                                  self.customer_experience[['MSISDN/Number', 'experience_score']],
                                  on='MSISDN/Number')
        # calculate satisfaction score 
        self.combined_scores['satisfaction_score'] = self.combined_scores[['engagement_score', 'experience_score']].mean(axis=1)

        # Return top 10 satisfied customers
        top_10_satisfied = self.combined_scores.nlargest(10,'satisfaction_score')
        return top_10_satisfied
    def predict_satisfaction(self):
        X = self.combined_scores[['engagement_score','experience_score']]
        y = self.combined_scores['satisfaction_score']
        
        #  split the data into train and test sets
        x_train,x_test,y_train,y_test = train_test_split(X, y, test_size=0.3,random_state=42)

        #  Initialize the model
        model = LinearRegression()

        # Train the model 
        model.fit(x_train,y_train)

        # predict on test set 
        y_pred = model.predict(x_test)

        # Evaluate the model 
        mse = mean_squared_error(y_test,y_pred)
        print(f'mean squared Error: {mse}')

        return model
    def k_means_clustering_on_scores(self):
        Kmeans = KMeans(n_clusters=2,random_state=42)
        self.combined_scores['satisfaction_cluster'] = Kmeans.fit_predict(
            self.combined_scores[['engagement_score','experience_score']]
        )
        
        return self.combined_scores[['MSISDN/Number','satisfaction_cluster']]
    def aggergate_scores_per_cluster(self):
        cluster_aggergation = self.combined_scores.groupby('satisfaction_cluster').agg({
            'engagement_score': ['mean'],
            'experience_score': ['mean'],
            'satisfaction_score': ['mean']
        }).reset_index()
        return cluster_aggergation
    
