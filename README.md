# Pyfeed  
Das Code Projekt wurde im Modul *«Programmierung 2»* an der Fachhochschule Graubünden umgesetzt.   

**zum Projekt**: https://pyfeed.herokuapp.com/

![Cover image and start page of pyfeed](docs/01_pyfeed.png?raw=true "Cover image pyfeed")

---

## Ausgangslage 
Fangen wir mit den Basics an. Pyfeed macht Gebrauch von der Web-Technologie <a href="https://en.wikipedia.org/wiki/RSS" target="_blank">RSS</a> (RDF Site Summary oder Really Simple Syndication). Dabei handelt es sich um einen XML-basierten Web-Feed, der es Benutzern und Anwendungen ermöglicht, auf Aktualisierungen von Websites in einem standardisierten, computerlesbaren Format zuzugreifen. Tools wie der <a href="https://feedly.com/" target="_blank">Feedly</a>-Reader ermöglichen es Benutzern, die RSS-Feeds zu verfolgen, indem sie die Feeds vieler verschiedener Websites abonnieren oder zu einem "News-Aggregator" Ihrer Wahl hinzufügen.

Kurz gesagt: RSS-Feeds sind ein großartiges Stück Technik, das leider beinahe in Vergessenheit geraten ist. Ein Schwachpunkt von RSS-Feeds ist, dass diese nicht standardisiert sind und im Feed oft Informationen fehlen, die ein Feedreader zur Anzeige Ihrer Inhalte benötigen könnte. Ursprünglich nahm sich der <a href="https://feedburner.google.com/" target="_blank">Google Feedburner</a> dieser Problematik an, indem es den Feed «burnt», so dass der Feedreader seine zusätzlichen Informationen erhielt. Leider wurde die Software seit 2004 von Google nicht mehr weiterentwickelt und ist mittlerweile veraltet.

## Feedreader 2.0: Pyfeed
Pyfeed ist ein Ersatz für den originalen Feedburner und bringt einige der wichtigsten Funktionen mit einem modernen Erscheinen ins Jahr 2020. Die Webapplikation ist ein Prototyp/Proof of Concept für einen solchen Feedburner, wie dieser mit Python und Flask umgesetzt werden könnte. 

**Wichtig**: Die Pyfeed-App würde im Echteinsatz nicht funktionieren, könnte aber mit einigen Erweiterungen so angepasst werden, dass sie dies täte. Pyfeed ist ein Proof of Concept: Der Quell-RSS-Feed, welcher der Benutzer eingibt, wird etwa nicht regelmässig automatisch aktualisiert und neu erzeugt - eine Funktion die für den Echteinsatz zwingend nötig wäre. Da diese Anforderung den Rahmen dieses Kurses übersteigt, wurde darauf verzichtet – auch weil es im Use Case primär um die Dateneingabe, -verarbeitung und schliesslich Datenausgabe geht – welche auch ohne diese fehlende Funktionalität in der App implementiert wurde. 

### Funktionsweise
Die Pyfeed-Webseite wurde in Bezug auf das UX so aufgesetzt, dass der User lediglich dem «Happy-Path» der Applikation folgen kann. Auf dem User Interface der Webseite ist vorerst die Startseite zu sehen, nach dieser folgt – falls gewünscht – die Erklärung zur Funktionsweise der App plus anschliessend die verschiedenen Eingaben:
 
* Als erstes benötigt die App eine Quell-RSS-Feedurl. Ungültige URLs (keine valide URL) oder URLs welche auf nicht RSS-Feedurls verweisen, werden vom Programm abgelehnt.
* Der User muss anschliessend im Optimieren Task die verschiedenen Parameter eintippen, welche für die Optimierung des Feeds benötigt werden. Für die Anforderungen dieser Funktionalität wurde auf diesen Blogeintrag von <a href="https://blog.feedly.com/10-ways-to-optimize-your-feed-for-feedly/" target="_blank">Feedly</a> zurückgegriffen. 
* Nach der Optimierung kann der User auf die neu generierte Endpoint URL zugreifen.

### Datenverarbeitung und -Ausgabe
Als Datenspeicherung wird ein JSON sowie je ein XML-File verwendet. In der JSON-Datei werden die bereits eingegebenen Feedurls und die neueste, optimisierte Version der dazugehörigen XML-Datei gesichert.

Die XML-Datei enthält den originalen RSS-Feed im XML-Format. Dieser wird optimisiert und mit weiteren Parametern und Metadaten ergänzt und überschrieben. Schliesslich wird die optimisierte Version des Files per Endpoint-URL dem Benutzer zur Verfügung gestellt.

### Bugs
Das Projekt enthält noch einige Bugs, welche nicht alle gefixt werden um trotzdem einen ersten MVP des Proof of Concepts zu erhalten. Die Fehler werden in erster Linie bei falschen Eingaben durch den User verursacht. Im Falle dass der User das Programm korrekt bedient, treten diese nicht ein. Die Bugs wurden als Issues im GitHub Repo festgehalten.

**zu den Issues**: <a href="https://github.com/sandromatter/PROG2/issues/" target="_blank">Issues</a>

### Szenarien 
Für das Projekt wurde der Programmfluss, bzw. die User Journey High-Level in einem Diagramm abgebildet.
Wie erwähnt ist die App so konzipiert worden, dass eine falsche Bedienung grundsätzlich ausgeschlossen ist, da Eingaben überprüft werden und falsche Pfade verboten werden.

![Diagram of the pyfeed User Journey.](docs/02_user-flowdiagram.png?raw=true "User diagram pyfeed app.")

## Installation und Ausführung
Um das Projekt Pyfeed lokal starten zu können, sind verschiedene Abhängigkeiten vorausgesetzt. Die Requirements werden im Pipfile im Projektordner aufgeführt und können mit Hilfe von diesem File installiert werden. Das Projekt wurde mit dem Python packaging tool «pipenv» aufgesetzt.

```
$ cd /{{your_path_to_directory}}/PROG2/
$ pip install pipenv
$ pipenv install
$ pipenv install --dev
$ pipenv run flask run
```

Nach Installation und dem aufsetzten und installieren der Importpakete in der virtuellen Umgebung, kann das Projekt mit <tt>flask run</tt> gestartet werden. Anschliessend ist dieses im Debug-Mode lokal auf <tt>http://127.0.0.1:5000/</tt> erreichbar.

Die Dependencies um das Projekt lokal zu testen befinden sich im Pipfile.

**[dev-packages]**
<tt>pylint</tt>
<tt>python-dotenv</tt>

**[packages]**
<tt>flask</tt>
<tt>requests</tt>
<tt>lxml</tt>
