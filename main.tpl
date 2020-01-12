<head>
    <title>FLKA Kallender Generator</title>
</head>
<body  >
<h1>Wiki Kalender generator</h1>

<form action="/" method="get">
    Monat: <input type="number" min="1" max="12" value="{{month}}" name="monat"><br>
    Jahr: <input type="number" value="{{year}}" name="jahr"><br>
    <input type="submit" value="Generieren" name="generate">
</form>

Kopiere den Text unten und füge ihn ins wiki ein:<br>
<textarea readonly rows="30" cols="80">{{cal_data}}</textarea>


</body>
</html>