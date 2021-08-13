from flask import render_template, request, jsonify
from .import bp as app
from .models import DivvyTable
from datetime import datetime as dt


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    start = request.args.get('start')
    end = request.args.get('end')
    from_station_id = request.args.get('from_station_id')

    # If starting station id is given
    if from_station_id:
        # Find the station name from the input station ID
        from_station_name = DivvyTable.query.filter(DivvyTable.from_station_id == from_station_id).first().from_station_name
        # Get rows with this from_station_id and has a start and end time within the time period inputted
        valid_rows = DivvyTable.query.filter(DivvyTable.from_station_id == from_station_id, 
                                            DivvyTable.starttime >= dt.strptime(start, '%Y-%m-%d'),
                                            DivvyTable.stoptime <= dt.strptime(end, '%Y-%m-%d') ).all()
    else:
        # Only time period was given
        valid_rows = DivvyTable.query.filter(DivvyTable.starttime >= dt.strptime(start, '%Y-%m-%d'),
                                        DivvyTable.stoptime <= dt.strptime(end, '%Y-%m-%d') ).all()
    avg_duration = sum(record.trip_duration for record in valid_rows) / len(valid_rows)
    
    if from_station_id:
        return jsonify({
            'averageDuration': avg_duration,
            'fromStationId': from_station_id,
            'fromStationName': from_station_name
        })
    else:
        return jsonify({
            'averageDuration': avg_duration
        })
        