from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def turtleview(request):
    con = """
    <!DOCTYPE html>
<html>
<head>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <style>
   .Game-Download {
    font-size: 30px;
    font-family: "Vazir";
    vertical-align: bottom;
    background-color: #eeeeee;
    width: 850px;
    height: 80px;
    text-align: center;
    border-radius: 10px;
}

.span1 {
    color: red;
}

.span2 {
    color: blue;
}

.span3 {
    color:green;
}

.span4 {
    color:red;
}


.span5 {
    color:blue;
}

a {
    text-decoration:none;
    
}

h1 {
    font-size: 66px;
    font-style: normal;
    font-family: sans-serif;
    background-color: #eee;
    width: 720px;
    border-radius: 25px;
    text-align: center;
    border-left: 35px solid blue;
    border-right: 35px solid red;
}

h2 {
    font-size: 37px;
    font-family: monospace;
    border-left: 20px solid red;
    border-right: 20px solid red;
    border: 3px solid red;
    width: 530px;
    height: 45px;
    text-align: center;
    border-radius: 5px;
}
   </style>
   <title>Games</title>
</head>
<body>
   <h1><span class="span1">TMNT</span> <span class="span2">Game</span></h1>
   <h2>Password : <span class="span3">www</span>.<span class="span4">yasdl</span>.<span class="span5">com</span></h2>
   <div class="Game-Download">
      <a href="https://dl.yasdl.com/Arash/2022/Game/Teenage.Mutant.Ninja.Turtles.Shredders.Revenge-Razor1911_YasDL.com.rar?aa2bb"
      target="_blank" title="Teenage Mutant Ninja Turtles Shredders Revenge"><hr> دانلود بازی Teenage Mutant Ninja Turtles: Shredders Revenge<hr></a>
</div>
</body>
</html>
    """
    return HttpResponse(con)