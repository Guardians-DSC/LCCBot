from flask import Flask
from flask import Blueprint
from flask import request
from flask import Response
from ..services.statusService import statusByHost
import paramiko

status_blueprint = Blueprint("status", __name__)

HOSTS = {
    "LCC1": "chopper.lcc.ufcg.edu.br",
    "LCC2": "r2d2.lcc.ufcg.edu.br",
    "LCC3": "kirk.lcc.ufcg.edu.br"
}

@status_blueprint.route('/status')
def status():
    lcc = request.args.get('lcc')
    resHTTPStatus = 200
    resData = {}

    try:
        if lcc != None:
            host = _validateLcc(lcc)
            if statusByHost(host) == True:
                resHTTPStatus = 200
            else: 
                resHTTPStatus = 503
        else:
            for lcc in HOSTS:
                host = HOSTS[lcc]
                if statusByHost(host) == True:
                    resData[lcc] =  "true"
                else: 
                    resData[lcc] = "false"
    except Exception: 
        resHTTPStatus = 400
    finally:
        return (resData, resHTTPStatus)

def _validateLcc(lcc):
    host = None
    if lcc == '1':
        host = HOSTS['LCC1']
    elif lcc == '2':
        host = HOSTS['LCC2']
    elif lcc == '3':
        host = HOSTS['LCC3']
    if host == None:
        raise Exception('Invalid LCC')
    return host