from scripts.db_setup import DataLoading
import matplotlib.pyplot as plt
import seaborn as sns


class UserOverview:
    def __init__(self):
        self.main = DataLoading()
    def load_data(self):
        self.data = self.main.data
        return self.data 
    def basic_data(self):
        rows , column = self.data.shape
        columns = self.data.columns
        head = self.data.head()
        print(f"the data have {rows} rows  and {column} columns")
        print(f" the data have this list of columns {columns}")
        print(f"the data looks like this {head}")
    def handset_type_analysis(self):
        number_of_unoque_handset_type = len(self.data['Handset Type'].unique())
        self.top_ten_handset_type = self.data['Handset Type'].value_counts().sort_values(ascending=False).head(10)
        print(f"the telecom company have {number_of_unoque_handset_type} types of unique handset mobile phones")
        print(f"and the top ten handsets are  \n {self.top_ten_handset_type}")
        print(f"And here is the visualization represenation {self.plot_top_ten_handsets()}")
    def plot_top_ten_handsets(self):
        print ("and here is the visual representaion")
        self.top_ten_handset_type.plot(kind='bar',color='skyblue')
        plt.title("Top ten handset chose by the user")
        plt.xlabel('types of handsets(Mobile phones)')
        plt.ylabel('the number of handsets used by our user')
        plt.xticks(rotation=90, ha='right')
        plt.show()
    def handset_manufacturers_anlysis(self):
        number_of_unoque_handset_manufacturers = len(self.data['Handset Manufacturer'].unique())
        self.top3_manufacturers = self.data['Handset Manufacturer'].value_counts().sort_values(ascending=False).head(3)
        print(f"the telecom company have {number_of_unoque_handset_manufacturers} types of unique handset mobile phones")
        print(f"and the top ten handsets are  \n {self.top3_manufacturers}")
        print(f"And here is the visualization represenation {self.plot_top_3_manufacturers()}")
    def plot_top_3_manufacturers(self):
        self.top3_manufacturers.plot(kind='bar' , color='lightgreen')
        plt.xlabel('manufacturer name')
        plt.ylabel('number of handset manufactured by the company')
        plt.title("Top three manufacrurers")
        plt.show()
    def  top_5_handsets_per_top_3_handset_manufacturer(self):
        top3_manufacturers_index = self.data['Handset Manufacturer'].value_counts().sort_values(ascending=False).head(3).index
        top_3_data = self.data[self.data['Handset Manufacturer'].isin(top3_manufacturers_index)]
        handset_type_counts = top_3_data.groupby('Handset Manufacturer')['Handset Type'].value_counts()
        print(f"the nadset tupes and there count on those top 3 manufacturing companies \n {handset_type_counts}")
        handset_type_counts = top_3_data.groupby(['Handset Manufacturer', 'Handset Type']).size()
        self.top_5_handsets_per_manufacturer = (
        handset_type_counts.groupby(level=0, group_keys=False)
        .nlargest(5)
        .reset_index(name='count')
        )
        print("The top 5 handset types and their count for the top 3 manufacturing companies:\n")
        print(self.top_5_handsets_per_manufacturer)
        print("and here is the visual reperesentaion")
        self.plot_top_5_hadsets_in_top_3_manufacturers()
    def plot_top_5_hadsets_in_top_3_manufacturers(self):
        # Step 1: Create a bar plot
        plt.figure(figsize=(12, 8))  # Set the figure size

        sns.barplot(
            x='Handset Type', 
            y='count', 
            hue='Handset Manufacturer', 
            data=self.top_5_handsets_per_manufacturer,
            palette='Set2'
        )

        # Step 2: Enhance the plot
        plt.title('Top 5 Handset Types for the Top 3 Manufacturers', fontsize=16)
        plt.xlabel('Handset Type', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels for better readability
        plt.legend(title='Manufacturer')

        # Display the plot
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()










    