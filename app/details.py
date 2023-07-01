from fileinput import filename
import webbrowser

from urllib.request import urlopen
import pymongo
def details():

    # client = pymongo.MongoClient("mongodb://localhost:27017/")
    client = pymongo.MongoClient("mongodb+srv://hospital:n%40GAmXWZbPr.n3c@ambulance.ymqigbw.mongodb.net/test")
    mydb = client["ANPR"]
    mycol = mydb["carDetails"]

    li1 = []

    filcol = mycol.find()
    for z in filcol :

        li1.append({'name': z['name'],'carName': z['carName'],'plateNo': z['plateNo'],'address': z['address']})

        # if(math.isnan(z['latitude']) == False and math.isnan(z['longitude']) == False):
        #     coords_2 = (z['latitude'], z['longitude'])
        #     dis = geopy.distance.geodesic(coords_1, coords_2).km
        #     if(dis < 500):
        #         li1.append({'longitude': z['longitude'],
        #                 'latitude': z['latitude'],'Name': z['Health Facility Name']})
        #         li2.append(
        #             {'Name': z['Health Facility Name'], 'Distance': int(int(dis)*1.12)})

    # List Ka Code
    # li1.sort(key=lambda x: x[''])

    print(li1)

    tbl = ""
    c=0
    for y in li1:
        if c==30:
            break

        c=c+1
        a = "<tr><td>%s<td>" %y['name']
        b = "<td>%s</td>" %y['carName']
        d = "<td>%s</td>" %y['plateNo']
        e = "<td>%s</td></tr>" %y['address']
        tbl = tbl+a+b+d+e


    contents = '''<!DOCTYPE html>
    <html lang="en">
    <html>
    <head>
    <script src="https://kit.fontawesome.com/de9d45e1c6.js" crossorigin="anonymous"></script>
    <meta http-equiv="content-type">
    <link rel="stylesheet" href="details.css">
    <link rel="icon" type="image/png" href="">
    <title>ANPR</title>
    </head>
    <body>
    <div class="twoparts">
        <div class="container">
            <div class="containerhead">
                <label for="Search" class="label1">LIST OF VEHICLES</label>
                    <form action="" class="searchbar">
                    <input type="text" id="myinput" placeholder="Search your vehicle....." onkeyup="searchFun()">
                    </form>
            </div>
    <table  id="mytable">
    %s
    </table>  
        </div>

        </div>
        <script>
            const searchFun = () => {
                let filter = document.getElementById('myinput').value.toUpperCase();

                let myTable = document.getElementById('mytable');

                let tr = myTable.getElementsByTagName('tr');

                for (var i = 0; i < tr.length; i++) {
                    let td = tr[i].getElementsByTagName('td')[3];

                    if (td) {
                        let textvalue = td.textContent || td.innerHTML;

                        if (textvalue.toUpperCase().indexOf(filter) > -1) {
                            tr[i].style.display = "";
                        }
                        else 
                        {
                            tr[i].style.display = "none";
                        }
                    }
                }
            }
            </script>
    </body>
    </html>
    ''' % (tbl)

    filename = 'C:\\Users\\Bhavesh Saini\\Desktop\\ANPR\\app\\details.html'

    # List Code End


    def main(contents, filename):
        output = open(filename, "w")
        output.write(str(contents))
        output.close()


    main(contents, filename)

    webbrowser.open(filename)
    # webbrowser.open('info.html')
# details()

# window.location = "confirmation.html";