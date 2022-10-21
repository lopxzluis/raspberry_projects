import socket
#import rgb_pwm
from machine import PWM, Pin
import time
import network

servo1 = PWM(Pin(13))
servo1.freq(50)

#rgb = rgb_pwm.rgbpwm(33,25,26,50,True)

#rgb.off()
ssid = 'ميركوسيس' #ميركوسيس #Nombre de la Red
password = 'lopezparra0426' #Contraseña de la red
wlan = network.WLAN(network.STA_IF)
wlan.active(True) #Activa el Wifi
wlan.connect(ssid, password) #Hace la conexión
while wlan.isconnected() == False: #Espera a que se conecte a la red
    pass
print('Conexion con el WiFi %s establecida' % ssid)
print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi

r_value = "0"
g_value = "0"
b_value = "0"

def web_page():   
    
    html = """
        <html>

<head>
    <title>ESP32 Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>

    <style>
        html {
            font-family: Helvetica;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
            size: 90px;
        }

        h1 {
            color: #0F3376;
            padding: 2vh;
        }

        p {
            font-size: 1.5rem;
        }

        table {
            margin: auto;
        }

        td {
            padding: 10px;            
        }

        .Button {
            border-radius: 31px;
            display: inline-block;
            cursor: pointer;
            color: #ffffff;
            font-family: Arial;
            font-size: 17px;
            font-weight: bold;
            font-style: italic;
            padding: 17px 19px;
            text-decoration: none;
        }

        .ButtonR {
            background-color: rgb(255, 30, 30);
            border: 3px solid #991f1f;
            text-shadow: 0px 2px 2px #471e1e;
        }

        .Button:active {
            position: relative;
            top: 1px;
        }

        .ButtonG {
            background-color: rgb(30, 255, 30);
            border: 3px solid #23991f;
            text-shadow: 0px 2px 2px #1e4723;
        }
        .range {
            margin: auto;
            -webkit-appearance: none;
            position: relative;
            overflow: hidden;
            height: 40px;
            width: 200px;
            cursor: pointer;
            border-radius: 0;

        }

        ::-webkit-slider-runnable-track {
            background: #ddd;
        }

        .range::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 20px;
            height: 40px;
            border: 2px solid #999;
        }

        .redrange::-webkit-slider-thumb {
            background: #fff;
            box-shadow: -100vw 0 0 100vw rgb(255, 30, 30);
        }

        .greenrange::-webkit-slider-thumb {
            background: #fff;
            box-shadow: -100vw 0 0 100vw rgb(30, 255, 30);
        }
        .slider {
            -webkit-appearance: none;
            width: 100%;
            height: 25px;
            background: #d3d3d3;
            outline: none;
            opacity: 0.7;
            -webkit-transition: .2s;
            transition: opacity .2s;
        }

        .slider:hover {
            opacity: 1;
        }

        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 25px;
            height: 25px;
            background: #04AA6D;
            cursor: pointer;
        }

        .slider::-moz-range-thumb {
            width: 25px;
            height: 25px;
            background: #04AA6D;
            cursor: pointer;
        }

        .slidecontainer {
            width: 100%;
        }
         #rinput{
            font-size:20pt;
        }
        #h1luis{
            font-size: 50px;

        }
        #pluis{
            font-size: 33px;
        }
        #rvalue{
            margin-top: 10px;
            height: 45px;
            font-size: 32px;
        }
        #btn_luis{
            height: 75px;
            width: 75px;
            font-size: 25px;
        }
    </style>

</head>

<h1 id="h1luis">Control Servo</h1>
<p id="pluis">0 - 180 Grados</p>
<form>
    
    <br>
    <div  class="d-inline-flex  justify-content-center w-100 p-3 mw-100 h-75 d-inline-block">

        <div class="d-flex flex-column">
            <div class="">
                <input id="rinput" style="width: 290px;" name="rinput"  type="range" class="form-range" id="customRange1" max="180" value=" @@"""+ r_value +""" @@">
            </div>

            <strong id="rvalue"> """+ r_value +""" </strong>

            <div class="p-4">
               <p><a> <button  class="ButtonR Button" id="btn_luis">X</button></a></p>
               
            </div>

        </div>
        
    </div>
</form>
<script>
    var sliderr = document.getElementById("rinput");
    var outputr = document.getElementById("rvalue");
    outputr.innerHTML = sliderr.value;
    sliderr.oninput = function () {
        outputr.innerHTML = this.value;
    }

    var sliderg = document.getElementById("ginput");
    var outputg = document.getElementById("gvalue");
    outputg.innerHTML = sliderg.value;
    sliderg.oninput = function () {
        outputg.innerHTML = this.value;
    }
</script>
</html>

        """
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(1)

while True:
    try:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = request.decode().split() 
        
        if 'rinput' in request[1]:
            r_value = request[1].split('&')[0].split('=')[1]
            #g_value = request[1].split('&')[1].split('=')[1]
            
            print(r_value)
            print(g_value)
            
            valor_servo = ((int(r_value)+45)*100000)/9
            servo1.duty_ns(int(valor_servo))
             
            #134 max
            #18 min
            #rgb.red(int(int(r_value) * 1.1717 + 18)) 
            #rgb.green(int(int(g_value) * 1.1717 + 18)) 
               
        
        response = web_page()        
        response = response.replace(" @@", "")
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except Exception as e:
        print(e)