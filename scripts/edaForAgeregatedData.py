import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


class eda_for_agg_data:
    def __init__(self):
        pass
    def load_data(self,data):
        self.data = data
        return self.data
    def check_for_missing_values(self):
        missing_values = self.data.isnull().sum()
        return missing_values
    def count_outliers(self):
        Q1 = self.data.quantile(0.25)
        Q3 = self.data.quantile(0.75)
        IQR = Q3 - Q1
        
        # Outlier conditions
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Identify outliers
        outliers = ((self.data < lower_bound) | (self.data > upper_bound)).sum()
        
        return outliers
    def cap_outliers_iqr(self, multiplier=2.0):
        for col in self.data.select_dtypes(include=[np.number]):
            Q1 = self.data[col].quantile(0.25)
            Q3 = self.data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - multiplier * IQR
            upper_bound = Q3 + multiplier * IQR
            self.data[col] = np.clip(self.data[col], lower_bound, upper_bound)
        return self.data
    def simple_Eda(self):
        # Display data types
        print(self.data.dtypes)

        # Summary statistics
        print(self.data.describe())
    def variable_transormation(self):
        self.data['total_data'] = self.data['total_download_data'] + self.data['total_upload_data']
        self.data['decile'] = pd.qcut(self.data['total_session_duration'], 10, labels=False)

        decile_summary = self.data.groupby('decile')['total_data'].sum().reset_index()
        return decile_summary
    def analyze_basic_metrics(self):
        metrics = self.data[['total_session_duration', 'total_download_data', 'total_upload_data']].agg(['mean', 'median', 'std'])
        print(metrics)
    def Non_Graphical_Univariate_Analysis(self):
        dispersion_metrics = self.data.var()
        print(dispersion_metrics)
    def Graphical_Univariate_Analysis(self):
        # Histogram for total session duration
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['total_session_duration'], kde=True)
        plt.title('Histogram of Total Session Duration')
        plt.show()

        # Boxplot for total download data
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.data['total_download_data'])
        plt.title('Boxplot of Total Download Data')
        plt.show()
    def Bivariate_Analysis(self):
        applications = ['Youtube', 'Netflix', 'Gaming', 'Other']
        for app in applications:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=self.data[f'total_data_volume_{app}_DL'], 
                            y=self.data['total_data'])
            plt.title(f'{app} Data vs Total Data')
            plt.xlabel(f'{app} Data')
            plt.ylabel('Total Data (DL + UL)')
            plt.show()
    def Correlation_Analysis(self):
        # Selecting the columns that are relevant for correlation analysis
        correlation_columns = [
            'total_data_volume_Youtube_DL', 'total_data_volume_Youtube_UL',
            'total_data_volume_Netflix_DL', 'total_data_volume_Netflix_UL',
            'total_data_volume_Gaming_DL', 'total_data_volume_Gaming_UL',
            'total_data_volume_Other_DL', 'total_data_volume_Other_UL'
        ]
        
        # Check if all columns are present
        if all(col in self.data.columns for col in correlation_columns):
            correlation_matrix = self.data[correlation_columns].corr()

            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
            plt.title('Correlation Matrix')
            plt.show()
        else:
            missing_cols = [col for col in correlation_columns if col not in self.data.columns]
            print(f"Missing columns: {missing_cols}")

    def Dimensionality_Reduction(self):
        # Select relevant features from your aggregated data
        features = self.data[
            [
                'total_data_volume_Youtube_DL', 'total_data_volume_Youtube_UL',
                'total_data_volume_Netflix_DL', 'total_data_volume_Netflix_UL',
                'total_data_volume_Gaming_DL', 'total_data_volume_Gaming_UL',
                'total_data_volume_Other_DL', 'total_data_volume_Other_UL'
            ]
        ]

        # Standardize the data
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)

        # Apply PCA to reduce dimensions to 2 components
        pca = PCA(n_components=2)
        principal_components = pca.fit_transform(scaled_features)

        # Create a DataFrame with the principal components
        pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

        # Plot the PCA result
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='PC1', y='PC2', data=pca_df)
        plt.title('PCA of Application Data')
        plt.show()

        # Explained variance to understand the importance of the components
        explained_variance = pca.explained_variance_ratio_
        print(f"Explained Variance by Component: {explained_variance}")

        return pca_df
 










