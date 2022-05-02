import functools
import json

from flask import Response


def returns_json(f):
    @functools.wraps(f)
    def fun(*args, **kwargs):
        res = f(*args, **kwargs)
        return Response(json.dumps(res),
                        headers=[('Access-Control-Allow-Origin', '*'), ('content-type', 'application/json')])

    return fun
