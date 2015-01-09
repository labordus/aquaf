webpage = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Aquaf foto overzicht</title>
<link rel="icon" type="image/png"
    href="http://www.aquaforum.nl/favicon.ico">
<link
    href="http://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.3/fotorama.css"
    rel="stylesheet">
<style type="text/css">
body {
    background-image: url(http://www.aquaforum.nl/ubb/images/back1.png);
    background-repeat: repeat;
    text-align: center;
}

.logobar {
    padding: 0;
    border: 0;
}

.maindiv {
    BORDER-RIGHT: #363466 1px solid;
    PADDING-RIGHT: 2px;
    BORDER-TOP: #363466 1px solid;
    PADDING-LEFT: 2px;
    PADDING-BOTTOM: 2pt;
    MARGIN-LEFT: auto;
    BORDER-LEFT: #363466 1px solid;
    WIDTH: 630px;
    MARGIN-RIGHT: auto;
    PADDING-TOP: 2pt;
    BORDER-BOTTOM: #363466 1px solid;
    POSITION: relative;
}

.fotorama, .fotorama-caption {
    width: 800px;
    max-width: 100%;
    margin-right: auto;
    margin-left: auto;
}

.fotorama-caption {
    text-align: center;
    line-height: 1.5;
    color: #CC0000;
    font-family: Georgia, serif; strong { font-weight : normal;
    color: #eee;
}

}
.fotorama__thumb-border {
    border-color: #FF0000;
}
</style>
</head>
<body>
    <div class="maindiv">
        <table>
            <tr>
                <td class="logobar"><a
                    href="http://www.aquaforum.nl/ubb/ubbthreads.php"> <img
                        style="display: block;"
                        src="http://www.aquaforum.nl/ubb/images/forumbanner.gif"
                        alt="Aquaforum.nl banner">
                </a></td>
            </tr>
        </table>
    </div>
    <div class="fotorama" data-nav="thumbs" data-keyboard="true" data-auto="false"
        data-navposition="bottom" data-fit="scaledown" data-width="800"
        data-height="600" data-click="true" data-loop="true"></div>
    <p class="fotorama-caption"></p>

    <script type="text/javascript"
        src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script type="text/javascript"
        src="http://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.3/fotorama.js"></script>
    <script type="text/javascript">
        $('.fotorama')
                .fotorama($jsoncontent);

        $('.fotorama').on(
                'fotorama:show ' + 'fotorama:load',
                function(e, fotorama) {
                    fotorama.$caption = fotorama.$caption
                            || $(this).next('.fotorama-caption');
                    var activeFrame = fotorama.activeFrame;
                    fotorama.$caption.html('<table style="border-collapse:collapse;border-spacing:0;border-color:#aabcfe;border-width:1px;border-style:solid;margin:0px auto"><tr><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#039;background-color:#e8edff;text-align:center" colspan="2">Gebruik onderstaande code in het forum bericht</th></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#fe0000;background-color:#f2d0d0;font-weight:bold;text-align:center" colspan="2">' + '[IMG]' + activeFrame.img + '[/IMG]' + '</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#669;background-color:#e8edff" colspan="2">Uploaddatum = ' + activeFrame.stamp + '</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#669;background-color:#e8edff" colspan="2">Dimensie = ' + activeFrame.width + 'x' + activeFrame.height + '</td></tr></table>');
            }).fotorama();
    </script>
</body>
</html>

'''