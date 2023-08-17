import os


DIR_PATH = 'Data/Weatherfiles'
SHORT_TO_FULL_MONTH = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

class WeatherDataParser:
    """
    A class for parsing weather data files.
    """
    def __init__(self, directory):
        """
        Initialize the WeatherDataParser.

        :param directory: Directory path containing weather data files.
        """
        self.directory = directory
        self.weather_data = {}
        self.years = []

    def parse_data(self):
        """
        Parse the weather data files in the specified directory and populate weather_data dictionary.
        """
        data = {}
        file_name_list = os.listdir(self.directory)

        for filename in file_name_list:
            year = filename.split('_')[2]
            month_abbr = filename.split('_')[3].split('.')[0].title()
            month = SHORT_TO_FULL_MONTH[month_abbr]

            if year not in self.weather_data:
                self.weather_data[year] = {}
            if month not in self.weather_data[year]:
                self.weather_data[year][month] = []

            file_path = DIR_PATH + '/' + filename

            with open(file_path, 'r') as f:
                lines = f.readlines()
            attributes = [attribute.strip() for attribute in lines[0].strip().split(',')]

            for line in lines[1:]:
                readings = line.strip().split(',')
                day_readings = {}
                for index, value in enumerate(readings):
                    if value:
                        day_readings[attributes[index]] = value
                    else:
                        day_readings[attributes[index]] = None
                self.weather_data[year][month].append(day_readings)

    def fetch_data(self):
        """
        Fetch and return the parsed weather data.

        :return: Parsed weather data.
        """
        self.parse_data()
        return self.weather_data

    def get_years(self):
        """
        Get a list of years present in the parsed weather data.

        :return: List of years.
        """
        self.years = list(self.weather_data.keys())
        self.years = sorted(self.years)
        return self.years




