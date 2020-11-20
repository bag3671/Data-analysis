from flask import Flask
import folium
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (37.5509655144007, 126.849532173376)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

@app.route('/marker')
def markerr():
    df = pd.read_csv("address3.csv")
    df['icon'] = ['asterisk','tint','check','sd-video','cloud-upload']
    color_dict = {'Clouds' : "blue",'sunny':'red'}
    mapping = folium.Map(location=[df.lat.mean(),df.lng.mean()],zoom_start=11)
    for i in df.index:
        folium.Marker(
            [df.lat[i],df.lng[i]], 
            popup=df["지역"][i], 
            tooltip=f'{df.desc[i]}, {df.temp[i]}',
            icon=folium.Icon(color = color_dict[df.weather[i]],icon=df.icon[i])).add_to(mapping)
    return mapping._repr_html_()
if __name__ == '__main__':
    app.run(debug=True)