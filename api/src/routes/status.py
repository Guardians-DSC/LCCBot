from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import paramiko

app =  Flask(__name__)

@app.route('/status')
def status():
    if not request.args.get('lcc') == None:
        lcc = request.args.get('lcc')
    
        if lcc == 1:
            host = "chopper.lcc.ufcg.edu.br"
        elif lcc == 2:
            host = "r2d2.lcc.ufcg.edu.br"
        elif lcc == 3:
            host = "kirk.lcc.ufcg.edu.br"
    
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=23456)
            ssh.close()
            return Response("{Online}", status=200, mimetype='application/json')
        except:
            return Response("{Offline}", status=503, mimetype='application/json')
    else:
        LCCs = ["chopper.lcc.ufcg.edu.br", "r2d2.lcc.ufcg.edu.br", "kirk.lcc.ufcg.edu.br"]
        statusLCC = {}
        for lcc in LCCs:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=lcc, port=23456)
                ssh.close()
                statusLCC[lcc] =  "true"
            except:
                statusLCC[lcc] = "false"
        return jsonify(statusLCC)  

if __name__ == "__main__":
    app.run()
