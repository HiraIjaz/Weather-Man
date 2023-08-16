from datetime import datetime


class WeatherReportGenerator:
    """
    A class for generating weather reports based on calculation results.
    """

    def __init__(self, yearly_results, monthly_results, weather_data):
        """
        Initialize the WeatherReportGenerator.

        :param yearly_results: Yearly calculation results.
        :param monthly_results: Monthly calculation results.
        :param weather_data: Parsed weather data.
        """
        self.yearly_results = yearly_results
        self.monthly_results = monthly_results
        self.weather_data = weather_data

    def generate_monthly_report(self, year, month):
        """
        Generate a monthly weather report for the given year and month.

        :param year: Year for the report.
        :param month: Month for the report.
        :return: Monthly weather report.
        """
        if month in self.monthly_results[year]:
            return {
                'Highest Averag': str(self.monthly_results[year][month]["average highest temp"]) + 'C',
                'Lowest Average': str(self.monthly_results[year][month]["average lowest temp"]) + 'C',
                'Average Mean Humidity': str(self.monthly_results[year][month]["mean humidity"]) + '%'
            }

    def generate_yearly_report(self, year):
        """
        Generate a yearly weather report for the given year.

        :param year: Year for the report.
        :return: Yearly weather report.
        """
        if year in self.yearly_results:
            date_str = self.yearly_results[year]['highest temp day']
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            highest_temp_day = date_obj.strftime('%B %d')

            date_str = self.yearly_results[year]['lowest temp day']
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            lowest_temp_day = date_obj.strftime('%B %d')

            date_str = self.yearly_results[year]['most humid day']
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            most_humid_day = date_obj.strftime('%B %d')

            return {
                'Highest': str(self.yearly_results[year]["highest temp"]) + 'C on ' + highest_temp_day,
                'Lowest': str(self.yearly_results[year]["lowest temp"]) + 'C on ' + lowest_temp_day,
                'Humidity': str(self.yearly_results[year]["humidity"]) + '% on ' + most_humid_day
            }

    def generate_daily_report(self, year, month):
        """
        Generate daily weather report for the given year and month.

        :param year: Year for the report.
        :param month: Month for the report.
        :return: Daily weather report.
        """
        result = {}
        if year in self.weather_data and month in self.weather_data[year]:
            days = self.weather_data[year][month]

            result['title'] = month + ' ' + year
            for day in days:
                date_str = day['PKT']
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                date = date_obj.strftime('%d')
                result[date] = []
                if day['Max TemperatureC']:
                    result[date].append(int((day["Max TemperatureC"])))
                if day['Min TemperatureC']:
                    low_high = ["-" for i in range(0, int(day["Min TemperatureC"]))]
                    result[date].append(int(day["Min TemperatureC"]))
        return result
