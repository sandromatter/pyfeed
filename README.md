# Pyfeed  
Das Code Projekt wurde im Modul *Programmierung 2* an der Fachhochschule Graubünden umgesetzt.   

**zum Projekt**: http://URL-EINGEBEN

---

## Ausgangslage 
Fangen wir mit den Basics an. Pyfeed macht Gebrauch von der Web-Technologie <a href="https://en.wikipedia.org/wiki/RSS" target="_blank">RSS</a> (RDF Site Summary oder Really Simple Syndication). Dabei handelt es sich um einen XML-basierten Web-Feed, der es Benutzern und Anwendungen ermöglicht, auf Aktualisierungen von Websites in einem standardisierten, computerlesbaren Format zuzugreifen. Tools wie der <a href="https://feedly.com/" target="_blank">Feedly</a>-Reader ermöglichen es Benutzern, die RSS-Feeds zu verfolgen, indem sie die Feeds vieler verschiedener Websites abonnieren oder zu einem "News-Aggregator" Ihrer Wahl hinzufügen.

Kurz gesagt: RSS-Feeds sind ein großartiges Stück Technik, das leider beinahe in Vergessenheit geraten ist. Ein Schwachpunkt von RSS-Feeds ist, dass diese nicht standardisiert sind und im Feed oft Informationen fehlen, die ein Feedreader zur Anzeige Ihrer Inhalte benötigen könnte. Ursprünglich nahm sich der <a href="https://feedburner.google.com/" target="_blank">Google Feedburner</a> dieser Problematik an, indem es den Feed "burnt", so dass der Feedreader seine zusätzlichen Informationen erhielt. Leider wurde die Software seit 2004 von Google nicht mehr weiterentwickelt und ist mittlerweile veraltet.


## Feedreader 2.0: Pyfeed
Pyfeed ist ein Ersatz für den originalen Feedburner und bringt einige der wichtigsten Funktionen mit einem modernen Erscheinen ins Jahr 2020. Die Webapplikation ist ein Prototyp für einen solchen Feedburner, wie dieser mit Python und Flask umgesetzt werden könnte. 

**Wichtig**: Die Pyfeed-App würde im Echteinsatz nicht funktionieren, könnte aber mit einigen Erweiterungen so angepasst werden, dass sie dies täte. So wird der Quell-RSS-Feed, welcher der Benutzer eingibt, etwa nicht regelmässige automatisch aktualisiert und neu erzeugt. Eine Funktion die für den Echteinsatz zwingend nötig wäre. Da diese Anforderung den Rahmen dieses Kurses übersteigt, wurde darauf verzichtet – auch weil es im Use Case primär um die Dateneingabe, -verarbeitung und schliesslich -ausgabe geht – welche auch ohne diese fehlende Funktionalität funktioniert. 


### Funktionsweise
Die Pyfeed-Webseite wurde in Bezug auf das UX so aufgesetzt, dass der User lediglich dem «Happy-Path» der Applikation folgen kann. Auf dem User Interface der Webseite ist vorerst die Startseite zu sehen, nach dieser folgt – falls gewünscht – die Erklärung zur Funktionsweise der App plus anschliessend die verschiedenen Eingaben:
 
* Als erstes benötigt die App eine Quell-RSS-Feedurl. Ungültige URLs (keine valide URL) oder URLs welche auf nicht RSS-Feedurls verweisen, werden vom Programm abgelehnt.
* Der User muss anschliessend im Optimieren Task die verschiedenen Parameter eintippen, welche für die Optimierung des Feeds benötigt werden. Für die Anforderungen dieser Funktionalität wurde auf diesen Blogeintrag von <a href="https://blog.feedly.com/10-ways-to-optimize-your-feed-for-feedly/" target="_blank">Feedly</a> zurückgegriffen. 
* Nach der Optimierung kann der User auf die neu generierte Endpoint URL zugreifen.


### Datenverarbeitung und -Ausgabe
Als Datenspeicherung wird ein JSON sowie je ein XML-File verwendet. In der JSON-Datei werden die bereits eingegebenen Feedurls und die neueste, optimisierte Version der dazugehörigen XML-Datei gesichert.

Die XML-Datei enthält den originalen RSS-Feed im XML-Format. Dieser wird optimisiert und mit weiteren Parametern und Metadaten ergänzt und überschrieben. Schliesslich wird die optimisierte Version des Files per Endpoint-URL dem Benutzer zur Verfügung gestellt.


### Szenarien 
Für das Projekt wurde der Programmfluss in einem Diagramm abgebildet. Auf die Unterlagen kann hier zugegriffen werden: Zu den <a href="https://example.com" target="_blank">Szenarien (LINK ÄNDERN)</a>

## Installation und Ausführung
Um das Projekt Pyfeed lokal starten zu können, sind verschiedene Abhängigkeiten vorausgesetzt. Die Requirements werden im Pipfile im Projektordner aufgeführt und können mit Hilfe von diesem File auch gleich installiert werden in der virtuellen Umgebung.

Nach Installation und dem aufsetzten und installieren der Importpakete in der virtuellen Umgebung, kann das Projekt mit <tt>flask run</tt> gestartet werden. Anschliessend ist dieses im Debug-Mode auf <tt>http://127.0.0.1:5000/</tt> erreichbar.
