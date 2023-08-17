from flask import Flask, render_template, request
from model.weather_report_generator import WeatherReportGenerator
from model.weather_calculations import WeatherDataAnalyzer
from model.weather_data_parser import WeatherDataParser

app = Flask(__name__)

DIR_PATH = 'Data/weatherfiles'

weather_parser = WeatherDataParser(DIR_PATH)
weather_data = weather_parser.fetch_data()

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


@app.route('/')
def base():
    """
    The base route that renders the base template with years and months for user selection.
    """
    return render_template('base.html', years=weather_parser.get_years(), months=MONTHS)


@app.route('/generate-report', methods=['Post'])
def generate_report():
    """
    Route for generating weather reports based on user input.

    The user can select the report type (yearly, monthly, daily) and provide the year and month (if applicable).

    :return: Rendered report template.
    """
    report_type = request.form.get('report-type')

    dataAnalyzer = WeatherDataAnalyzer(weather_data)
    dataAnalyzer.comp_yearly_calculations()
    dataAnalyzer.comp_calculations_monthly()
    report_generator = WeatherReportGenerator(dataAnalyzer.get_yearly_calculations(),
                                              dataAnalyzer.get_monthly_calculations(),
                                              weather_data)
    barchart = False
    if report_type == 'year':
        generated_report = report_generator.generate_yearly_report(request.form.get('year'))
    elif report_type == 'month':
        generated_report = report_generator.generate_monthly_report(request.form.get('year'), request.form.get('month'))
    else:
        generated_report = report_generator.generate_daily_report(request.form.get('year'), request.form.get('month'))
        barchart = True

    return render_template('report.html', report=generated_report, barchart=barchart)


if __name__ == '__main__':
    app.run(debug=True)
