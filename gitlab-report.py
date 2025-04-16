html = """
<html>
<head><meta http-equiv="Content-Type" content="text/html;charset=" utf-8"=""><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"></head>
    <body>
        <div class="container"><h1 class="display-1">Orchestrator Git Releases</h1><ul class="nav justify-content-center"><li class="nav-item"><a class="nav-link" href="./dcs-hsm_v253.html">dcs-hsm_v253</a></li><li class="nav-item"><a class="nav-link" href="./dcs-hsm_v252.html">dcs-hsm_v252</a></li><li class="nav-item"><a class="nav-link" href="./dca_v253.html">dca_v253</a></li><li class="nav-item"><a class="nav-link" href="./dca_v252.html">dca_v252</a></li><li class="nav-item"><a class="nav-link" href="./dcs-ts_v253.html">dcs-ts_v253</a></li><li class="nav-item"><a class="nav-link" href="./dcs-ts_v252.html">dcs-ts_v252</a></li><li class="nav-item"><a class="nav-link" href="./ias_v253.html">ias_v253</a></li><li class="nav-item"><a class="nav-link" href="./ias_v252.html">ias_v252</a></li><li class="nav-item"><a class="nav-link" href="./aqs_v253.html">aqs_v253</a></li><li class="nav-item"><a class="nav-link" href="./aqs_v252.html">aqs_v252</a></li></ul></div>
        <div style="height: 100px;"></div>
        <div style="display: flex; justify-content: center;">
                    <img src="img/fcsg.png" style="width:250px;height:250px;">
        </div>
        <div style="height: 100px;"></div>
        <h1 style="text-align:center">Kämpfen und Siegen</h1>
    </body>
</html>
"""
print(html)

with open("gitlab-report.html", "w") as file:
    file.write(html)