from scripts.db_setup import DataLoading
import missingno as msno
import numpy as np
from sklearn.impute import SimpleImputer
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


class data_cleaning_and_preprocessing:
    def __init__(self):
        main = DataLoading()
        self.data = main.load_data()
    def check_for_missing_values(self):
        missing_values = self.data.isnull().sum()
        missing_values_percentage = (missing_values / len(self.data)) * 100

        missing_data_info = {
            "missing_values": missing_values,
            "missing_values_percentage": missing_values_percentage
        }

        return "missing_data_info"
    def visualize_the_missing_data(self):
        msno.matrix(self.data)
        msno.bar(self.data)
    def fill_the_missing_values(self):
        # for numeric columns let's use the impute numeric columns with median
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        imputer_median = SimpleImputer(strategy='median')
        self.data[numeric_cols] = imputer_median.fit_transform(self.data[numeric_cols])

        # for catacorical column we use the Impute with mode
        catagorical_cols = self.data.select_dtypes(include=[object]).columns
        imputer_mode = SimpleImputer(strategy='most_frequent')
        self.data[catagorical_cols]=imputer_mode.fit_transform(self.data[catagorical_cols])
    def check_for_outliers(self):
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        z_scores = np.abs(stats.zscore(self.data[numeric_cols]))
        # Identify outliers where the z-score is greater than 3 in any column
        outliers = (z_scores > 3).any(axis=1)
        print(f"the outliers are {outliers}")
        print("and here is the visual representaion for some of the columns")
        self.plot_outliers(numeric_cols)
    def plot_outliers(self,numeric_cols):
            # Set up the grid size, e.g., 3 columns per row
        num_cols_per_row = 3
        num_rows = (len(numeric_cols) + num_cols_per_row - 1) // num_cols_per_row  # Ceiling division

        fig, axes = plt.subplots(num_rows, num_cols_per_row, figsize=(15, num_rows * 5))
        axes = axes.flatten()

        for i, col in enumerate(numeric_cols):
            sns.boxplot(x=self.data[col], ax=axes[i])
            axes[i].set_title(f'Boxplot for {col}')

        # Hide any empty subplots if the number of plots is less than num_cols_per_row * num_rows
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()
    def check_for_outliers_iqr_method(self):
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
    
        for col in numeric_cols:
            Q1 = self.data[col].quantile(0.25)
            Q3 = self.data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = self.data[(self.data[col] < lower_bound) | (self.data[col] > upper_bound)]
            if not outliers.empty:
                print(f"Outliers detected in {col}:\n", outliers[col])
            else:
                print(f"No outliers detected in {col} using IQR method.")
    def handle_outliers(self):
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns

        for col in numeric_cols:
            Q1 = self.data[col].quantile(0.25)
            Q3 = self.data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            self.data[col] = np.where(self.data[col] > upper_bound, upper_bound,
                                    np.where(self.data[col] < lower_bound, lower_bound, self.data[col]))

        self.normalize_the_data(numeric_cols)
    def normalize_the_data(self, numeric_cols):
        for col in numeric_cols:
            self.data[f'log_{col}'] = np.log(self.data[col] + 1)



