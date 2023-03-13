"""
Simple WEB app that converts from WGS84 to L-Est97 coordinate system and vice versa.

Author: Danyil Kurbatov
"""

from flask import Flask, render_template, request
from package_danyil.converter import convert_wgs_to_est, convert_est_to_wgs

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def convert_app():
    """Main program run method."""
    if request.method == 'POST':
        longitude = request.form['longitude']
        latitude = request.form['latitude']
        from_c = request.form['from_c']
        to_c = request.form['to_c']

        if from_c == 'wgs' and to_c == 'est':
            res = convert_wgs_to_est(latitude, longitude)
            return render_template('converter.html', result=res, latitude=latitude, longitude=longitude,
                                   from_c=from_c, to_c=to_c)
        elif from_c == 'est' and to_c == 'wgs':
            res = convert_est_to_wgs(latitude, longitude)
            return render_template('converter.html', result=res, latitude=latitude, longitude=longitude,
                                   from_c=from_c, to_c=to_c)
    else:
        return render_template('converter.html')


if __name__ == '__main__':
    app.run()
