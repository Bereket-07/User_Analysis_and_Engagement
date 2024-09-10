from scripts import DataLoading
from sklearn.impute import SimpleImputer
import numpy as np
import missingno as msno
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')

DATABASE_URL= f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class userExperiance:
    def __init__(self) -> None:
        pass
    def load_data(self):
        main = DataLoading()
        self.data = main.load_data()
        return self.data
    def agg_by_user(self):
        # Calculate averages
        self.data['Average TCP Retransmission'] = (self.data['TCP DL Retrans. Vol (Bytes)'] + self.data['TCP UL Retrans. Vol (Bytes)']) / 2
        self.data['Average RTT'] = (self.data['Avg RTT DL (ms)'] + self.data['Avg RTT UL (ms)']) / 2
        self.data['Average Throughput'] = (self.data['Avg Bearer TP DL (kbps)'] + self.data['Avg Bearer TP UL (kbps)']) / 2

  

        self.user_experiance = self.data.groupby('MSISDN/Number').agg({
            'Average TCP Retransmission':'mean',
            'Average RTT':'mean',
            'Handset Type': 'first',
            'Average Throughput':'mean'
        
        }).reset_index()
        return self.user_experiance
    def check_for_missing_values(self):
        missing_values = self.user_experiance.isnull().sum()
        missing_values_percentage = (missing_values / len(self.data)) * 100

        print(" Missing values count:\n",missing_values)
        print("missing values Percentage:\n",missing_values_percentage)
        print("And here is the visual representation")
        self.visualize_the_missing_data()
    def visualize_the_missing_data(self):
        msno.matrix(self.user_experiance)
        msno.bar(self.user_experiance)
    def remove_missing_values(self):
        numeric_cols = self.user_experiance.select_dtypes(include=[np.number]).columns
        imputer_mean = SimpleImputer(strategy='mean')
        self.user_experiance[numeric_cols] = imputer_mean.fit_transform(self.user_experiance[numeric_cols])
        # for catacorical column we use the Impute with mode
        catagorical_cols = self.user_experiance.select_dtypes(include=[object]).columns
        imputer_mode = SimpleImputer(strategy='most_frequent')
        self.user_experiance[catagorical_cols]=imputer_mode.fit_transform(self.user_experiance[catagorical_cols])
    def check_for_outliers_iqr_method(self):
        numeric_cols = self.user_experiance.select_dtypes(include=[np.number]).columns
    
        for col in numeric_cols:
            Q1 = self.user_experiance[col].quantile(0.25)
            Q3 = self.user_experiance[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = self.user_experiance[(self.user_experiance[col] < lower_bound) | (self.user_experiance[col] > upper_bound)]
            if not outliers.empty:
                print(f"Outliers detected in {col}:\n", outliers[col])
            else:
                print(f"No outliers detected in {col} using IQR method.")
    def handle_outliers(self):
        numeric_cols = self.user_experiance.select_dtypes(include=[np.number]).columns

        for col in numeric_cols:
            Q1 = self.user_experiance[col].quantile(0.25)
            Q3 = self.user_experiance[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            self.user_experiance[col] = np.where(self.user_experiance[col] > upper_bound, upper_bound,
                                    np.where(self.user_experiance[col] < lower_bound, lower_bound, self.user_experiance[col]))
    def compute_list_of_ten(self):
        # Assuming the dataset is already loaded into a DataFrame named df

        # Compute top 10 values
        top_10_tcp = self.user_experiance['Average TCP Retransmission'].sort_values(ascending=False).head(10)
        top_10_rtt = self.user_experiance['Average RTT'].sort_values(ascending=False).head(10)
        top_10_throughput = self.user_experiance['Average Throughput'].sort_values(ascending=False).head(10)

        # Compute bottom 10 values
        bottom_10_tcp = self.user_experiance['Average TCP Retransmission'].sort_values(ascending=True).head(10)
        bottom_10_rtt = self.user_experiance['Average RTT'].sort_values(ascending=True).head(10)
        bottom_10_throughput = self.user_experiance['Average Throughput'].sort_values(ascending=True).head(10)

        # Compute most frequent 10 values
        most_freq_tcp = self.user_experiance['Average TCP Retransmission'].value_counts().head(10)
        most_freq_rtt = self.user_experiance['Average RTT'].value_counts().head(10)
        most_freq_throughput = self.user_experiance['Average Throughput'].value_counts().head(10)

        # Display the results
        print("Top 10 TCP Values:\n", top_10_tcp)
        print("Bottom 10 TCP Values:\n", bottom_10_tcp)
        print("Most Frequent TCP Values:\n", most_freq_tcp)

        print("\nTop 10 RTT Values:\n", top_10_rtt)
        print("Bottom 10 RTT Values:\n", bottom_10_rtt)
        print("Most Frequent RTT Values:\n", most_freq_rtt)

        print("\nTop 10 Throughput Values:\n", top_10_throughput)
        print("Bottom 10 Throughput Values:\n", bottom_10_throughput)
        print("Most Frequent Throughput Values:\n", most_freq_throughput)

        # Create subplots
        fig, axes = plt.subplots(3, 3, figsize=(18, 15))

        # Top 10 TCP
        sns.barplot(x=top_10_tcp.values, y=top_10_tcp.index, ax=axes[0, 0], palette="viridis")
        axes[0, 0].set_title('Top 10 TCP Retransmission Values')
        axes[0, 0].set_xlabel('Average TCP Retransmission')

        # Bottom 10 TCP
        sns.barplot(x=bottom_10_tcp.values, y=bottom_10_tcp.index, ax=axes[0, 1], palette="viridis")
        axes[0, 1].set_title('Bottom 10 TCP Retransmission Values')
        axes[0, 1].set_xlabel('Average TCP Retransmission')

        # Most Frequent TCP
        sns.barplot(x=most_freq_tcp.values, y=most_freq_tcp.index, ax=axes[0, 2], palette="viridis")
        axes[0, 2].set_title('Most Frequent TCP Retransmission Values')
        axes[0, 2].set_xlabel('Frequency')

        # Top 10 RTT
        sns.barplot(x=top_10_rtt.values, y=top_10_rtt.index, ax=axes[1, 0], palette="magma")
        axes[1, 0].set_title('Top 10 RTT Values')
        axes[1, 0].set_xlabel('Average RTT')

        # Bottom 10 RTT
        sns.barplot(x=bottom_10_rtt.values, y=bottom_10_rtt.index, ax=axes[1, 1], palette="magma")
        axes[1, 1].set_title('Bottom 10 RTT Values')
        axes[1, 1].set_xlabel('Average RTT')

        # Most Frequent RTT
        sns.barplot(x=most_freq_rtt.values, y=most_freq_rtt.index, ax=axes[1, 2], palette="magma")
        axes[1, 2].set_title('Most Frequent RTT Values')
        axes[1, 2].set_xlabel('Frequency')

        # Top 10 Throughput
        sns.barplot(x=top_10_throughput.values, y=top_10_throughput.index, ax=axes[2, 0], palette="coolwarm")
        axes[2, 0].set_title('Top 10 Throughput Values')
        axes[2, 0].set_xlabel('Average Throughput')

        # Bottom 10 Throughput
        sns.barplot(x=bottom_10_throughput.values, y=bottom_10_throughput.index, ax=axes[2, 1], palette="coolwarm")
        axes[2, 1].set_title('Bottom 10 Throughput Values')
        axes[2, 1].set_xlabel('Average Throughput')

        # Most Frequent Throughput
        sns.barplot(x=most_freq_throughput.values, y=most_freq_throughput.index, ax=axes[2, 2], palette="coolwarm")
        axes[2, 2].set_title('Most Frequent Throughput Values')
        axes[2, 2].set_xlabel('Frequency')

        plt.tight_layout()
        plt.show()
    def Average_Throughput_per_Handset_Type(self):
        throughput_per_handset = self.user_experiance.groupby('Handset Type')['Average Throughput'].mean().reset_index()
        print(throughput_per_handset)

        # let's visualize
        plt.figure(figsize=(14,7))
        sns.histplot(data=throughput_per_handset,x='Average Throughput',kde=True,bins=30)
        plt.title('Distribution of average Throughput per Handset Type')
        plt.xlabel('Average Throughput (kbps)')
        plt.ylabel('Frequency')
        plt.show()
    def tcp_per_handset(self):
        tcp_per_handset = self.user_experiance.groupby('Handset Type')['Average TCP Retransmission'].mean().reset_index()
        print(tcp_per_handset)

        plt.figure(figsize=(14,7))
        sns.histplot(data=tcp_per_handset,x='Average TCP Retransmission' , kde=True,bins=30)
        plt.title('Distribution of average Throughput per Handset Type')
        plt.xlabel('Average TCP Retransmission')
        plt.ylabel('Frequency')
        plt.show()
    def compute_report(self):
        experience_metrics = self.user_experiance[['Average TCP Retransmission', 'Average RTT', 'Average Throughput']]

        # Standardize the data
        scaler = StandardScaler()
        scaled_metrics = scaler.fit_transform(experience_metrics)

        # Perform k-means clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        self.user_experiance['Cluster'] = kmeans.fit_predict(scaled_metrics)

        # Analyze and describe clusters
        centroids = kmeans.cluster_centers_
        print("Cluster centroids:\n", centroids)

        # Visualize the clusters
        sns.pairplot(self.user_experiance, hue='Cluster', vars=['Average TCP Retransmission', 'Average RTT', 'Average Throughput'])
        plt.show()
        return self.user_experiance
    def save_to_database(self, table_name='self.user_experiance_clusters'):
        engine = create_engine(DATABASE_URL)
        try:
            with engine.connect() as connection:
                self.user_experiance.to_sql(table_name, connection, if_exists='replace', index=False)
                print(f"Data saved successfully to table '{table_name}'.")
        except Exception as e:
            print(f"An error occurred while saving to database: {e}")






