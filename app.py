from bottle import Bottle, route, run, template, static_file, request, error, hook, get, post, server_names
import bottle
import datetime
import fabkalendergenerator

@route('/static/<type>/<filename>')
def serve_css(type, filename):
    return static_file(filename, root=type+'/')


@get('/')
def main_menu():
    now = datetime.datetime.now()
    return template('main.tpl', cal_data=None, year=now.year, month=now.month)

@get('/')
def gen_stuff():
    now = datetime.datetime.now()
    month = request.params.get('monat')
    year = request.params.get('jahr')
    cal_data=None
    if month and year:
        cal_data=fabkalendergenerator.tabelle(month, year)
        print(cal_data)
    else:
        month=now.month
        year = now.year

    return template('main.tpl', cal_data=cal_data, year=year, month=month)


run(host='127.0.0.1', port=10123)