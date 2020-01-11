#!/usr/bin/env python3

import sys
import os
import getopt
import calendar
import datetime
import locale


weekdays=['Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag']

daystoprint=[True,False,True,False,True,True,False]



def header (monat, jahr):
    print (f'\n======  Öffnungstage {datetime.date(jahr,monat,1).strftime("%B")} {jahr} ======\n')
    print ('[[:labsitter:intern:tagesliste_regeln|Regeln]]\n')

def tabelle (monat, jahr):
    donnerstage=0

    out = ("^Datum^Wochentag^   \\ Labsitter \\   \\ 18-20Uhr^   \\ Labsitter \\   \\ 20-22 Uhr^Kommentar|\n")
    cal= calendar.Calendar()
    for (tag, wochentag) in cal.itermonthdays2(int(jahr), int(monat)):
        if tag==0:
            continue
        if wochentag==3:
            donnerstage+= 1
            if donnerstage==3:
                out += (f"|{tag}.{monat}.|**{weekdays[wochentag]}**| | |**OpenLabDay** |\n")
                out += (f"|{tag}.{monat}.|**{weekdays[wochentag]}**| | |**OpenLabDay** |\n")
                continue
        if daystoprint[wochentag]:
            out += (f"|{tag}.{monat}.|{weekdays[wochentag]}| | | |\n")
    out += ("\n\n")
    print(out)
    return out

def main(argv):

    locale.setlocale(locale.LC_ALL, '')
    try:
        opts, optargs = getopt.getopt(argv,"", ["monat=","jahr="])

    except getopt.ParameterError:
        sys.exit(2)

    monat=jahr=''
    for opt, arg in opts:
        if opt in ("--monat") :
            monat= arg
        if opt in ("--jahr") :
            jahr= arg

    if monat=='' and jahr=='':
        print("\nlabkalendergenerator --monat=nn --jahr=nnnn\n\n"
	      "          monat  Monatnummer 1-12\n"
	      "          jahr   Das Jahr\n")
        sys.exit(0)
    if jahr.isdigit() and int(jahr)>2019 and int(jahr)<2200 :
        jahr= int(jahr)
    else : sys.exit("\nERROR: Parameter jahr illegaler Wert\n")
    if monat.isdigit() and int(monat)>=1 and int(monat)<=12 :
        monat= int(monat)
    else : sys.exit("\nERROR: Parameter monat illegaler Wert\n")
    
    header(monat,jahr)
    tabelle(monat,jahr)
    


if __name__ == '__main__':
    main(sys.argv[1:])
