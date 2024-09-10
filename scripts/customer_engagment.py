from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scripts import DataLoading
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')

DATABASE_URL= f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class CustomerEngagement:
    def __init__(self):
        pass

    def load_data(self):
        main = DataLoading()
        self.data = main.load_data()
        return self.data

    def aggregate_per_customer(self):
        self.customer_engagement = self.data.groupby('MSISDN/Number').agg({
            'Youtube DL (Bytes)': 'sum',
            'Youtube UL (Bytes)': 'sum',
            'Netflix DL (Bytes)': 'sum',
            'Netflix UL (Bytes)': 'sum',
            'Gaming DL (Bytes)': 'sum',
            'Gaming UL (Bytes)': 'sum',
            'Other DL (Bytes)': 'sum',
            'Other UL (Bytes)': 'sum',
            'Dur. (ms)': 'sum',   # Assuming session duration is in milliseconds
            'Bearer Id': 'count'  # Assuming each 'Bearer Id' represents a session
        }).reset_index()

        # Calculate total traffic per application
        self.customer_engagement['Total Youtube Traffic'] = self.customer_engagement['Youtube DL (Bytes)'] + self.customer_engagement['Youtube UL (Bytes)']
        self.customer_engagement['Total Netflix Traffic'] = self.customer_engagement['Netflix DL (Bytes)'] + self.customer_engagement['Netflix UL (Bytes)']
        self.customer_engagement['Total Gaming Traffic'] = self.customer_engagement['Gaming DL (Bytes)'] + self.customer_engagement['Gaming UL (Bytes)']
        self.customer_engagement['Total Other Traffic'] = self.customer_engagement['Other DL (Bytes)'] + self.customer_engagement['Other UL (Bytes)']

        # Calculate overall metrics
        self.customer_engagement['Total Traffic'] = (
            self.customer_engagement['Total Youtube Traffic'] +
            self.customer_engagement['Total Netflix Traffic'] +
            self.customer_engagement['Total Gaming Traffic'] +
            self.customer_engagement['Total Other Traffic']
        )
        self.customer_engagement['Session Frequency'] = self.customer_engagement['Bearer Id']
        self.customer_engagement['Session Duration'] = self.customer_engagement['Dur. (ms)'] / 1000  # Convert to seconds

        return self.customer_engagement

    def identify_top_ten_customers_per_metric(self):
        top_10_youtube = self.customer_engagement.nlargest(10, 'Total Youtube Traffic')
        top_10_netflix = self.customer_engagement.nlargest(10, 'Total Netflix Traffic')
        top_10_gaming = self.customer_engagement.nlargest(10, 'Total Gaming Traffic')
        top_10_other = self.customer_engagement.nlargest(10, 'Total Other Traffic')

        return {
            'Top 10 Youtube Users': top_10_youtube[['MSISDN/Number', 'Total Youtube Traffic']],
            'Top 10 Netflix Users': top_10_netflix[['MSISDN/Number', 'Total Netflix Traffic']],
            'Top 10 Gaming Users': top_10_gaming[['MSISDN/Number', 'Total Gaming Traffic']],
            'Top 10 Other Users': top_10_other[['MSISDN/Number', 'Total Other Traffic']]
        }

    def normalize_the_engagement_metrics(self):
        # initializing the scaler
        scaler = MinMaxScaler()

        # normalize the engagement metrics
        normalized_metrics = scaler.fit_transform(
            self.customer_engagement[['Session Frequency', 'Session Duration', 'Total Traffic']]
        )

        # convert to a DataFrame
        self.normalized_df = pd.DataFrame(
            normalized_metrics,
            columns=['Session Frequency', 'Session Duration', 'Total Traffic']
        )

        return self.normalized_df

    def k_means_clustering(self, k=3):
        # Initialize k-means with specified clusters
        kmeans = KMeans(n_clusters=k, random_state=42)

        # fit the model and predict the clusters
        self.normalized_df['cluster'] = kmeans.fit_predict(self.normalized_df)

        # Add the cluster labels back to the original customer engagement DataFrame
        self.customer_engagement['cluster'] = self.normalized_df['cluster']

        return self.customer_engagement
    def save_to_database(self, table_name='customer_engagement_clusters'):
        try:
            # Create the engine using SQLAlchemy
            engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/telecom_db')
            
            # Save the DataFrame to a SQL table using the engine
            self.customer_engagement.to_sql(table_name, con=engine, if_exists='replace', index=False)
            
            print(f"Data saved successfully to table '{table_name}'.")
        except Exception as e:
            print(f"An error occurred while saving to database: {e}")

    def analyze_clusters(self):
        cluster_analysis = self.customer_engagement.groupby('cluster').agg({
            'Session Frequency': ['min', 'max', 'mean', 'sum'], 
            'Session Duration': ['min', 'max', 'mean', 'sum'],
            'Total Traffic': ['min', 'max', 'mean', 'sum']
        }).reset_index()

        return cluster_analysis

    def plot_elbow_method(self):
        wcss = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, random_state=42)
            kmeans.fit(self.normalized_df)
            wcss.append(kmeans.inertia_)

        # Plot the elbow method graph
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, 11), wcss, marker='o')
        plt.title('Elbow Method')
        plt.xlabel('Number of clusters')
        plt.ylabel('WCSS')
        plt.show()

    def aggregate_user_traffic_per_application(self):
        application_columns = [
            'Total Youtube Traffic', 'Total Netflix Traffic',
            'Total Gaming Traffic', 'Total Other Traffic'
        ]
        
        top_10_users_per_application = {}
        for app in application_columns:
            top_10_users = self.customer_engagement.nlargest(10, app)
            top_10_users_per_application[app] = top_10_users[['MSISDN/Number', app]]

        return top_10_users_per_application

    def plot_top_3_applications(self):
        # Aggregate total traffic for each application
        app_traffic = self.customer_engagement[
            ['Total Youtube Traffic', 'Total Netflix Traffic', 'Total Gaming Traffic', 'Total Other Traffic']
        ].sum()

        # Get the top 3 applications based on traffic
        top_3_apps = app_traffic.nlargest(3)

        # Plotting
        plt.figure(figsize=(10, 6))
        top_3_apps.plot(kind='bar', color=['blue', 'red', 'green'])
        plt.title('Top 3 Most Used Applications by Total Traffic')
        plt.xlabel('Application')
        plt.ylabel('Total Traffic (Bytes)')
        plt.show()
