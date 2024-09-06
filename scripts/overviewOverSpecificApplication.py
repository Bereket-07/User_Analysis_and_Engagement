

class overviewoversomeapplication:
    def __init__(self,data):
        self.data = data
    def aggregatingg_and_countint(self,application):
        user_behavior = self.data.groupby('Bearer Id').agg(
            number_of_xdr_sessions=('Bearer Id','count'), # count of xDR sessions
            total_session_duration=('Dur. (ms)','sum'), # sum of session durations in milliseconds
            total_download_data = ('log_Total DL (Bytes)','sum'), # sum of total download data
            total_upload_data = ('log_Total UL (Bytes)','sum'), # sumof total upoad data
        )

        # calculate the total data volumne for each application
       

        for app in application:
            dl_col = f'log_{app} DL (Bytes)'
            ul_col = f'log_{app} UL (Bytes)'

            user_behavior[f'total_data_volume_{app}_DL'] = self.data.groupby('Bearer Id')[dl_col].sum()
            user_behavior[f'total_data_volume_{app}_UL'] = self.data.groupby('Bearer Id')[ul_col].sum()

        return user_behavior
    def check_for_missing_value(self):
        user_behavior = self.aggregatingg_and_countint()
        return user_behavior.isnull().sum()
    