import sqlite3
import datetime
connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()
connection2 = sqlite3.connect("database2.sqlite")
cursor2 = connection2.cursor()

charges = {
    "Pedophilia": 30,
    "Jailbaiting": 30,
    "Doxxing": 30,
    "IP Grabbing": 25,
    "Information Spreading": 25,
    "DDoSing": 25,
    "Leaking": 15,
    "Account Compromising": 15,
    "Admin Abusing": 15,
    "Theft": 15
}

cursor2.execute("select * from cases")
oldcases = cursor2.fetchall()
casecounter = 1

for case in oldcases:
    if case[3] == "ACTIVE" or case[3] == "CLEARED":
        severity = 0
        expiredate = ""
        date = datetime.datetime.today()
        for charge in case[1].split("|"):
            if charge == "":
                continue
            if charge in charges:
                severity = sum((severity, charges[charge]))
                continue
            if charge.find("Exploiting") != -1:
                severity = sum((severity, 2)) # type: ignore
                continue
            elif charge.find("Malicious Distribution") != -1:
                severity = sum((severity, 15)) # type: ignore
                continue
            elif charge.find("Scamming") != -1:
                severity = sum((severity, 15)) # type: ignore
                continue
        pedocharge = False
        for charge in case[1].split("|"):
            if charge == "Pedophilia" or charge == "Jailbaiting":
                pedocharge = True
                expiredate = "NONE"
        if severity >= 20 and pedocharge == False:
            exp = date + datetime.timedelta(days=730)
            for charge in case[1].split("|"):
                if charge.find("Exploiting") != -1:
                    exp += datetime.timedelta(days=60)
                    break
            expiredate = exp.strftime("%d/%m/%Y")
        elif severity >= 10 and pedocharge == False:
            exp = date + datetime.timedelta(days=365)
            for charge in case[1].split("|"):
                if charge.find("Exploiting") != -1:
                    exp = exp + datetime.timedelta(days=60)
                    break
            expiredate = exp.strftime("%d/%m/%Y")
        elif pedocharge == False:
            exp = date
            for charge in case[1].split("|"):
                if charge.find("Exploiting") != -1:
                    exp = exp + datetime.timedelta(days=60)
                    break
            expiredate = exp.strftime("%d/%m/%Y")
        cursor.execute("insert into cases values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (casecounter, case[1], case[3], case[4], case[5], expiredate, case[6], case[7], case[8], case[9], case[10], severity))
        print(f"{case[0]} {case[2]} added")
        casecounter += 1

connection.commit()