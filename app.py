@app.route('/single_ride_with_map/<int:ride_id>')
def single_ride_with_map(ride_id):
    return render_template('single_ride_with_map.html', ride_id=ride_id)
