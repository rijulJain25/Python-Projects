from tkinter import *
from tkinter import ttk
import wikipedia
from geopy.geocoders import Nominatim
from googletrans import Translator
import gmplot
import os
from geopy import distance
import requests
from bs4 import BeautifulSoup
import requests, json
import datetime
from suntime import Sun
from timezonefinder import TimezoneFinder

root = Tk()
root.title("Escort Amigo")

r = IntVar()
r.set(1)
frame = LabelFrame(root, text="Options Available", padx=50, pady=50)  # padding inside the frame
frame.pack(padx=40, pady=40)  # padding outside of frame

options = [("Geo Locator", 1), ("Weather", 2), ("Map", 3), ("Train TT", 4), ("Convertor", 5), ("Search", 6)]

for text, num in options:
    Radiobutton(frame, text=text, variable=r, value=num).pack(anchor=W)


def click(value):
    if value == 1:
        top = Toplevel()
        top.title("Geo Locator")

        global options1
        t = IntVar()
        t.set(1)
        frame = LabelFrame(top, text="Find", padx=50, pady=50)  # padding inside the frame
        frame.pack(padx=10, pady=10)  # padding outside of frame

        options1 = [("Place through Zipcode", 1), ("Zipcode through place", 2), ("Co-ordinates through place", 3),
                    ("Place through co-ordinates", 4), ("Distance Between Places", 5)]

        for text, num in options1:
            Radiobutton(frame, text=text, variable=t, value=num).pack(anchor=W)

        def next(val):
            if val == 1:
                mid = Toplevel()
                mid.title("Place through Zipcode")
                m = IntVar()
                m.set(1)
                frame = LabelFrame(mid, text="Find", padx=50, pady=50)  # padding inside the frame
                frame.pack(padx=10, pady=10)  # padding outside of frame
                geolocator = Nominatim(user_agent="geoapiExercises")

                zipcode = Entry(frame, width=35, borderwidth=5)
                zipcode.insert(0, "Enter zipcode of place to search")
                zipcode.grid(row=0, column=0, columnspan=2)

                def find():
                    top1 = Toplevel()
                    top1.title("Result")

                    frame1 = LabelFrame(top1, text="Address", padx=50, pady=50)  # padding inside the frame
                    frame1.pack(padx=10, pady=10)  # padding outside of frame
                    location = geolocator.geocode(zipcode.get())
                    my_label1 = Label(frame1, text="Zipcode: " + str(zipcode.get()))
                    my_label1.grid(row=0, column=0)
                    my_label2 = Label(frame1, text="Location is: " + str(location))
                    my_label2.grid(row=1, column=0)

                button = Button(frame, text="Find", command=find)
                button.grid(row=1, column=1)
            elif val == 2:
                mid = Toplevel()
                mid.title("Zipcode thorugh Place")

                m = IntVar()
                m.set(1)
                frame = LabelFrame(mid, text="Find", padx=50, pady=50)  # padding inside the frame
                frame.pack(padx=10, pady=10)  # padding outside of frame

                geolocator = Nominatim(user_agent="geoapiExercises")

                place = Entry(frame, width=35, borderwidth=5)
                place.insert(0, "Enter place to search for zipcode")
                place.grid(row=0, column=0, columnspan=2)

                def find():
                    top1 = Toplevel()
                    top1.title("Result")

                    frame1 = LabelFrame(top1, text="Zipcode", padx=50, pady=50)  # padding inside the frame
                    frame1.pack(padx=10, pady=10)  # padding outside of frame
                    location = geolocator.geocode(place.get())
                    # traverse the data
                    data = location.raw
                    loc_data = data['display_name'].split()
                    my_label1 = Label(frame1, text="Zipcode: " + loc_data[-2])
                    my_label1.grid(row=0, column=0)
                    my_label2 = Label(frame1, text="Location: " + str(location))
                    my_label2.grid(row=1, column=0)

                button = Button(frame, text="Find", command=find)
                button.grid(row=1, column=1)
            elif val == 3:
                mid = Toplevel()
                mid.title("Co-ordinates through place")

                m = IntVar()
                m.set(1)
                frame = LabelFrame(mid, text="Find", padx=50, pady=50)  # padding inside the frame
                frame.pack(padx=10, pady=10)  # padding outside of frame
                global loc

                loc = Nominatim(user_agent="GetLoc")

                place = Entry(frame, width=35, borderwidth=5)
                place.insert(0, "Enter place name")
                place.grid(row=0, column=0, columnspan=2)

                def find():
                    top1 = Toplevel()
                    top1.title("Result")

                    frame1 = LabelFrame(top1, text="Co-ordinates", padx=50, pady=50)  # padding inside the frame
                    frame1.pack(padx=10, pady=10)  # padding outside of frame
                    getLoc = loc.geocode(place.get())
                    my_label1 = Label(frame1, text="Address: " + getLoc.address)
                    my_label1.grid(row=0, column=0)
                    my_label2 = Label(frame1, text="Latitude: " + str(getLoc.latitude))
                    my_label2.grid(row=1, column=0)
                    my_label2 = Label(frame1, text="Longitude: " + str(getLoc.longitude))
                    my_label2.grid(row=2, column=0)

                button = Button(frame, text="Find", command=find)
                button.grid(row=1, column=1)
            elif val == 4:
                mid = Toplevel()
                mid.title("Place through co-ordinates")
                m = IntVar()
                m.set(1)
                frame = LabelFrame(mid, text="Find", padx=50, pady=50)  # padding inside the frame
                frame.pack(padx=10, pady=10)  # padding outside of frame
                geoLoc = Nominatim(user_agent="GetLoc")

                lat = Entry(frame, width=35, borderwidth=5)
                lat.insert(0, "Enter latitude for place")
                lat.grid(row=0, column=0, columnspan=2)
                lon = Entry(frame, width=35, borderwidth=5)
                lon.insert(0, "Enter longitude for place")
                lon.grid(row=1, column=0, columnspan=2)

                def find():
                    top1 = Toplevel()
                    top1.title("Result")
                    frame1 = LabelFrame(top1, text="Place Name", padx=50, pady=50)  # padding inside the frame
                    frame1.pack(padx=10, pady=10)  # padding outside of frame
                    loc = float(lat.get()), float(lon.get())
                    locname = geoLoc.reverse(loc)
                    my_label1 = Label(frame1, text="Address: " + locname.address)
                    my_label1.grid(row=0, column=0)

                button = Button(frame, text="Find", command=find)
                button.grid(row=2, column=1)
            elif val == 5:
                mid = Toplevel()
                mid.title("Distance Between Places")

                m = IntVar()
                m.set(1)
                frame = LabelFrame(mid, text="Find", padx=50, pady=50)  # padding inside the frame
                frame.pack(padx=10, pady=10)  # padding outside of frame
                geolocator = Nominatim(user_agent="geoapiExercises")

                place1 = Entry(frame, width=35, borderwidth=5)
                place1.insert(0, "Enter Place(From)")
                place1.grid(row=0, column=0, columnspan=2)

                place2 = Entry(frame, width=35, borderwidth=5)
                place2.insert(0, "Enter Place(To)")
                place2.grid(row=1, column=0, columnspan=2)

                def find():
                    top1 = Toplevel()
                    top1.title("Result")

                    frame1 = LabelFrame(top1, text="Distance", padx=50, pady=50)  # padding inside the frame
                    frame1.pack(padx=10, pady=10)  # padding outside of frame
                    p1 = geolocator.geocode(str(place1.get()))
                    p2 = geolocator.geocode(str(place2.get()))
                    Loc1_lat, Loc1_lon = (p1.latitude), (p1.longitude)
                    Loc2_lat, Loc2_lon = (p2.latitude), (p2.longitude)
                    location1 = (Loc1_lat, Loc1_lon)
                    location2 = (Loc2_lat, Loc2_lon)
                    res = (str(distance.distance(location1, location2).km) + " Km")
                    my_label1 = Label(frame1, text="Distance: " + res)
                    my_label1.grid(row=0, column=0)

                button = Button(frame, text="Find", command=find)
                button.grid(row=2, column=1)

        button = Button(top, text="Next", command=lambda: next(t.get()))
        button.pack()

    elif value == 2:
        top = Toplevel()
        top.title("Weather Finder")

        t = IntVar()
        t.set(1)
        frame = LabelFrame(top, text="Place Name", padx=50, pady=50)  # padding inside the frame
        frame.pack(padx=10, pady=10)  # padding outside of frame

        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

        city = Entry(frame, width=35, borderwidth=5)
        city.insert(0, "Please enter city name")
        city.grid(row=0, column=0, columnspan=2)

        def next(val):
            mid = Toplevel()
            mid.title("Weather")

            frame1 = LabelFrame(mid, text="Weather", padx=50, pady=50)  # padding inside the frame
            frame1.pack(padx=10, pady=10)  # padding outside of frame

            API_KEY = "95d77195c5450d4b98551a8111d2aa1d"
            URL = BASE_URL + "q=" + city.get() + "&appid=" + API_KEY
            response = requests.get(URL)
            geolocator = Nominatim(user_agent="geoapiExercises")
            global location
            location = geolocator.geocode(city.get())
            latitude = location.latitude
            longitude = location.longitude
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            my_label1 = Label(frame1, text="City: " + city.get())
            my_label1.grid(row=0, column=0)
            my_label2 = Label(frame1, text="Time Zone: " + str(result))
            my_label2.grid(row=1, column=0)

            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = main['temp']
                humidity = main['humidity']
                pressure = main['pressure']
                report = data['weather']
                my_label3 = Label(frame1, text=f"Temperature: {temperature} Kelvin")
                my_label3.grid(row=2, column=0)
                my_label4 = Label(frame1, text=f"Humidity: {humidity} percent")
                my_label4.grid(row=3, column=0)
                my_label5 = Label(frame1, text=f"Pressure: {pressure} hPa")
                my_label5.grid(row=4, column=0)
                my_label6 = Label(frame1, text=f"Weather Report: {report[0]['description']}")
                my_label6.grid(row=5, column=0)
            sun = Sun(latitude, longitude)
            time_zone = datetime.date(2021, 9, 13)
            sun_rise = sun.get_local_sunrise_time(time_zone)
            sun_dusk = sun.get_local_sunset_time(time_zone)
            my_label6 = Label(frame1, text="Sun rise at : " + str(sun_rise.strftime('%H:%M')))
            my_label6.grid(row=6, column=0)
            my_label6 = Label(frame1, text="Dusk at : " + str(sun_dusk.strftime('%H:%M')))
            my_label6.grid(row=7, column=0)

        button = Button(top, text="Find", command=lambda: next(city.get()))
        button.pack()

    elif value == 3:
        top = Toplevel()
        top.title("Weather Finder")

        t = IntVar()
        t.set(1)
        frame = LabelFrame(top, text="Place Name", padx=50, pady=50)  # padding inside the frame
        frame.pack(padx=10, pady=10)  # padding outside of frame

        loc = Nominatim(user_agent="GetLoc")

        place = Entry(frame, width=35, borderwidth=5)
        place.insert(0, "Please enter city name")
        place.grid(row=0, column=0, columnspan=2)

        def find(val):
            getLoc = loc.geocode(val)
            lat = getLoc.latitude
            lon = getLoc.longitude
            gmap1 = gmplot.GoogleMapPlotter(lat, lon, 13)
            cpath = "D:\\map11.html"
            gmap1.draw(cpath)
            os.startfile(cpath)

        button = Button(top, text="Find", command=lambda: find(place.get()))
        button.pack()
    elif value == 4:
        top = Toplevel()
        top.title("Schedule Finder")

        t = IntVar()
        t.set(1)
        frame = LabelFrame(top, text="Train Data", padx=50, pady=50)  # padding inside the frame
        frame.pack(padx=10, pady=10)  # padding outside of frame

        def getdata(url):
            r = requests.get(url)
            return r.text

        station1 = Entry(frame, width=35, borderwidth=5)
        station1.insert(0, "Please enter code of Station(From)")
        station1.grid(row=0, column=0, columnspan=2)
        station2 = Entry(frame, width=35, borderwidth=5)
        station2.insert(0, "Please enter code of Station(To)")
        station2.grid(row=1, column=0, columnspan=2)
        sname1 = Entry(frame, width=35, borderwidth=5)
        sname1.insert(0, "Please enter name of Station(From)")
        sname1.grid(row=2, column=0, columnspan=2)
        sname2 = Entry(frame, width=35, borderwidth=5)
        sname2.insert(0, "Please enter name of Station(To)")
        sname2.grid(row=3, column=0, columnspan=2)
        date = Entry(frame, width=35, borderwidth=5)
        date.insert(0, "Please enter date")
        date.grid(row=4, column=0, columnspan=2)

        def find():
            mid = Toplevel()
            mid.title("Schedule")

            mid.geometry("500x500")

            # pass the url into getdata function
            url = "https://www.railyatri.in/booking/trains-between-stations?from_code=" + station1.get() + "&from_name=" + sname1.get() + "+JN+&journey_date=" + date.get() + "&src=tbs&to_code=" + station2.get() + "&to_name=" + sname2.get() + "+JN+&user_id=-1636260722&user_token=61636260722&utm_source=train_ticket_dweb_search"

            htmldata = getdata(url)
            soup = BeautifulSoup(htmldata, 'html.parser')
            # find the Html tag
            # with find()
            # and convert into string
            data_str = ""
            data_str1 = ""
            for item in soup.find_all("div", class_="TravelTimeInfo"):
                data_str = data_str + item.get_text()
            result1 = data_str.split("\n")
            for item in soup.find_all("div", class_="namePart"):
                data_str = data_str + item.get_text()
            result2 = data_str.split("\n")

            # Display the result
            for element in result1:
                if element in result2:
                    result2.remove(element)
            result1 = list(filter(None, result1))

            my_tree = ttk.Treeview(mid)
            my_tree['columns'] = ("ele1", "ele2")

            my_tree.column("#0", width=0)
            my_tree.column("ele1", width=300, anchor=W)
            my_tree.column("ele2", width=150, anchor=W)

            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("ele1", text="Train Names", anchor=W)
            my_tree.heading("ele2", text="Timings", anchor=W)

            l = [[] for i in range(len(result2))]
            s = ['a', 'aa', 'aaa', 'aaaa', '   ', 's', 'ss', 'sss', 'ssss']
            t = ['q', '', 'w']
            k = 0
            j = 0
            for i in range(len(result2) - 1):
                if result2[i] == '':
                    j = j + 1
                else:
                    l[j].append(result2[i])

            for i in range(len(result1) - 1):
                if result1[i] == '                              ' or result1[i] == ' ' or result1[i] == '            ':
                    k = k + 1
                else:
                    l[k].append(result1[i])

            d = []
            p = []
            for d in range(len(l) - 1):
                if len(l[d]) == 6:
                    p.append(l[d])

            c = 0
            for r in p:
                my_tree.insert(parent='', index='end', iid=c, text="", values=(r[0], r[1]))
                c = c + 1
                my_tree.insert(parent='', index='end', iid=c, text="", values=('', r[2]))
                my_tree.move(c, c - 1, 'end')
                c = c + 1
                my_tree.insert(parent='', index='end', iid=c, text="", values=('', r[3]))
                my_tree.move(c, c - 2, 'end')
                c = c + 1
                my_tree.insert(parent='', index='end', iid=c, text="", values=('', r[4]))
                my_tree.move(c, c - 3, 'end')
                c = c + 1
                my_tree.insert(parent='', index='end', iid=c, text="", values=('', r[5]))
                my_tree.move(c, c - 4, 'end')
                c = c + 1

            my_tree.pack(padx=40, pady=40)

        button = Button(top, text="Find", command=find)
        button.pack()

    elif value == 5:
        top = Toplevel()
        top.title("Convertor")

        global options2
        t1 = IntVar()
        t1.set(1)
        frame = LabelFrame(top, text="Convertor", padx=50, pady=50)  # padding inside the frame
        frame.pack(padx=10, pady=10)  # padding outside of frame

        options2 = [("Currency Convertor", 1), ("Language Convertor", 2)]

        for text, num in options2:
            Radiobutton(frame, text=text, variable=t1, value=num).pack(anchor=W)

        def next1(val):
            if val == 1:
                top1 = Toplevel()
                top1.title("Currency Convertor")

                t = IntVar()
                t.set(1)

                frame = LabelFrame(top1, text="Convert", padx=50, pady=50)  # padding inside the frame
                frame.pack(padx=10, pady=10)  # padding outside of frame

                global curf
                global curt
                global amtt

                curf = Entry(frame, width=35, borderwidth=5)
                curf.insert(0, "Enter currency(From)")
                curf.grid(row=0, column=0, columnspan=2)
                curt = Entry(frame, width=35, borderwidth=5)
                curt.insert(0, "Enter currency(To)")
                curt.grid(row=1, column=0, columnspan=2)
                amtt = Entry(frame, width=35, borderwidth=5)
                amtt.insert(0, "Enter Amount")
                amtt.grid(row=2, column=0, columnspan=2)

                def con():
                    mid = Toplevel()
                    mid.title("Currency Convertor")

                    m = IntVar()
                    m.set(1)

                    frame1 = LabelFrame(mid, text="Convert", padx=50, pady=50)  # padding inside the frame
                    frame1.pack(padx=10, pady=10)  # padding outside of frame

                    class RealTimeCurrencyConverter():
                        def __init__(self, url):
                            self.data = requests.get(url).json()
                            self.currencies = self.data['rates']

                        def convert(self, from_currency, to_currency, amount):
                            initial_amount = amount
                            # first convert it into USD if it is not in USD.
                            # because our base currency is USD
                            if from_currency != 'USD':
                                amount = amount / self.currencies[from_currency]

                            # limiting the precision to 4 decimal places
                            amount = round(amount * self.currencies[to_currency], 4)
                            return amount

                    currfrom = curf.get()
                    currto = curt.get()
                    amt = int(amtt.get())
                    url = 'https://api.exchangerate-api.com/v4/latest/USD'
                    converter = RealTimeCurrencyConverter(url)
                    my_label1 = Label(frame1, text="Converted Amount= " + str(
                        converter.convert(currfrom, currto, amt)) + currto)
                    my_label1.grid(row=0, column=0)

                button = Button(top1, text="Convert", command=con)
                button.pack()

            elif val == 2:
                top1 = Toplevel()
                top1.title("Language Convertor")

                t = IntVar()
                t.set(1)

                frame = LabelFrame(top1, text="Convert", padx=50, pady=50)  # padding inside the frame
                frame.pack(padx=10, pady=10)  # padding outside of frame

                translator = Translator()

                text = Entry(frame, width=35, borderwidth=5)
                text.insert(0, "Enter text")
                text.grid(row=0, column=0, columnspan=2)

                lanf = Entry(frame, width=35, borderwidth=5)
                lanf.insert(0, "Translate from")
                lanf.grid(row=1, column=0, columnspan=2)

                lant = Entry(frame, width=35, borderwidth=5)
                lant.insert(0, "Translate to")
                lant.grid(row=2, column=0, columnspan=2)

                def con():
                    mid = Toplevel()
                    mid.title("Language Convertor")

                    m = IntVar()
                    m.set(1)

                    frame1 = LabelFrame(mid, text="Convert", padx=50, pady=50)  # padding inside the frame
                    frame1.pack(padx=10, pady=10)  # padding outside of frame

                    # translate text
                    translated_text = translator.translate(text.get(), src=lanf.get(), dest=lant.get())

                    my_label1 = Label(frame1, text=f"The Actual Text was: {text.get()}")
                    my_label1.grid(row=0, column=0)
                    my_label2 = Label(frame1, text=f"The Translated Text is: {translated_text.text}")
                    my_label2.grid(row=1, column=0)

                button = Button(top1, text="Convert", command=con)
                button.pack()

        button = Button(top, text="Next", command=lambda: next1(t1.get()))
        button.pack()
    elif value == 6:
        top = Toplevel()
        top.title("Search")

        t = IntVar()
        t.set(1)
        frame = LabelFrame(top, text="Find", padx=50, pady=50)  # padding inside the frame
        frame.pack(padx=10, pady=10)  # padding outside of frame

        query = Entry(frame, width=35, borderwidth=5)
        query.insert(0, "Enter place name to search")
        query.grid(row=0, column=0, columnspan=2)

        def search():
            mid = Toplevel()
            mid.title("Search Result")

            m = IntVar()
            m.set(1)

            frame1 = LabelFrame(mid, text="Information Found", padx=50, pady=50)  # padding inside the frame
            frame1.pack(padx=10, pady=10)  # padding outside of frame
            results = wikipedia.summary(query.get(), sentences=6)
            my_label2 = Label(frame1, text=results, wraplength=800, justify=LEFT)
            my_label2.grid(row=1, column=0, columnspan=3, rowspan=3)

        button = Button(top, text="Next", command=lambda: search())
        button.pack()


button = Button(root, text="Next", command=lambda: click(r.get()))
button.pack()

root.mainloop()