from model import weather_data_parser, weather_report_generator


class WeatherDataAnalyzer:
    """
    A class for analyzing weather data.
    """

    def __init__(self, weatherdata):
        """
        Initialize the WeatherDataAnalyzer.

        :param weatherdata: Weather data to be analyzed.
        """
        self.weather_data = weatherdata
        self.yearly_calculations = {}
        self.monthly_calculations = {}

    def comp_yearly_calculations(self):
        """
        Compute yearly weather calculations.
        """
        for year, months in self.weather_data.items():
            highest_temp = float('-inf')
            highest_temp_day = ''
            lowest_temp = float('inf')
            lowest_temp_day = ''
            highest_humidity = 0
            most_humid_day = ''

            for month, days in months.items():
                for day in days:
                    if day['Max TemperatureC'] and float(day['Max TemperatureC']) > highest_temp:
                        highest_temp = float(day['Max TemperatureC'])
                        highest_temp_day = day.get('PKT')

                    if day['Min TemperatureC'] and float(day['Min TemperatureC']) < lowest_temp:
                        lowest_temp = float(day['Min TemperatureC'])
                        lowest_temp_day = day.get('PKT')

                    if day['Max Humidity'] and int(day['Max Humidity']) > highest_humidity:
                        highest_humidity = int(day['Max Humidity'])
                        most_humid_day = day.get('PKT')

            self.add_yearly_result(year, highest_temp, highest_temp_day, lowest_temp, lowest_temp_day, most_humid_day,
                                   highest_humidity)

    def comp_calculations_monthly(self):
        """
        Compute monthly weather calculations.
        """
        for year, months in self.weather_data.items():
            for month, days in months.items():
                total_highest_temp = 0
                total_lowest_temp = 0
                total_mean_humidity = 0
                total_days = len(days)
                for day in days:
                    if day['Max TemperatureC']:
                        total_highest_temp += float(day['Max TemperatureC'])
                    if day['Min TemperatureC']:
                        total_lowest_temp += float(day['Min TemperatureC'])
                    if day['Mean Humidity']:
                        total_mean_humidity += float(day['Mean Humidity'])

                avg_highest_temp = float(total_highest_temp / total_days)
                avg_lowest_temp = float(total_lowest_temp / total_days)
                mean_humidity = float(total_mean_humidity / total_days)

                self.add_monthly_result(year, month, avg_highest_temp, avg_lowest_temp, mean_humidity)

    def add_monthly_result(self, year, month, avg_highest_temp, avg_lowest_temp, mean_humidity):
        """
        Add monthly weather calculation results.

        :param year: Year of the data.
        :param month: Month of the data.
        :param avg_highest_temp: Average highest temperature.
        :param avg_lowest_temp: Average lowest temperature.
        :param mean_humidity: Mean humidity.
        """
        if year not in self.monthly_calculations:
            self.monthly_calculations[year] = {}
        if month not in self.weather_data[year]:
            self.weather_data[year][month] = {}
        self.monthly_calculations[year][month] = {
            'average highest temp': avg_highest_temp,
            'average lowest temp': avg_lowest_temp,
            'mean humidity': mean_humidity
        }

    def add_yearly_result(self, year, highest_temp, highest_temp_day, lowest_temp, lowest_temp_day, most_humid_day,
                          humidity):
        """
        Add yearly weather calculation results.

        :param year: Year of the data.
        :param highest_temp: Highest temperature.
        :param highest_temp_day: Day of the highest temperature.
        :param lowest_temp: Lowest temperature.
        :param lowest_temp_day: Day of the lowest temperature.
        :param most_humid_day: Day with the highest humidity.
        :param humidity: Humidity value.
        """
        self.yearly_calculations[year] = {
            'highest temp': highest_temp,
            'highest temp day': highest_temp_day,
            'lowest temp': lowest_temp,
            'lowest temp day': lowest_temp_day,
            'most humid day': most_humid_day,
            'humidity': humidity
        }

    def get_yearly_calculations(self):
        """
        Get yearly weather calculation results.

        :return: Yearly weather calculations.
        """
        return self.yearly_calculations

    def get_monthly_calculations(self):
        """
        Get monthly weather calculation results.

        :return: Monthly weather calculations.
        """
        return self.monthly_calculations



