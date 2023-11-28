# RESULTS
#### SELECT 1
```
{
  "head": {
    "vars": [
      "subject"
    ]
  },
  "results": {
    "bindings": [
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Óscar_Tabárez"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Estadio_Hernando_Siles"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Argentina_national_football_team"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Juan_Fernando_Quintero"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Rivaldo"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Newell's_Old_Boys"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Radamel_Falcao"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Lionel_Messi"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Luis_Suárez"
        }
      },
      {
        "subject": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Playmaker"
        }
      }
    ]
  }
}
```
#### SELECT 2 
```
{
  "head": {
    "vars": [
      "birthPlace",
      "birthDate"
    ]
  },
  "results": {
    "bindings": [
      {
        "birthPlace": {
          "type": "uri",
          "value": "http://dbpedia.org/resource/Lanús"
        },
        "birthDate": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#date",
          "value": "1960-10-30"
        }
      }
    ]
  }
}
```
#### CONSTRUCT 1
```
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Johan_Cruyff> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Globe_Soccer_Awards> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Copa_América> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Playmaker> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Lionel_Messi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Newell's_Old_Boys> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentina_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ronaldo_(Brazilian_footballer)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sevilla_FC> .
<http://dbpedia.org/resource/Sevilla_FC> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Diego_Maradona> .
```
#### CONSTRUCT 2
```
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/position> <http://dbpedia.org/resource/Second_striker> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/position> <http://dbpedia.org/resource/Attacking_midfielder> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/height> "1.65e0"^^<http://www.w3.org/2001/XMLSchema#double> .
```
#### ASK
```
{
  "head": {},
  "boolean": true
}
```
#### DESCRIBE
```
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Central_midfielder> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Silvio_Marzolini> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Illeists> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/years> "1995"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Playmaker> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_U-20_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/World_football_transfer_record> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1986–87_S.S.C._Napoli_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1983–84_FC_Barcelona_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/fullname> "Diego Armando Maradona"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Dubai> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Milan> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ga.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Italian_Peninsula> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Italian_Argentines> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/S.S.C._Napoli> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Uruguay_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Canadian_National_Soccer_League> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://qu.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1993_Artemio_Franchi_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Corriente_River> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/nationalgoals> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/managerclubs> <http://dbpedia.org/resource/Dorados_de_Sinaloa> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Fujairah_FC_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Armando Maradona"@eo .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Santiago_Bernabéu_Stadium> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Martin_Amis> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentina–Brazil_football_rivalry> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Armando Maradona"@ca .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Attaque_77> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Armando Maradona"@it .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona (Buenos Aires, 30 oktober 1960 – Dique Luján, 25 november 2020) was een Argentijns profvoetballer en voetbaltrainer. Hij wordt beschouwd als een van de beste voetballers ooit. Op het WK in 1986 was hij dé vedette, die Argentinië naar de wereldtitel leidde. Het Italiaanse Napoli hielp hij in 1987 aan een eerste landstitel. In 1991 werd hij bij Napoli geschorst wegens cocaïnegebruik. Op het WK van 1994 werd hij na twee wedstrijden naar huis gestuurd, nadat hij positief testte op de drug efedrine. Tussen november 2008 en juli 2010 was hij bondscoach van het Argentijns voetbalelftal."@nl .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Italian_Football_Hall_of_Fame> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:S-bef> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:UAE_Pro_League_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://am.dbpedia.org/resource/ዲየጎ_ማራዶና> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/position> <http://dbpedia.org/resource/Second_striker> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Rome> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://es.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:1990_FIFA_World_Cup_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://commons.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ml.dbpedia.org/resource/ഡീഗോ_മറഡോണ> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentina_national_football_team_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Advanced_playmaker> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_World_Youth_Championship> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Villa_Fiorito> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:FIFA_100> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Andrés_Iniesta> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1988–89_UEFA_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Arg_vs_urss_1979.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Host110187130> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/New_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona (Lanús, 30 ottobre 1960 – Tigre, 25 novembre 2020) è stato un calciatore, allenatore di calcio e dirigente sportivo argentino, di ruolo centrocampista offensivo, campione del mondo nel 1986 e vicecampione del mondo nel 1990 con la nazionale argentina. Soprannominato El Pibe de Oro (\"il ragazzo d'oro\"), è considerato uno dei più grandi calciatori di tutti i tempi. In una carriera da professionista più che ventennale militò nell'Argentinos Juniors, nel Boca Juniors, nel Barcellona, nel Napoli, nel Siviglia e nel Newell's Old Boys. Con la nazionale argentina partecipò a ben quattro Mondiali (1982, 1986, 1990 e 1994), vincendo da protagonista il torneo del 1986; i 91 incontri disputati e le 34 reti realizzate in nazionale costituirono due record, successivamente battuti. Contro l'Inghilterra ai quarti di finale di Messico 1986 segnò una rete considerata il gol del secolo, tre minuti dopo aver segnato un gol con la mano (noto come mano de Dios), altro episodio per cui è spesso ricordato. Non poté mai entrare nelle graduatorie del Pallone d'oro perché fino al 1994 il premio era riservato ai giocatori europei: per questo motivo nel 1995 vinse il Pallone d'oro alla carriera. Ha comunque ricevuto altri numerosi riconoscimenti individuali: condivise con Pelé il premio ufficiale FIFA come Miglior giocatore del XX secolo, e nel 1993 venne insignito del titolo di miglior calciatore argentino di sempre, tributatogli dalla federazione calcistica dell'Argentina. Nel 2002 fu inserito nella FIFA World Cup Dream Team, selezione formata dai migliori undici giocatori della storia dei Mondiali, ottenendo, tra gli undici della squadra ideale, il maggior numero di voti. Nel 2004 venne inserito da Pelé nel FIFA 100, la lista dei 125 migliori calciatori viventi, stilata in occasione del centenario della federazione. Nel 2012 viene premiato come Miglior Calciatore del Secolo ai Globe Soccer Awards e nel 2014 entra a far parte della Hall of Fame del calcio italiano tra i giocatori stranieri. Tra le figure più controverse e iconiche della storia dello sport per la sua personalità eccentrica e polarizzante dentro e fuori dal campo, fu sospeso due volte dal calcio giocato per uso di prodotti ad azione stimolante: una prima volta per uso di cocaina nel 1991 ed una seconda per positività ai test antidoping, al mondiale degli Stati Uniti 1994, per uso di efedrina, sostanza illegale spesso utilizzata per perdere peso. Commissario tecnico dell'Argentina per un breve periodo alla fine degli anni duemila, dopo il ritiro ufficiale dal calcio nel 1997, Maradona subì un aumento eccessivo di peso (risolto con l'aiuto di un bypass gastrico) e le conseguenze della dipendenza dalla cocaina, dalla quale si liberò dopo lunghi soggiorni in centri di disintossicazione."@it .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Parody_religion_deities> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1989–90_S.S.C._Napoli_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:World_Soccer_Magazine_World_Player_of_the_Year_winners> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Association_football_midfielders> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Is iar-imreoir agus traenálaí peile ón Airgintín é Diego Armando Maradona, a rugadh i mBuenos Aires ar an 30 Deireadh Fómhair, 1960 - 25 Samhain 2020). Bhí sé ar dhuine de na himreoirí is fearr agus is cáiliúla riamh, a d'imir le roinnt de na chlubanna is mó ar domhan agus a bhí ina chaptaen nuair a bhuaigh an fhoireann náisiúnta Corn an Domhain sa bhliain 1986.Roghnaíodh mar Imreoir an Chomórtais é, agus na rudaí a chuimhnítear is mó ná an cúl iontach a fuair sé in aghaidh Shasana, agus an cúl conspóideach \"Lámh Dé\" sa chluiche céanna."@ga .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Zlatan_Ibrahimović> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:NIG-ARG_(11).jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona (30 Oktober 1960 – 25 November 2020) yang lebih dikenal dengan sebutan Maradona adalah pemain sepak bola legendaris Argentina.Maradona menjadi pelatih timnas Argentina mulai November 2008 sampai Juli 2010. Untuk Argentina Maradona tampil sebanyak 91 kali dan mencetak 34 gol. Maradona termasuk dalam deretan pemain sepak bola terbaik abad ini bersama dengan Pele, Johan Cruyff dan Christian Vieri. Pemain yang pernah mencetak gol dengan tangan yang disebut gol tangan tuhan"@in .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_per/Maradona,%20Diego> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/deathDate> "2020-11-25"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Italy_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_passing_caniggia.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Stadio_San_Paolo> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona​ (Lanús, 30 de octubre de 1960-Dique Luján, 25 de noviembre de 2020)​ fue un futbolista y entrenador argentino. Como jugador, se desempeñó como mediocampista ofensivo o delantero, y es reconocido por numerosos especialistas,​​ exfutbolistas y personalidades internacionales​ como «uno de los mejores futbolistas en la historia».​ Asimismo, ha sido catalogado por algunos medios como el «mejor jugador en la historia de la Copa Mundial», de la cual fue designado como el mejor jugador en su edición de 1986.​ En los premios a Jugador del Siglo de la FIFA fue seleccionado como el «mejor futbolista del siglo xx» en la votación popular, obtuvo la tercera posición en la votación de los expertos seleccionados por la FIFA,​y logró la quinta ubicación en la votación realizada por la IFFHS.​ En la edición de los Premios Globe Soccer 2012 fue distinguido como el mejor «Jugador del Siglo xx».​​Por su legendaria figura en el deporte, que le valió los apodos de Pibe de Oro, así como por su personalidad extravagante, temperamental y carismática, y por su problemática vida fuera del fútbol, en donde fue suspendido por dopaje en 1991 y 1994, Maradona es considerado una de las figuras más históricas de la República Argentina, y uno de sus mayores representantes en el resto del mundo.​​​​Asimismo, su persona ha sido motivo de las más variadas referencias en la cultura popular argentina y napolitana.​​ Criado en el barrio de Villa Fiorito, Maradona fue fichado para las divisiones juveniles de Argentinos Juniors, donde pasó cinco temporadas, obteniendo el récord de ser el máximo goleador del campeonato argentino cinco veces consecutivas. En 1981, fue traspasado a Boca Juniors,​donde obtuvo el Campeonato Metropolitano, su único título en Argentina. Tras el Mundial de España de 1982, Maradona se convirtió en el primer futbolista en lograr el récord de ser el traspaso más caro del mundo dos veces, al ser transferido al Barcelona por 7,30 millones de euros, y luego al Napoli de Italia por 12 millones de euros.​En España, Diego obtendría tres títulos nacionales antes de acabar en Italia en 1984. Allí, Maradona se convirtió en una de las figuras públicas más importantes de Nápoles,​al llevar al equipo a lograr el scudetto en dos oportunidades (1987, 1990) y la Copa de la UEFA, el único título internacional de la institución. Luego de siete temporadas como napolitano, en la que acabó como el máximo goleador histórico, Maradona abandonó Italia luego de obtener su primer positivo por dopaje en la temporada 1990-91. En la etapa final de su carrera, jugó en Sevilla y Newell's Old Boys para acabar regresando a Boca Juniors en 1995 y terminar de retirarse en 1997.​ Con la Selección Argentina, Maradona fue campeón del Mundial Juvenil de 1979, y con los mayores del Mundial de México de 1986 como capitán del equipo, en la que protagonizaría una de las actuaciones individuales más destacadas de la historia del deporte,​​​al anotar los dos célebres goles que dieron la victoria a su selección en el partido contra Inglaterra en los cuartos de final, el primero de ellos conocido como «la mano de Dios» y el segundo como el «Gol del Siglo», señalado por una votación de la FIFA como el mejor en la historia de los mundiales del siglo XX.​En Italia 1990, Argentina casi repetiría la misma gesta, pero acabaría como subcampeón. Después de tres años de ausencia por sus problemas de dopaje, Maradona regresó para ayudar en la clasificación de Argentina para el Mundial de Estados Unidos de 1994, torneo en el que Diego volvería a dar positivo en drogas al encontrarse efedrina en sus muestras, siendo expulsado de la competición, lo que contribuyó a la posterior eliminación de Argentina en octavos de final.​Esta sería su última participación a nivel selecciones como jugador. Tras su retirada como futbolista, su impacto como jugador inspiró la Iglesia maradoniana, fue conductor televisivo tanto en Italia como en Argentina,​ y vicepresidente de la Comisión de Fútbol de Boca Juniors entre 2005 y 2006, antes de lanzarse en su carrera como director técnico. Tras cortas experiencias en los años 90, en octubre de 2008 Maradona fue designado como entrenador de la Selección Argentina de cara al Mundial de Sudáfrica 2010. Luego de una agónica clasificación en las Eliminatorias, en el torneo Argentina quedaría eliminada en cuartos de final ante Alemania. Posterior a su paso por la Selección, entrenó a los clubes árabes Al-Wasl y Al-Fujairah, al club mexicano de segunda división Dorados de Sinaloa, y desde 2019 y hasta su muerte en 2020 a Gimnasia y Esgrima La Plata, de la Primera División de Argentina. Además, fue presidente honorario del Dinamo Brest entre julio y septiembre de 2018.​​"@es .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Iglesia_Maradoniana> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Contestant109613191> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:South_American_Footballer_of_the_Year> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentinos_Juniors> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Expatriate_football_managers_in_the_United_Arab_Emirates> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#NaturalPerson> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1984–85_S.S.C._Napoli_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatBocaJuniorsFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Los_Angeles> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1989_Copa_América> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2006_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Serie_A_top_scorers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Pakistan_Football_Federation> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Soccer_Aid> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentinaNationalFootballTeamManagers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:FIFA_U-20_World_Cup_awards> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_television_talk_show_hosts> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Navboxes_bottom> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "دييغو أرماندو مارادونا (تلفظ بالإسبانية: ‎/ˈdjeɣo maɾaˈðona/‏؛ 30 أكتوبر 1960 – 25 نوفمبر 2020) كان لاعب ومدرب كرة قدم أرجنتيني سابق. يُعتبر على نطاق واسع أحد أعظم اللاعبين في التاريخ، وكان أحد الفائزين بالمناصفة بجائزة لاعب القرن العشرين من الفيفا. تم الجمع بين رؤية مارادونا وتمريراته ومهاراته في التحكم بالكرة والمراوغة مع قصر قامته 1.65 متر (5 قدم 5 بوصة)، مما يسمح له بالمناورة بشكل أفضل من معظم لاعبي كرة القدم الآخرين؛ غالبًا ما كان يتخطى عدة لاعبين من الخصم أثناء الجري. كان لوجوده وقيادته في الميدان تأثير كبير على الأداء العام لفريقه، في حين أنه غالبًا ما كان يتم تمييزه من قبل الخصوم. بالإضافة إلى قدراته الإبداعية، كان يمتلك حس تهديفي وكان معروفًا بأنه متخصص في الركلات الحرة. كان مارادونا موهوبًا منذ الصغر، وقد حصل على لقب «El Pibe de Oro» («الطفل الذهبي»)، وهو الاسم الذي ظل ملازمه طوال مسيرته المهنية. لعب كصانع ألعاب متقدم في المركز الكلاسيكي لصاحب الرقم 10، وهو أول لاعب في تاريخ كرة القدم يحطم الرقم القياسي العالمي لرسوم الانتقال مرتين، الأولى عندما انتقل إلى برشلونة مقابل رسوم انتقال قياسية آنذاك بلغت 5 ملايين جنيه إسترليني، والثاني عندما انتقل إلى نابولي مقابل رسوم انتقال قياسية أخرى بلغت 6.9 مليون جنيه إسترليني. لعب مع أرجنتينوس جونيورز وبوكا جونيورز وبرشلونة ونابولي وإشبيلية ونيولز أولد بويز خلال مسيرته مع الأندية، واشتهر بفترته في نابولي وبرشلونة حيث حصل على العديد من الألقاب. في مسيرته الدولية مع الأرجنتين، خاض 91 مباراة دولية وسجل 34 هدفًا. لعب مارادونا في أربع بطولات في كأس العالم، بما في ذلك كأس العالم 1986 في المكسيك حيث كان قائداً للأرجنتين وقادهم للفوز على ألمانيا الغربية في النهائي، وفاز بالكرة الذهبية كأفضل لاعب في البطولة. في ربع نهائي كأس العالم 1986، سجل كلا هدفي الفوز 2–1 على إنجلترا اللذان دخلا تاريخ كرة القدم لسببين مختلفين. الهدف الأول سجله باستخدام يده دون أن ينتبه الحكم، ويعرف بـ«يد الرب»، بينما سجل هدفه الثاني بعد جري 60 م (66 يارد) ومراوغته لخمسة لاعبين من إنجلترا، وتم التصويت على هذا الهدف ليكون «هدف القرن» من قبل المصوتين على موقع FIFA.com في عام 2002. أصبح مارادونا مدربًا للمنتخب الأرجنتيني في نوفمبر 2008. وكان مسؤولاً عن الفريق في مونديال 2010 في جنوب إفريقيا قبل أن يغادر بعد نهاية البطولة. ثم درب نادي الوصل الذي فاز في الدوري الإماراتي للمحترفين 2011–12. في عام 2017، أصبح مارادونا مدربًا للفجيرة قبل مغادرته في نهاية الموسم. في مايو 2018، تم إعلان مارادونا كرئيس جديد لنادي دينامو برست البيلاروسي. وصل إلى بريست وتم تقديمه من قبل النادي لبدء مهامه في يوليو. من سبتمبر 2018 إلى يونيو 2019، كان مارادونا مدربًا لنادي دورادوس المكسيكي. وكان مدربًا لنادي جيمناسيا لابلاتا من عام 2019 حتى وفاته في عام 2020."@ar .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__3> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Sevilla_FC_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/San_Isidro,_Buenos_Aires> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Pelé> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://af.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Diego_Maradona_celebrando_la_obtención_del_Torneo_Metropolitano_de_1981.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Textil_Mandiyú_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2005_FIFA_World_Youth_Championship> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Liquid_diet> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Amy_Winehouse> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Wikicat1982FIFAWorldCupPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Curl_(football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mar_del_Plata> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ms.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Belgium_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Catalonia_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_kempes_spain.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Golden_Ball_(FIFA)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://vec.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://scn.dbpedia.org/resource/Diegu_Armandu_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/SoccerManager> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://an.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Paolo_Maldini> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Expatriate_footballers_in_Spain> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Tottenham_Hotspur_F.C.> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentinos_Juniors_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/bg> "gold"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageExternalLink> <https://www.worldcat.org/oclc/953395867> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/image> "Maradona v lazio.jpg"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Redirect> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Jersey_number> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cocaine> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Serie_A_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Miguel_Ángel_Russo> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Asif_Kapadia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Worldcat_id> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Alicante> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Foxboro_Stadium> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Turin> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/El_Gráfico_(Argentina)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:DiegoMaradona.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ja.dbpedia.org/resource/ディエゴ・マラドーナ> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sv.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Belarus> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/manageryears> "2008"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona Franco (* 30. Oktober 1960 in Lanús; † 25. November 2020 in Tigre) war ein argentinischer Fußballspieler und -trainer. Maradona ist eine der „Legenden des Weltfußballs“ und gilt als einer der besten Fußballspieler der Geschichte. Er machte sich zu Beginn seiner Karriere bereits im Alter von 15 Jahren bei den Argentinos Juniors einen Namen, bevor er zu den Boca Juniors wechselte und 1981 argentinischer Meister wurde. Anschließend zog es den „Goldjungen“ (El Pibe de Oro) für eine Rekordablösesumme nach Europa zum FC Barcelona. Dort feierte er mit dem Pokalsieg 1983 nur einen wichtigen Titelgewinn. Von Krankheiten und Verletzungen geplagt, musste er den Verein nach nur zwei Jahren wegen zahlreicher Skandale wieder verlassen. Daraufhin schloss er sich dem SSC Neapel an, "@de .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatLivingPeople> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1978_Argentine_Primera_División> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Birth_date> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Serie_A_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Commons_category> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Luigi_de_Magistris_(politician)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://et.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/align> "right"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Los_Ratones_Paranoicos> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/PhysicalEntity100001930> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:FIFA_World_Cup_Golden_Ball> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Racing_Club_de_Avellaneda> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1983_Copa_de_la_Liga> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Charles_Dickens> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sa.dbpedia.org/resource/डियेगो_माराडोना> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Lothar_Matthäus> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Penalty_kick_(association_football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatSevillaFCFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#differentFrom> <http://dbpedia.org/resource/Madonna> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona (30 Oktober 1960 – 25 November 2020) yang lebih dikenal dengan sebutan Maradona adalah pemain sepak bola legendaris Argentina.Maradona menjadi pelatih timnas Argentina mulai November 2008 sampai Juli 2010. Untuk Argentina Maradona tampil sebanyak 91 kali dan mencetak 34 gol. Maradona termasuk dalam deretan pemain sepak bola terbaik abad ini bersama dengan Pele, Johan Cruyff dan Christian Vieri. Pemain yang pernah mencetak gol dengan tangan yang disebut gol tangan tuhan"@in .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/caps> "36"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/caps> "5"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Konex_Foundation> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/managerclubs> <http://dbpedia.org/resource/Argentina_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Convert> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/The_Champions_Promenade,_Diego_Maradona_-_panoramio.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Diego_Sinagra> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <https://global.dbpedia.org/id/iCDy> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Guillem_Balagué> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/DNA_tests> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1989–90_Serie_A> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatRacingClubDeAvellanedaManagers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/State_of_Palestine> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/BAFTA_Award> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:1984_World_Soccer_World_XI> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://cv.dbpedia.org/resource/Марадона_Диего> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://bg.dbpedia.org/resource/Диего_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/La_Noche_del_10> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Peter_Reid> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/A.C._Milan> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ben_Johnson_(Canadian_sprinter)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/The_Times> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/La_Bombonera> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Authority_control> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_100> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Eukaryote> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/image> "Maradona entrenando napoli.jpg"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__9> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_expatriates_in_Cuba> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Esquina,_Corrientes> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/url> <https://web.archive.org/web/20211010164117/https:/worldnews24daily.com/2020/11/diego-maradona-argentina-football-legend-dies-aged-60.html/amp> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Babe_Ruth> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://tl.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/nationalcaps> "15"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Wikicat2010FIFAWorldCupManagers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:MedalSport> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Stadio_Olimpico> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Rivellino> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mexico_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Maradona_by_Kusturica> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_at_Karama-1.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/youthclubs> <http://dbpedia.org/resource/Argentinos_Juniors> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/managerclubs> <http://dbpedia.org/resource/Deportivo_Riestra> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://os.dbpedia.org/resource/Марадонæ,_Диего_Армандо> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mexico_City> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Wikicat1987CopaAméricaPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Corner_kick> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Elizabeth_II> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://nl.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Obesity> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:UEFA_Cup_winning_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Newell's_Old_Boys_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/L'Équipe_Champion_of_Champions> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://yago-knowledge.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/image> "Murales en homenaje a Diego Armando Maradona en el estadio que lleva su nombre, sobre la calle Boyacá..jpg"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Swiss_franc> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1987–88_Serie_A> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://musicbrainz.org/artist/e14f6aa8-b933-40e6-bdf5-f833ecdcd61e> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Organism100004475> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Argentina_celebrando_copa_(cropped).jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Romania_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1988–89_Serie_A> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Adult109605289> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Diego_acompanado_al_antidoping.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/90min.com> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Chavista> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2020–21_UEFA_Europa_League> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "디에고 마라도나"@ko .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/Argentinos_Juniors> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/goals> "81"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/The_Washington_Post> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Gary_Lineker> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ky.dbpedia.org/resource/Диего_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/managerClub> <http://dbpedia.org/resource/Fujairah_FC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "دييغو مارادونا"@ar .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:!> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/clubs> <http://dbpedia.org/resource/Newell's_Old_Boys> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentine_Primera_División> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Miraflores_Palace> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:IFFHS_Men's_World_Team_of_the_20th_Century> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Barack_Obama> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sergio_Agüero> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Expatriate_football_managers_in_Mexico> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Queen_maradona.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Al-Wasl_F.C._managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Textil_Mandiyú> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:S.S.C._Napoli_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/FC_Barcelona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__13> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "ディエゴ・アルマンド・マラドーナ（Diego Armando Maradona, 1960年10月30日 - 2020年11月25日）は、アルゼンチン・ブエノスアイレス州ラヌース出身の元サッカー選手、サッカー指導者。ポジションはフォワードまたはミッドフィールダー。"@ja .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/National_mourning> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:FIFA_World_Cup-winning_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/IMG_(company)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:1987_Copa_América_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/International_Federation_of_Football_History_&_Statistics> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Swastika> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatPeopleFromBuenosAiresProvince> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Maradona, né le 30 octobre 1960 à Lanús (province de Buenos Aires, Argentine) et mort le 25 novembre 2020 à Tigre (province de Buenos Aires), est un footballeur international argentin devenu entraîneur. Durant sa carrière de joueur, entre 1976 et 1997, il évolue au poste de milieu offensif sous le maillot no 10. Surnommé El Pibe de Oro (Le gamin en or), il est considéré comme l'un des meilleurs joueurs de l'histoire du football. Joueur prodige des années 1980, artisan de la victoire de l'équipe d'Argentine à la Coupe du monde 1986 au Mexique, star éternelle du Napoli, il est aussi l'une des personnalités les plus controversées du sport et de la société en raison de ses relations peu recommandables à cette époque, ses nombreux dérapages verbaux, ses deux contrôles positifs en 1991 en Italie et en 1994 lors du mondial américain et de sa dépendance à la cocaïne, qui a largement perturbé sa carrière de joueur professionnel ainsi que son état de santé. Il fait partie de la FIFA 100, une liste des plus grands footballeurs vivants, publiée en 2004 pour le centenaire de la Fédération internationale de football association (FIFA), signée par Pelé, considéré comme le meilleur joueur de football du XXe siècle et fait partie de l'équipe mondiale du XXe siècle. Reconverti entraîneur, il est nommé sélectionneur de l'équipe nationale argentine le 28 octobre 2008. À l'issue de la Coupe du monde de football de 2010 au cours de laquelle l'Argentine s'incline lourdement face à l'Allemagne en quart de finale (0-4), son contrat de sélectionneur n'est pas renouvelé. Il est l'entraîneur du club argentin de Gimnasia La Plata de 2019 à 2020. Alors que sa santé décline à partir des années 2000, il meurt d'un arrêt cardiaque à son domicile de Buenos Aires, presque un mois après son soixantième anniversaire."@fr .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ne.dbpedia.org/resource/डिएगो_म्याराडोना> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://hr.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/El_Clásico> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://no.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_Primera_División_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Diego_Simeone> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Illeists> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_football_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Zinedine_Zidane> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/nationalteam> <http://dbpedia.org/resource/Argentina_national_under-20_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:The_Champions_Promenade,_Diego_Maradona_-_panoramio.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona, född 30 oktober 1960, död 25 november 2020, var en argentinsk fotbollsspelare och tränare. Maradona anses som en av de bästa fotbollsspelarna genom tiderna och av vissa som den allra bästa. När det internationella fotbollsförbundet Fifa anordnade en webbaserad omröstning år 2000 med världens fotbollsfans om vem som har varit 1900-talets bästa fotbollsspelare så blev Maradona placerad på förstaplatsen. Efter den aktiva karriären blev han fotbollstränare. Han ledde bland annat Argentinas herrlandslag i VM 2010."@sv .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/caption> "Maradona after winning the 1986 FIFA World Cup with Argentina"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/World_XI> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Medal> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://pa.dbpedia.org/resource/ਡਿਏਗੋ_ਮੈਰਾਡੋਨਾ> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1994_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Scotland_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Bolivia_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:1960_births> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hugo_Porta> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Palace_of_Westminster> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/goals> "5"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentina_international_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:FC_Barcelona_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://bn.dbpedia.org/resource/দিয়েগো_মারাদোনা> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Dorados_de_Sinaloa_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Wikicat1986FIFAWorldCupPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:1986_FIFA_World_Cup_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Apertura> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Wikicat1990FIFAWorldCupPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Barasat> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.wikidata.org/entity/Q5> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Asociación_Atlética_Argentinos_Juniors> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Corrientes_Province> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Presentacion_maradona_napoli.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://simple.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/nationalgoals> "34"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/NIG-ARG_(11).jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Squad_number_(association_football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentine_Football_Association> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Carlos_Fren> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://data.europa.eu/euodp/jrc-names/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_World_Cup_Dream_Team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:IPA-es> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/caps> "188"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://my.dbpedia.org/resource/ဒီယဲဂို_မာရာဒိုနာ> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona (ur. 30 października 1960 w Lanús, zm. 25 listopada 2020 w Tigre) – argentyński piłkarz i trener piłkarski. Nazywany także „El Diez” („Dziesiątka”) i „Pelusa” („Puszek”). Uważany za jednego z najlepszych graczy w historii tego sportu, został wybrany najlepszym zawodnikiem XX wieku (wraz z Pelém), uzyskując 53% głosów w sondzie na oficjalnej stronie FIFA. Zdobył trzecie miejsce w głosowaniu zrealizowanym przez członków Komisji Futbolowej FIFA i ludzi prenumerujących FIFA Magazine."@pl .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sourav_Ganguly> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Switzerland_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatAlWaslFCManagers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ramón_Díaz> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Association_football_forwards> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/San_Siro> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_people_of_Guaraní_descent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:See_also> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradonas's_jersey_donated_to_Pope_Francis.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sl.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Konex_Award> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Falstaff> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:1987_World_Soccer_World_XI> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_expatriate_sportspeople_in_Italy> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_expatriates_in_Cuba> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Al-Fujairah_SC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:FIFA_World_Cup_Dream_Team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/managerclubs> <http://dbpedia.org/resource/Club_de_Gimnasia_y_Esgrima_La_Plata> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/UAE_Pro-League> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Copa_América> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Expatriate_footballers_in_Spain> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_cano_debut.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentinePeopleOfCroatianDescent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatPeopleFromLomasDeZamora> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/birthDate> "1960-10-30"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Club_de_Gimnasia_y_Esgrima_La_Plata> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Tattoo> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/England_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Andrea_Pirlo> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1992–93_La_Liga> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/HNK_Rijeka> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatPeopleFromLanús> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/totalWidth> "350"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Al-Wasl_F.C.> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2020_Copa_de_la_Liga_Profesional> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/goals> "116"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Pope_John_Paul_II> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Jorge_Burruchaga> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:1982_FIFA_World_Cup_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_people_of_Basque_descent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona (30. října 1960 Lanús, Buenos Aires – 25. listopadu 2020 , Buenos Aires) byl argentinský fotbalista a trenér argentinské fotbalové reprezentace. Všeobecně je považován za jednoho z nejlepších a nejtalentovanějších světových hráčů všech dob. S národním týmem Argentiny zvítězil ve finále Mistrovství světa hráčů do 20 let 1979 v Japonsku, mistrovství světa 1986 v Mexiku a byl druhý na mistrovství světa 1990 v Itálii. Pelé ho roku 2004 zařadil mezi 125 nejlepších žijících fotbalistů."@cs .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Stadio_Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Criminal_negligence> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Juventus_F.C.> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_expatriate_sportspeople_in_the_United_Arab_Emirates> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_passing_caniggia.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://su.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/manageryears> "2018"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__7> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentinaInternationalFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/source> "—Emir Kusturica, film director"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Formation_(association_football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Diego_Maradona_celebrando_la_obtención_del_Torneo_Metropolitano_de_1981.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona (Lanús, 30 ottobre 1960 – Tigre, 25 novembre 2020) è stato un calciatore, allenatore di calcio e dirigente sportivo argentino, di ruolo centrocampista offensivo, campione del mondo nel 1986 e vicecampione del mondo nel 1990 con la nazionale argentina. Soprannominato El Pibe de Oro (\"il ragazzo d'oro\"), è considerato uno dei più grandi calciatori di tutti i tempi."@it .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:2010_FIFA_World_Cup_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/bg> "#6AB5FF"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/birthDate> "1960-10-30"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:People_from_Lomas_de_Zamora_Partido> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/managerclubs> <http://dbpedia.org/resource/Racing_Club_de_Avellaneda> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sergey_Bubka> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_squad_1994_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Death_date_and_age> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona (Lanús, 30 d'octubre de 1960 - Dique Luján, 25 de novembre de 2020) va ser un jugador i entrenador de futbol argentí. És considerat un dels millors futbolistes de la història; va ser escollit com el \"millor jugador del Món\" amb un 53,6% de vots, segons una enquesta per internet de la FIFA, la Fifa Internet Award, l'any 2000. Va debutar a l'Argentinos Juniors el 1976. Després d'unes bones actuacions, va ser traspassat al Boca Juniors, club amb el qual el 1980 va guanyar un campionat. El 1981 va ser transferit al Futbol Club Barcelona; tot i haver demostrat ser un extraordinari futbolista, primer una hepatitis, i després una greu lesió al turmell causada per una dura entrada no van permetre que tingués la continuïtat desitjada. Els esdeveniments de la Final de la Copa de l'any 1984, pels quals va ser sancionat durant uns quants mesos, i altres factors combinats, van fer que fitxés pel SSC Napoli italià, equip que no havia guanyat cap torneig des de feia temps; allà Diego hi va fer una notable actuació i va contribuir al fet que el seu equip guanyés dos Scudettos i la Copa de la UEFA (1989), entre d'altres èxits. El 1991 deixà Itàlia per anar a jugar amb el Sevilla FC i el 1993 va retornar al futbol argentí, primer amb els Newell's Old Boys i, el 1995, un altre cop pel Boca Juniors, equip amb el qual es retirà com a jugador professional el 30 d'octubre de 1997. Amb la selecció argentina va jugar quatre Copes Mundials de Futbol: la d'Espanya '82 (on van arribar als vuitens de final), Mèxic '86 (on es van proclamar campions), Itàlia '90 (on van ser subcampions) i Estats Units 94' (on va disputar només dos partits). És el cinquè màxim golejador de la selecció argentina de futbol. Com a entrenador va dirigir els equips argentins Mandiyú de Corrientes (1994) i Racing Club (1995). Aquests èxits es van veure entelats pels seus problemes amb l'addicció a les drogues que van afectar tant la seva carrera futbolística (amb suspensions imposades per diverses federacions futbolístiques), com la seva salut. A més, es va veure involucrat en uns quants fets judicials de diversa naturalesa. Va morir el 25 de novembre de 2020 a causa d'una aturada cardiorespiratòria."@ca .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Dique_Luján> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Charly_García> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Marca_Leyenda> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Goikoetxea_lesiona_maradona.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1979_South_American_U-20_Championship> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Object100002684> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/clubs> <http://dbpedia.org/resource/Argentinos_Juniors> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__5> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/position> <http://dbpedia.org/resource/Attacking_midfielder> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona (Buenos Aires, 30 oktober 1960 – Dique Luján, 25 november 2020) was een Argentijns profvoetballer en voetbaltrainer. Hij wordt beschouwd als een van de beste voetballers ooit. Op het WK in 1986 was hij dé vedette, die Argentinië naar de wereldtitel leidde. Het Italiaanse Napoli hielp hij in 1987 aan een eerste landstitel. In 1991 werd hij bij Napoli geschorst wegens cocaïnegebruik. Op het WK van 1994 werd hij na twee wedstrijden naar huis gestuurd, nadat hij positief testte op de drug efedrine. Tussen november 2008 en juli 2010 was hij bondscoach van het Argentijns voetbalelftal."@nl .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/totalWidth> "200"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentina_national_football_team_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona, (Lanús, Buenos Aires, 1960ko urriaren 30a - Tigre, Buenos Aires, 2020ko azaroaren 25a), ezizenez Pelusa, argentinar futbolari eta entrenatzailea izan zen. Historiako futbolari hoberenetako bat izan zen, hoberena aditu askoren ustetan. Bere jokalari ibilbidean Argentinos Juniors, Boca Juniors, Bartzelona, Napoli, Sevilla eta Newell's Old Boysen aritu zen. Garaipenik handienak, bi Scudetto eta UEFA Kopa bat, Napolirekin lortu zituen. Argentinako selekzioarekin 1986ko Munduko Futbol Txapelketa irabazi zuen. Denetara 91 partida jokatu zituen selekzio absolutuarekin, eta 34 gol sartu."@eu .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/manageryears> "2019"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ta.dbpedia.org/resource/டீகோ_மரடோனா> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Serie_A> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/A.S._Roma> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Дие́го Арма́ндо Марадо́на (исп. Diego Armando Maradona, испанское произношение: [ˈdjeɣo maɾaˈðona]; 30 октября 1960, Ланус — 25 ноября 2020, Дике-Лухан) — аргентинский футболист, игравший на позициях атакующего полузащитника и нападающего. Выступал за клубы «Архентинос Хуниорс», «Бока Хуниорс», «Барселона», «Наполи», «Севилья» и «Ньюэллс Олд Бойз», а также сборную Аргентины. Чемпион мира 1986 года, вице-чемпион мира 1990 года. Чемпион мира среди молодёжных команд 1979 года. Лучший игрок чемпионата мира 1986 года. Футболист года в Южной Америке 1979 и 1980 годов. Дважды член символических сборных чемпионатов мира. Чемпион Аргентины в составе клуба «Бока Хуниорс». Двукратный чемпион Италии в составе клуба «Наполи»."@ru .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Parody_religion_deities> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ronaldinho> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Miguel_Ángel_Sola> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/BBC_Radio> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_sportspeople_in_doping_cases> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Player110439851> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/nationalteam> <http://dbpedia.org/resource/Argentina_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/managerClub> <http://dbpedia.org/resource/Dorados_de_Sinaloa> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentinosJuniorsFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://fi.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona (Spanish: [ˈdjeɣo maɾaˈðona]; 30 October 1960 – 25 November 2020) was an Argentine professional football player and manager. Widely regarded as one of the greatest players in the history of the sport, he was one of the two joint winners of the FIFA Player of the 20th Century award. Maradona's vision, passing, ball control, and dribbling skills were combined with his small stature, which gave him a low centre of gravity allowing him to manoeuvre better than most other players. His presence and leadership on the field had a great effect on his team's general performance, while he would often be singled out by the opposition. In addition to his creative abilities, he possessed an eye for goal and was known to be a free kick specialist. A precocious talent, Maradona was given the nickname \"El Pibe de Oro\" (\"The Golden Boy\"), a name that stuck with him throughout his career. He also had a troubled off-field life and was banned in both 1991 and 1994 for abusing drugs. An advanced playmaker who operated in the classic number 10 position, Maradona was the first player to set the world record transfer fee twice: in 1982 when he transferred to Barcelona for £5 million, and in 1984 when he moved to Napoli for a fee of £6.9 million. He played for Argentinos Juniors, Boca Juniors, Barcelona, Napoli, Sevilla, and Newell's Old Boys during his club career, and is most famous for his time at Napoli where he won numerous accolades. In his international career with Argentina, he earned 91 caps and scored 34 goals. Maradona played in four FIFA World Cups, including the 1986 World Cup in Mexico, where he captained Argentina and led them to victory over West Germany in the final, and won the Golden Ball as the tournament's best player. In the 1986 World Cup quarter final, he scored both goals in a 2–1 victory over England that entered football history for two different reasons. The first goal was an unpenalized handling foul known as the \"Hand of God\", while the second goal followed a 60 m (66 yd) dribble past five England players, voted \"Goal of the Century\" by FIFA.com voters in 2002. Maradona became the coach of Argentina's national football team in November 2008. He was in charge of the team at the 2010 World Cup in South Africa before leaving at the end of the tournament. He then coached Dubai-based club Al Wasl in the UAE Pro-League for the 2011–12 season. In 2017, Maradona became the coach of Fujairah before leaving at the end of the season. In May 2018, Maradona was announced as the new chairman of Belarusian club Dynamo Brest. He arrived in Brest and was presented by the club to start his duties in July. From September 2018 to June 2019, Maradona was coach of Mexican club Dorados. He was the coach of Argentine Primera División club Gimnasia de La Plata from September 2019 until his death in November 2020."@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_squad_1987_Copa_América> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cameo_appearance> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Onze_d'Or> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Person100007846> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatPrimeraDivisiónArgentinaPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Club_de_Gimnasia_y_Esgrima_La_Plata_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentina_international_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/years> "1986"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/fg> "white"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1987–88_S.S.C._Napoli_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Club_de_Gimnasia_y_Esgrima_La_Plata_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/YagoLegalActor> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:1987_Copa_América_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Is iar-imreoir agus traenálaí peile ón Airgintín é Diego Armando Maradona, a rugadh i mBuenos Aires ar an 30 Deireadh Fómhair, 1960 - 25 Samhain 2020). Bhí sé ar dhuine de na himreoirí is fearr agus is cáiliúla riamh, a d'imir le roinnt de na chlubanna is mó ar domhan agus a bhí ina chaptaen nuair a bhuaigh an fhoireann náisiúnta Corn an Domhain sa bhliain 1986.Roghnaíodh mar Imreoir an Chomórtais é, agus na rudaí a chuimhnítear is mó ná an cúl iontach a fuair sé in aghaidh Shasana, agus an cúl conspóideach \"Lámh Dé\" sa chluiche céanna."@ga .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Claudio_Gentile> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://d-nb.info/gnd/11916938X> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_gol_a_inglaterra.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sportsnet> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_v_lazio.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/100_Greatest_(TV_series)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Person> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Falklands_War> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Flagicon> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/years> "1992"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1990–91_S.S.C._Napoli_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatTextilMandiyúManagers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Alberto_Fernández> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:UEFA_Europa_League_winning_captains> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Brazil_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Onze_Mondial> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Manchester_United_F.C.> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/PFF_National_Challenge_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Goikoetxea_lesiona_maradona.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://he.dbpedia.org/resource/דייגו_מראדונה> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Son_of_the_Bride> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ballon_d'Or_Dream_Team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/clubs> <http://dbpedia.org/resource/FC_Barcelona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sw.cyc.com/concept/Mx4rvofERZwpEbGdrcN5Y29ycA> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Giuseppe_Bruscolotti> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://uk.dbpedia.org/resource/Дієго_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:FC_Barcelona_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://mk.dbpedia.org/resource/Диего_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentina_national_rugby_union_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Bolivia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageLength> "243889"^^<http://www.w3.org/2001/XMLSchema#nonNegativeInteger> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/DiegoMaradona.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageID> "8485"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/managerClub> <http://dbpedia.org/resource/Deportivo_Mandiyú> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Goal_celebration> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Italian_Football_Hall_of_Fame> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Webarchive> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/fg> "navy"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/direction> "vertical"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Newell's_Old_Boys_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_World_Cup_All-Time_Team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_nationalists> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.wikidata.org/entity/Q19088> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona (ur. 30 października 1960 w Lanús, zm. 25 listopada 2020 w Tigre) – argentyński piłkarz i trener piłkarski. Nazywany także „El Diez” („Dziesiątka”) i „Pelusa” („Puszek”). Uważany za jednego z najlepszych graczy w historii tego sportu, został wybrany najlepszym zawodnikiem XX wieku (wraz z Pelém), uzyskując 53% głosów w sondzie na oficjalnej stronie FIFA. Zdobył trzecie miejsce w głosowaniu zrealizowanym przez członków Komisji Futbolowej FIFA i ludzi prenumerujących FIFA Magazine. Przez większość swojego życia Maradona zdobywał wielkie trofea zarówno z reprezentacją Argentyny, jak również z niektórymi klubami, w których grał. Z reprezentacją zdobył mistrzostwo świata w 1986, wicemistrzostwo na mundialu w 1990 i mistrzostwo na mistrzostwach świata juniorów w 1979. Najważniejsze trofea na poziomie klubowym zdobył grając w SSC Napoli, z którym zdobył Puchar UEFA oraz jedyne dwa tytuły mistrza Włoch w historii drużyny. Po zakończeniu kariery sportowej związał się z telewizją, prowadził program La Noche del 10, emitowany przez Canal 13 pod koniec 2005 roku. Był także wiceprezesem Comisión de Fútbol Atlético Boca Juniors od czerwca 2005 do sierpnia 2006 roku. Od 2008 do 2010 był selekcjonerem seniorskiej reprezentacji Argentyny, z którą wywalczył awans do Mistrzostw Świata 2010 w RPA, a w turnieju finałowym awansował do ćwierćfinału."@pl .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Animal> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:UEFA_Cup_winning_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/Sevilla_FC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/France_Football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/Newell's_Old_Boys> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_expatriate_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:1986_FIFA_World_Cup_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Arg_vs_urss_1979.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Dirty_War> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sergio_Batista> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Bruno_Giordano> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_Primera_División_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:-%22> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:FIFA_World_Cup_Winning_Captain> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:1995_South_American_Team_of_the_Year> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Diego_Maradona_series> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/UEFA_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://cy.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:1989_Copa_América_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/quote> "\"He had complete mastery of the ball. When Maradona ran with the ball or dribbled through the defence, he seemed to have the ball tied to his boots. I remember our early training sessions with him: the rest of the team were so amazed that they just stood and watched him. We all thought ourselves privileged to be witnesses of his genius.\""@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/List_of_retired_numbers_in_association_football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://wa.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/El_Cazador_de_Aventuras> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sarrià_Stadium> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Arrigo_Sacchi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1986–87_Serie_A> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sex_Pistols> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/The_hand_of_God> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:IFFHS_All-time_Men's_World_Dream_Team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ronaldo_(Brazilian_footballer)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Al-Saadi_Gaddafi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Table_football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1990_FIFA_World_Cup_Final> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:WDLtot> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Testimonial_match> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_banco_racing.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Short_description> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Criollo_people> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/title> "Awards"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ko.dbpedia.org/resource/디에고_마라도나> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Attacking_midfielder> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wordnet_type> <http://www.w3.org/2006/03/wn/wn20/instances/synset-soccer_player-noun-1> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ba.dbpedia.org/resource/Диего_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:1990_FIFA_World_Cup_Team_of_the_Tournament> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_Roman_Catholics> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Multiple_image> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/George_Best> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://th.dbpedia.org/resource/ดิเอโก_มาราโดนา> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/width> "27.0"^^<http://dbpedia.org/datatype/perCent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Steve_Cram> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://pt.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Flag_of_Argentina> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/thumbnail> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona-Mundial_86_con_la_copa.jpg?width=300> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Presentacion_maradona_napoli.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/caps> "26"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Boston> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Nigeria_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://eo.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://mn.dbpedia.org/resource/Диего_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://pl.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_y_Kirchner.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Pp-semi-indef> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Retired_numbers_in_football_(soccer)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/CONMEBOL–UEFA_Cup_of_Champions> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Exequias_de_Néstor_Kirchner_en_Casa_Rosada_7.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Rosario,_Santa_Fe> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Racing_Club_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/David_Goldblatt_(writer)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Guerin_d'Oro> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://als.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Franco_Baresi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Thing> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/nationalcaps> "91"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cap_(sport)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://li.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mar_del_Plata_Summit_of_the_Americas> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/source> "—Bryon Butler's BBC Radio commentary on Maradona's second goal against England"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sr.dbpedia.org/resource/Дијего_Армандо_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Blockquote> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Marek_Hamšík> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "迭戈·马拉多纳"@zh .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/managerclubs> <http://dbpedia.org/resource/Deportivo_Mandiyú> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona (Spanish: [ˈdjeɣo maɾaˈðona]; 30 October 1960 – 25 November 2020) was an Argentine professional football player and manager. Widely regarded as one of the greatest players in the history of the sport, he was one of the two joint winners of the FIFA Player of the 20th Century award. Maradona's vision, passing, ball control, and dribbling skills were combined with his small stature, which gave him a low centre of gravity allowing him to manoeuvre better than most other players. His presence and leadership on the field had a great effect on his team's general performance, while he would often be singled out by the opposition. In addition to his creative abilities, he possessed an eye for goal and was known to be a free kick specialist. A precocious talent, Maradona was "@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/goals> "7"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Marking_(association_football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/London> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/CausalAgent100007347> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1977_Argentine_Primera_División> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/George_W._Bush> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/El_Mundo_(Spain)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:FIFA_100> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_expatriate_sportspeople_in_the_United_Arab_Emirates> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentina_under-20_international_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Gianfranco_Zola> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/width> "28.0"^^<http://dbpedia.org/datatype/perCent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_television_talk_show_hosts> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/goals> "22"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/List_of_association_football_families> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1988–89_Coppa_Italia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FC_Barcelona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://vi.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2007_Copa_América> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_cano_debut.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Carlos_Bianchi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ballon_d'Or> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatDeifiedPeople> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ka.dbpedia.org/resource/დიეგო_მარადონა> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://war.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:La_Liga_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/South_American_Footballer_of_the_Year> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona Franco (* 30. Oktober 1960 in Lanús; † 25. November 2020 in Tigre) war ein argentinischer Fußballspieler und -trainer. Maradona ist eine der „Legenden des Weltfußballs“ und gilt als einer der besten Fußballspieler der Geschichte. Er machte sich zu Beginn seiner Karriere bereits im Alter von 15 Jahren bei den Argentinos Juniors einen Namen, bevor er zu den Boca Juniors wechselte und 1981 argentinischer Meister wurde. Anschließend zog es den „Goldjungen“ (El Pibe de Oro) für eine Rekordablösesumme nach Europa zum FC Barcelona. Dort feierte er mit dem Pokalsieg 1983 nur einen wichtigen Titelgewinn. Von Krankheiten und Verletzungen geplagt, musste er den Verein nach nur zwei Jahren wegen zahlreicher Skandale wieder verlassen. Daraufhin schloss er sich dem SSC Neapel an, erneut für eine Rekordablösesumme. Mit dem Underdog aus Kampanien, der vor seiner Ankunft dem Abstieg nahe war, feierte er zwischen 1984 und 1991 die größten Erfolge seiner Vereinskarriere, darunter 1987 und 1990 die bis heute einzigen Meistertitel der Vereinsgeschichte und den Gewinn des UEFA-Cups 1989. Der Juniorenweltmeister von 1979 führte die argentinische Nationalmannschaft 1986 in Mexiko als Mannschaftskapitän zum Gewinn ihrer zweiten Weltmeisterschaft nach 1978. Dabei erzielte der 25-Jährige beim 2:1-Sieg gegen England im Viertelfinale innerhalb von vier Minuten zwei der berühmtesten Tore der Fußballgeschichte, als er zunächst einen hohen Ball mit der Hand, der „Hand Gottes“, regelwidrig ins Tor beförderte und anschließend nach einem Dribbling über etwa 60 Meter das WM-Tor des Jahrhunderts erzielte. Insgesamt nahm Maradona an vier WM-Turnieren (1982, 1986, 1990, 1994) teil und erzielte in 91 Länderspielen 34 Tore. In den 1990er Jahren geriet Maradona wegen Drogenproblemen und Doping in die Schlagzeilen und bekam vom Fußballweltverband FIFA zweimal eine 15-monatige Sperre auferlegt. Nach seiner aktiven Karriere war Maradona als Trainer tätig, hatte aber immer wieder gesundheitliche Schwierigkeiten."@de .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ku.dbpedia.org/resource/Armando_Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://gd.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/Argentina_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Maradona_family> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1979_FIFA_World_Youth_Championship> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://lv.dbpedia.org/resource/Djego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__11> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hitachi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Guaraná_Antarctica> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Perugia_Calcio> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Andy_Warhol> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Il_Corriere_dello_Sport> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hampden_Park> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/title> "Argentina squads"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://uz.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Artemio_Franchi_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_World_Cup_awards> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Whole100003553> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/clubs> <http://dbpedia.org/resource/Boca_Juniors> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Clear> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/IFFHS_World_Team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://az.dbpedia.org/resource/Dieqo_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_messi_creacion_adan.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:FIFA_World_Cup-winning_captains> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/align> "left"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://fy.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://d-nb.info/gnd/1090234171> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageExternalLink> <https://web.archive.org/web/20211010164117/https:/worldnews24daily.com/2020/11/diego-maradona-argentina-football-legend-dies-aged-60.html/amp> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/totalWidth> "300"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentineFootballManagers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sepp_Blatter> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_gol_a_inglaterra.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:1990_FIFA_World_Cup_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cameroon_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageExternalLink> <https://worldnews24daily.com/2021/02/diego-maradona-was-addicted-alcohol-and-marijuana-cause-of-death.html> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:South_American_Team_of_the_20th_Century> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Subdural_hematoma> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Maradona_family> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Terry_Butcher> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/UNICEF> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/footer> "Maradona exhibiting his ball control in a match against Lazio  and during a training session. Michel Platini stated, \"Diego was capable of things no one else could match. The things I could do with a football, he could do with an orange.\""@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:FIFA_World_Cup-winning_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mario_Kempes> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://umbel.org/umbel/rc/PersonWithOccupation> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://lb.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_in_Russia.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona (30. října 1960 Lanús, Buenos Aires – 25. listopadu 2020 , Buenos Aires) byl argentinský fotbalista a trenér argentinské fotbalové reprezentace. Všeobecně je považován za jednoho z nejlepších a nejtalentovanějších světových hráčů všech dob. S národním týmem Argentiny zvítězil ve finále Mistrovství světa hráčů do 20 let 1979 v Japonsku, mistrovství světa 1986 v Mexiku a byl druhý na mistrovství světa 1990 v Itálii. Pelé ho roku 2004 zařadil mezi 125 nejlepších žijících fotbalistů. Byl ofenzivní hráč malého, podsaditého vzrůstu. Jeho krátké silné nohy a nízko položené těžiště mu dávaly výhodu v krátkých sprintech, navíc byl geniální v práci s míčem. Hrál zpravidla levou nohou, a to i v situacích, kdy bylo vzhledem k poloze míče zdánlivě vhodnější hrát pravačkou. Na mistrovství světa MS 1982, MS 1986, MS 1990, MS 1994 odehrál 21 zápasů a vstřelil 8 branek."@cs .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/YagoLegalActorGeo> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Gimnasia_y_Esgrima_La_Plata_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Person> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/source> "—Barcelona teammate Lobo Carrasco"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://te.dbpedia.org/resource/డియెగో_మారడోనా> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Club_Atlético_Independiente> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ur.dbpedia.org/resource/ڈیاگو_میراڈونا> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:WDL> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Haka> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/deathDate> "2020-11-25"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Doping_(sport)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:'> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/title> <http://dbpedia.org/resource/United_Press_International_Athlete_of_the_Year_Award> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/South_Korea_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Globe_Soccer_Awards> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Al_Wasl_FC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/João_Batista_da_Silva> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Waka_Waka_(This_Time_for_Africa)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_Player_of_the_Century> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Casa_Rosada> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1986–87_Coppa_Italia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/goals> "0"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Expatriate_footballers_in_Italy> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Gonzalo_Higuaín> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Expatriate_football_managers_in_Mexico> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ckb.dbpedia.org/resource/دیێگۆ_مارادۆنا> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Terry_Fenwick> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Julio_Grondona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sq.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/manageryears> "2017"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://it.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/clubs> <http://dbpedia.org/resource/S.S.C._Napoli> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/managerClub> <http://dbpedia.org/resource/Deportivo_Riestra> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Al-Wasl_F.C._managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Football_League_XI> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_expatriate_sportspeople_in_Spain> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Wikicat1994FIFAWorldCupPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Michel_Platini> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Carlos_Alberto_Torres> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Agustín_Rodríguez_Santiago> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://yo.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://www.wikidata.org/entity/Q17515> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://fr.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/nationalyears> "1977"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Free_kick_(association_football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Internal_bleeding> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://kk.dbpedia.org/resource/Диего_Армандо_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Gaza_Strip> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Doping_cases_in_association_football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Deportivo_Riestra> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Дие́го Арма́ндо Марадо́на (исп. Diego Armando Maradona, испанское произношение: [ˈdjeɣo maɾaˈðona]; 30 октября 1960, Ланус — 25 ноября 2020, Дике-Лухан) — аргентинский футболист, игравший на позициях атакующего полузащитника и нападающего. Выступал за клубы «Архентинос Хуниорс», «Бока Хуниорс», «Барселона», «Наполи», «Севилья» и «Ньюэллс Олд Бойз», а также сборную Аргентины. Чемпион мира 1986 года, вице-чемпион мира 1990 года. Чемпион мира среди молодёжных команд 1979 года. Лучший игрок чемпионата мира 1986 года. Футболист года в Южной Америке 1979 и 1980 годов. Дважды член символических сборных чемпионатов мира. Чемпион Аргентины в составе клуба «Бока Хуниорс». Двукратный чемпион Италии в составе клуба «Наполи». Лучший футболист XX века по голосованию на официальном сайте ФИФА, где он набрал 53,6 % голосов; по версии футбольной Комиссии ФИФА, Марадона — 3-й футболист в XX веке. По опросу МФФИИС занимает 5-е место среди лучших футболистов мира XX века. Занимает 2-е место среди лучших игроков XX века по версии журнала World Soccer. Занимает второе место среди лучших игроков XX века по версии журнала France Football. Занимает 2-е место среди лучших игроков XX века по версии Guerin Sportivo. Занимает 2-е место среди лучших игроков за всю историю футбола по версии журнала Placar. Является лучшим футболистом в истории чемпионатов мира по версии газеты The Times. Входит в ФИФА 100. Первый обладатель почётного «Золотого мяча». Член Зала славы итальянского футбола в номинации «лучший иностранный игрок». Член символической сборной лучших игроков на всех чемпионатах мира по версии ФИФА. Член символической сборной лучших игроков в истории Южной Америки. В 1999 году Марадона был признан лучшим спортсменом XX века в Аргентине. Автор гола в ворота сборной Англии, получившего название «Гол столетия» и признанного лучшим голом в истории чемпионатов мира; в той же игре забил мяч рукой, этот случай известен как «Рука Бога». Марадона является почётным гражданином Буэнос-Айреса и Неаполя. Именем Диего названы стадион клуба «Архентинос Хуниорс», открытый 26 декабря 2003 года в день его дебюта в составе команды, и стадион клуба «Наполи». В июне 2005 года Марадона получил премию Фаустино Сармиэнто от аргентинского сената. Спортивная карьера Марадоны оказалась сокращённой из-за наркотической зависимости, вследствие которой он был вынужден на некоторое время покинуть футбол из-за дисквалификации и лечения. Кроме этого Марадона был замешан в нескольких судебных разбирательствах, включая арест в апреле 1991 года за хранение кокаина и двухлетний условный срок, полученный им в 1999 году за стрельбу из пневматической винтовки по журналистам летом 1994 года. После завершения карьеры игрока Марадона работал телекомментатором на каналах Аргентины и Италии. С июня 2005 по август 2006 года являлся вице-президентом футбольной комиссии клуба «Бока Хуниорс». Снялся в нескольких фильмах. С октября 2008 года по июль 2010 года Марадона работал главным тренером сборной Аргентины, с которой дошёл до четвертьфинала чемпионата мира 2010 года."@ru .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Onze_Mondial_European_Footballer_of_the_Year> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_expatriate_sportspeople_in_Italy> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Association_football_midfielders> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatNewell'sOldBoysFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/url> <https://web.archive.org/web/20211010164119/https:/worldnews24daily.com/2021/02/diego-maradona-was-addicted-alcohol-and-marijuana-cause-of-death.html> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Florence> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:1979_Copa_América_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Expatriate_football_managers_in_the_United_Arab_Emirates> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://cs.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ayrton_Senna> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Rodrigo_Bueno> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://tt.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sam_Cane> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Daniel_Passarella> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1988–89_S.S.C._Napoli_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Club_Atlético_River_Plate> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/El_Salvador_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sports_Illustrated> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1982_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Soviet_Union_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://min.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Clausura> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/youthyears> "1969"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2004–05_in_Argentine_football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/SoccerPlayer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona, (Lanús, Buenos Aires, 1960ko urriaren 30a - Tigre, Buenos Aires, 2020ko azaroaren 25a), ezizenez Pelusa, argentinar futbolari eta entrenatzailea izan zen. Historiako futbolari hoberenetako bat izan zen, hoberena aditu askoren ustetan. Bere jokalari ibilbidean Argentinos Juniors, Boca Juniors, Bartzelona, Napoli, Sevilla eta Newell's Old Boysen aritu zen. Garaipenik handienak, bi Scudetto eta UEFA Kopa bat, Napolirekin lortu zituen. Argentinako selekzioarekin 1986ko Munduko Futbol Txapelketa irabazi zuen. Denetara 91 partida jokatu zituen selekzio absolutuarekin, eta 34 gol sartu. Drogamendetasunak askotan lohitu zituen haren garaipenak. 1991n, doping kontrol batean kokainarekin positiboa eman ostean, 15 hilabetez futbolean jokatu gabe egon behar izan zuen. 1994an, berriz, Munduko Futbol Txapelketatik egotzi zuten beste positibo batengatik. Futboletik erretiratu eta gero, kokaina eta alkohol kontsumoak osasun arazo larriak eragin zizkion. 2010eko Munduko Futbol Txapelketan, Argentinako selekzioa zuzendu zuen."@eu .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatTelevisionTalkShowHosts> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:FIFA_World_Cup-winning_captains> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:South_American_Footballer_of_the_Year_winners> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/UEFA_Champions_League> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cafetaleros_de_Tapachula> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sco.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Recopa_Sudamericana_2005> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Buenos_Aires> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentine_Senate> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Drug_test> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Marilyn_Monroe> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Mural_maradona_clubestrella_latablada.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "디에고 아르만도 마라도나(스페인어: Diego Armando Maradona, 1960년 10월 30일 ~ 2020년 11월 25일‏)는 아르헨티나의 전설적인 축구선수로, 현역 시절 포지션은 미드필더였다. 메시, 펠레와 함께 축구 역사상 최고의 선수로 자주 언급된다. 별명은 황금빛 소년으로 시야, 패싱력, 볼 컨트롤, 드리블, 프리킥 능력, 필드에서의 리더쉽을 가진 완벽한 공격형 미드필더이자 플레이메이커로써 시대를 풍미했다. 1980년대를 대표하는 위대한 미드필더로, 미셸 플라티니, 지쿠, 마르코 판 바스턴과 같은 기라성들 중에서도 단연 최고의 경지에 오른 선수였다. 더불어 마라도나는 알프레도 디 스테파노, 펠레와 준하거나 혹은 능가하는 평가를 받고 있으며 그에 합당한 완벽한 기량을 지닌 범시대적 위대한 선수였다. 2020년 11월 25일, 심장마비로 향년 60세의 나이에 세상을 떠났다."@ko .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Senna_(film)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__1> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.wikidata.org/entity/Q729> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando MARADONA (naskiĝis la 30-an de oktobro 1960 - mortis la 25-an de novembro 2020) estis argentina futballudisto, konsiderata unu el la plej bonkvalitaj en la tuta mondo. Li estas konata kiel el pibe de oro (la ora knabo) aŭ Pelusa (“Hararpilko” pro sia hararo). Li naskiĝis proksime de la argentina ĉefurbo Bonaero kaj komencis ludi futbalon profesie kiel 15-jaraĝa en la klubo Argentinos Juniors. En 1980 li transiris al Boca Juniors. Post unu jaro li komencis sian eŭropan karieron en la hispana FC Barcelona en Barcelono. En 1984 li translokiĝis al Napolo, Italio, kun kies teamo li gajnis du naciajn ĉampionecojn de Italio kaj fariĝis vera loka idolo. En 1992 li ludis en la teamo de Sevilo kaj poste denove en Argentino en la teamoj Newell's Old Boys kaj denove en la Boca Juniors. Liaj plej memorataj ludoj okazis kun la Argentina nacia teamo de futbalo, ĉefe en la Mondaj Ĉampionadoj de 1982, 1986, 1990 kaj 1994. Liaj du goloj en 1986 kontraŭ Anglio fariĝis festataj en la tuta lando kaj konataj en la mondo; Argentino ricevis la venkan Pokalon en tiu jaro. La unua golo kontraŭ Anglio estis farita de Maradona per pilkotuŝo de sia mano. Oni ofte parolas pri \"la mano de dio\" kiam oni parolas pri tiu golo. Post sia retiriĝo li tre ofte aperis en amaskomunikiloj, ĉefe pro siaj sanproblemoj, plejparte okazigitaj pro sia trouzo de drogoj. En la Futbala Mondpokalo 2010 li estis la trejnisto de la argentina nacia teamo. Lia morto okazis je la 25-a de novembro, malmultaj tagoj post suferi cerbinfarkton. Li estis operaciita pri tio kaj post kelkaj postoperaciaj tagoj, li suferis korinfarkton kaj ne postvivis."@eo .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Diego_Costa> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:FIFA_100> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://kn.dbpedia.org/resource/ಡಿಯೇಗೋ_ಮೆರಡೋನ> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Carlos_Bilardo> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ottavio_Bianchi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "迭戈·阿曼多·马拉多纳（西班牙語：Diego Armando Maradona，1960年10月30日－2020年11月25日），生于阿根廷布宜诺斯艾利斯，昵称“世纪球王”、“球场上帝”，阿根廷足球運動員和教練，是世界足球史上傳奇球星之一，但也是最具爭議的球員之一。 马拉多纳是足球场上极富传奇色彩且个性鲜明的“上帝”。1986年马拉多纳凭借一己之力率领阿根廷队第二次获得世界杯冠军。并成为世界杯的助攻王（8次，但由於FIFA官方正式統計世界杯助攻次數是從1986開始的，實際上球王比利四屆世界杯累計有高達10次的助攻），同时创造世界杯过人（90次），及被侵犯次数最高纪录（60次），1987年将保级球队那不勒斯成功带上意甲冠军宝座，2001年被评为世纪球王。马拉多纳可以踢前場任何位置，用左脚带球，其盤帶技術可說是舉世無雙，射門技術也是頂尖水準。 比利掛靴之後，世界各地雖有優秀球星不斷湧現，但都難以與比利比肩，直到马拉多纳的出現，因此他又被稱為「新球王」。在他1976年到1997年的职业球员生涯中，马拉多纳先后加入阿根廷青年、博卡青年、巴塞罗那、那不勒斯、塞維利亞、紐維爾舊生、博卡青年。曾获得过阿根廷甲組聯賽冠军、意大利足球甲级联赛冠军、欧洲联盟杯冠军。在阿根廷國家足球隊效力的17年（1977年－1994年）里，他还获得过世界杯冠军和世界青年足球锦标赛冠军。2001年，他被国际足联评为「20世纪最佳球员」。 2020年11月25日，患有扩张性心肌病的马拉多纳因慢性心力衰竭导致的急性肺水肿去世，享年60岁。"@zh .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Jorge_Valdano> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1983_Supercopa_de_España> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Administrator109770949> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:2020_deaths> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Retired_numbers_in_association_football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/FootballPlayer110101634> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Iraq_War> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_squad_1979_Copa_América> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "ディエゴ・マラドーナ"@ja .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/ESPN_FC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Fujairah_FC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Director110014939> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/Argentina_national_under-20_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona (Lanús, 30 d'octubre de 1960 - Dique Luján, 25 de novembre de 2020) va ser un jugador i entrenador de futbol argentí. És considerat un dels millors futbolistes de la història; va ser escollit com el \"millor jugador del Món\" amb un 53,6% de vots, segons una enquesta per internet de la FIFA, la Fifa Internet Award, l'any 2000. Com a entrenador va dirigir els equips argentins Mandiyú de Corrientes (1994) i Racing Club (1995). Va morir el 25 de novembre de 2020 a causa d'una aturada cardiorespiratòria."@ca .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Martín_Guzmán_con_Alberto_Fernández_y_Maradona.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FourFourTwo> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/VfB_Stuttgart> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Дієго Марадона"@uk .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://de.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Emir_Kusturica> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/New_Zealand_national_rugby_union_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://eu.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Boca_Juniors> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:South_American_Footballer_of_the_Year_winners> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Kolkata> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Puma_SE> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Roberto_Baggio> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1995–96_Boca_Juniors_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Germany_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Goal_of_the_Century> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_messi_creacion_adan.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Daniel_Bertoni> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ciro_Ferrara> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatSerieAFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/birthPlace> "Lanús, Argentina"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/team> <http://dbpedia.org/resource/Boca_Juniors> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_people_of_Italian_descent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Athlete109820263> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatS.S.C.NapoliPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Deified_people> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Infobox_football_biography> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Set_piece_(football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_sportspeople_in_doping_cases> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Portal> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__10> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FC_Dynamo_Brest> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/years> "1981"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Iran> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Estadio_Azteca> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1982–83_FC_Barcelona_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:1989_Copa_América_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageRevisionID> "1124729351"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_national_football_team_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_kempes_spain.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Josep_Lluís_Núñez> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Copa_del_Rey> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Exequias_de_Néstor_Kirchner_en_Casa_Rosada_7.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_expatriate_football_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/South_American_Youth_Championship> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/height> "1.65e0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/IFFHS> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentineExpatriateFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_Soccer_Aid_2.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Caniggia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentine_Footballer_of_the_Year> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hepatitis> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1993–94_Argentine_Primera_División> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Wikicat1979CopaAméricaPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://fo.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_expatriate_football_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentina_under-20_international_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:2010_FIFA_World_Cup_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Fujairah_FC_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Talleres_de_Córdoba> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ubaldo_Fillol> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/quote> "\"Even if I played for a million years, I'd never come close to Maradona. Not that I'd want to anyway. He's the greatest there's ever been.\""@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://azb.dbpedia.org/resource/دیئقو_مارادونا> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Aurelio_De_Laurentiis> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Alberto_Tarantini> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/caps> "40"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://nap.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Quote_box> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Boca_Juniors_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Czech_Republic_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/source> "— Pelé paying tribute following Maradona's death"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/BBC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#seeAlso> <http://dbpedia.org/resource/Creole_football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentinos_Juniors_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Homicide> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatExpatriateFootballersInItaly> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Ballon_d'Or_Dream_Team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hugo_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/managerClub> <http://dbpedia.org/resource/Club_de_Gimnasia_y_Esgrima_La_Plata> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1986_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__15> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "ディエゴ・アルマンド・マラドーナ（Diego Armando Maradona, 1960年10月30日 - 2020年11月25日）は、アルゼンチン・ブエノスアイレス州ラヌース出身の元サッカー選手、サッカー指導者。ポジションはフォワードまたはミッドフィールダー。"@ja .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Andreas_Brehme> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__2> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ar.dbpedia.org/resource/دييغو_مارادونا> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:S-end> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_squad_1990_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Andoni_Goikoetxea> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Kaká> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_Barcelona_shirt.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Mono> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/deathPlace> "Dique Luján, Argentina"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Puebla> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Maradona, né le 30 octobre 1960 à Lanús (province de Buenos Aires, Argentine) et mort le 25 novembre 2020 à Tigre (province de Buenos Aires), est un footballeur international argentin devenu entraîneur. Durant sa carrière de joueur, entre 1976 et 1997, il évolue au poste de milieu offensif sous le maillot no 10. Surnommé El Pibe de Oro (Le gamin en or), il est considéré comme l'un des meilleurs joueurs de l'histoire du football."@fr .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Camorra> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ephedrine> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://mg.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Use_Oxford_spelling> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona​ (Lanús, 30 de octubre de 1960-Dique Luján, 25 de noviembre de 2020)​ fue un futbolista y entrenador argentino. Como jugador, se desempeñó como mediocampista ofensivo o delantero, y es reconocido por numerosos especialistas,​​ exfutbolistas y personalidades internacionales​ como «uno de los mejores futbolistas en la historia».​ Asimismo, ha sido catalogado por algunos medios como el «mejor jugador en la historia de la Copa Mundial», de la cual fue designado como el mejor jugador en su edición de 1986.​ En los premios a Jugador del Siglo de la FIFA fue seleccionado como el «mejor futbolista del siglo xx» en la votación popular, obtuvo la tercera posición en la votación de los expertos seleccionados por la FIFA,​y logró la quinta ubicación en la votación realizada por "@es .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1979_Argentine_Primera_División> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://bs.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Dribbling> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/width> "32.0"^^<http://dbpedia.org/datatype/perCent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "디에고 아르만도 마라도나(스페인어: Diego Armando Maradona, 1960년 10월 30일 ~ 2020년 11월 25일‏)는 아르헨티나의 전설적인 축구선수로, 현역 시절 포지션은 미드필더였다. 메시, 펠레와 함께 축구 역사상 최고의 선수로 자주 언급된다. 별명은 황금빛 소년으로 시야, 패싱력, 볼 컨트롤, 드리블, 프리킥 능력, 필드에서의 리더쉽을 가진 완벽한 공격형 미드필더이자 플레이메이커로써 시대를 풍미했다. 1980년대를 대표하는 위대한 미드필더로, 미셸 플라티니, 지쿠, 마르코 판 바스턴과 같은 기라성들 중에서도 단연 최고의 경지에 오른 선수였다. 더불어 마라도나는 알프레도 디 스테파노, 펠레와 준하거나 혹은 능가하는 평가를 받고 있으며 그에 합당한 완벽한 기량을 지닌 범시대적 위대한 선수였다. 현역에서 은퇴한 후 두 차례 짧은 감독 경력을 보낸 마라도나는 2008년 10월 28일, 아르헨티나 축구 국가대표팀 감독으로 선임되었으나 전술상의 문제를 노출하며 기대를 모았던 2010년 FIFA 월드컵에서 독일에 0-4로 대패하여 준결승 진출에 실패하였다. 그럼에도 불구하고 아르헨티나 축구협회는 그를 유임하는 대신 마라도나의 밑에서 일하고 있던 코칭 스태프들을 경질하려 했다. 그런데 마라도나는 자신이 이끄는 코칭 스태프들을 배신할 수 없다며 2010년 7월 27일에 아르헨티나 축구 국가대표팀에서 사퇴했다. 그 이후 알와슬 FC의 감독이 되었으나, 계약 기간을 다 채우지 못하고 경질되었다. 2020년 11월 25일, 심장마비로 향년 60세의 나이에 세상을 떠났다."@ko .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://lt.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Sevilla_FC_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/CBC_Sports> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Buenos_Aires_Province> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:1960_births> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mike_Tyson> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hungary_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/UEFA_Europa_League> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Los_Angeles_Times> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Capocannoniere> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Head110162991> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Bella_Vista,_Buenos_Aires> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://tr.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Rabona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Spanish_Argentines> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/King_Juan_Carlos> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Lionel_Messi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Golden_Foot_Legends_Award> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://id.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__14> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ia.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Captain_(association_football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Copa_Sudamericana_2005> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://rdf.freebase.com/ns/m.02c7q> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando Maradona Franco (Lanús, 30 de outubro de 1960 — Tigre, 25 de novembro de 2020) foi um treinador e futebolista argentino que atuava como meia-atacante. Considerado um dos maiores futebolistas de todos os tempos, liderou a conquista da Copa do Mundo de 1986, marcando, nas quartas-de-final, o Gol do Século. Ele ainda disputou mais três mundiais (1982, 1990 e 1994), tendo alcançado o vice-campeonato em 1990. A Copa de 1994 ficou marcada como o ponto final da vitoriosa trajetória de Maradona pela Seleção, após ele ser apanhado no exame antidoping na partida contra a Nigéria (a segunda da Argentina no Mundial). Por conta de sua notória participação nos mundiais, em 2002 ele foi escolhido para o Time dos Sonhos das Copas do Mundo FIFA."@pt .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/image> "Mural maradona clubestrella latablada.jpg"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2019_Venezuelan_presidential_crisis> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sky_Sports> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ca.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_expatriate_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:1979_Copa_América_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@nl .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@fr .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@sv .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Doping_cases_in_association_football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@ga .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@de .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@cs .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@eu .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@pl .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@es .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@in .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Diego Maradona"@pt .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:2020_deaths> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Ballon_d'Or_Additional_Awards> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Pro_Evolution_Soccer_2018> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/title> "Olimpia de Oro"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Estadio_Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatFCBarcelonaFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Further> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:1986_FIFA_World_Cup_Team_of_the_Tournament> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Golden_Foot> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Lanús> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/position> <http://dbpedia.org/resource/Attacking_midfielder> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Distinguish> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:1993_South_American_Team_of_the_Year> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Coca-Cola> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mi_enfermedad> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:1982_FIFA_World_Cup_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Ο Ντιέγκο Αρμάντο Μαραντόνα (ισπανικά: Diego Armando Maradona, 30 Οκτωβρίου 1960 – 25 Νοεμβρίου 2020) ήταν Αργεντινός ποδοσφαιριστής και προπονητής ποδοσφαίρου. Θεωρείται ως ένας από τους κορυφαίους ποδοσφαιριστές όλων των εποχών, ενώ αρκετοί στο άθλημα και κυρίως φίλαθλοι θεωρούν το Μαραντόνα ως τον καλύτερο όλων. Στις εκλογές της IFFHS ψηφίστηκε 5ος καλύτερος ποδοσφαιριστής του 20ού αιώνα. Ακόμη, βραβεύτηκε από τη FIFA το 2000 ως ο κορυφαίος ποδοσφαιριστής του 20ού αιώνα μαζί με τον Πελέ."@el .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Michael_Jordan> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Left-wing_politics> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Alcohol_abuse> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_squad_2010_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Ντιέγκο Μαραντόνα"@el .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_Primera_División_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1984_Copa_del_Rey_Final> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/César_Luis_Menotti> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/years> "1982"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Juan_José_Jiménez_Collar> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Copa_de_la_Liga> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Che_Guevara> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1989_UEFA_Cup_Final> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://io.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:S.S.C._Napoli_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentina_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/L'Équipe> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://gl.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatPeopleConvictedOfDrugOffenses> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Superclásico> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:People_convicted_of_drug_offenses> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentinePeopleOfItalianDescent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradonas's_jersey_donated_to_Pope_Francis.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_expatriate_sportspeople_in_Spain> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatExpatriateFootballersInSpain> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Greece_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Cite_book> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <https://data.globalnewsgraph.org/gng/person/diego-maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/managerclubs> <http://dbpedia.org/resource/Al-Wasl_F.C.> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/name> "Diego Armando Maradona"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_expatriate_sportspeople_in_Mexico> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Dorados_de_Sinaloa_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageExternalLink> <https://worldnews24daily.com/2020/11/diego-maradona-argentina-football-legend-dies-aged-60.html/amp> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sh.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__8> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/footer> "Left: Maradona sitting on the bench during his debut coaching Racing Club in a preseason match against Independiente, January 1995. Right: greeting fans after being appointed manager of Dubai club Al Wasl of UAE in 2011"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Gabriel_Batistuta> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/years> "1993"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_Barcelona_shirt.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2014_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://da.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Argentina_celebrando_copa_(cropped).jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Steve_Hodge> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Manu_Chao> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Imperialism> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "迭戈·阿曼多·马拉多纳（西班牙語：Diego Armando Maradona，1960年10月30日－2020年11月25日），生于阿根廷布宜诺斯艾利斯，昵称“世纪球王”、“球场上帝”，阿根廷足球運動員和教練，是世界足球史上傳奇球星之一，但也是最具爭議的球員之一。 马拉多纳是足球场上极富传奇色彩且个性鲜明的“上帝”。1986年马拉多纳凭借一己之力率领阿根廷队第二次获得世界杯冠军。并成为世界杯的助攻王（8次，但由於FIFA官方正式統計世界杯助攻次數是從1986開始的，實際上球王比利四屆世界杯累計有高達10次的助攻），同时创造世界杯过人（90次），及被侵犯次数最高纪录（60次），1987年将保级球队那不勒斯成功带上意甲冠军宝座，2001年被评为世纪球王。马拉多纳可以踢前場任何位置，用左脚带球，其盤帶技術可說是舉世無雙，射門技術也是頂尖水準。 2020年11月25日，患有扩张性心肌病的马拉多纳因慢性心力衰竭导致的急性肺水肿去世，享年60岁。"@zh .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1958_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Gastric_bypass_surgery> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/totalgoals> "259"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2018_Venezuelan_presidential_election> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Toronto_Italia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_in_Russia.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Osvaldo_Ardiles> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:World_Team_of_the_20th_century> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Use_dmy_dates> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://pnb.dbpedia.org/resource/ڈیاگو_میراڈونا> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Supercopa_de_España> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:People_convicted_of_drug_offenses> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Roberto_Durán> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/UEFA> .
<http://dbpedia.org/resource/Diego_Maradona> <http://schema.org/sameAs> <http://viaf.org/viaf/34444144> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Naples> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Shakira> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Racing_Club_de_Avellaneda_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Reflist> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://la.dbpedia.org/resource/Didacus_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/isPrimaryTopicOf> <http://en.wikipedia.org/wiki/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_people_of_Guaraní_descent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Diego Armando MARADONA (naskiĝis la 30-an de oktobro 1960 - mortis la 25-an de novembro 2020) estis argentina futballudisto, konsiderata unu el la plej bonkvalitaj en la tuta mondo. Li estas konata kiel el pibe de oro (la ora knabo) aŭ Pelusa (“Hararpilko” pro sia hararo). Li naskiĝis proksime de la argentina ĉefurbo Bonaero kaj komencis ludi futbalon profesie kiel 15-jaraĝa en la klubo Argentinos Juniors. En 1980 li transiris al Boca Juniors. Post sia retiriĝo li tre ofte aperis en amaskomunikiloj, ĉefe pro siaj sanproblemoj, plejparte okazigitaj pro sia trouzo de drogoj."@eo .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://jv.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentineFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_squad_1982_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Peter_Shilton> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_entrenando_napoli.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Real_Madrid_CF> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Newell's_Old_Boys> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.wikidata.org/entity/Q628099> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/date> "2021-10-10"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Guerin_Sportivo> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentina_v_England_(1986_FIFA_World_Cup)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/CA_Osasuna> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2010_FIFA_World_Cup_qualification_(CONMEBOL)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Diego_Maradona_at_Mexico_86_(Panini_Supersport).jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:S-start> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Nutmeg_(association_football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/US_Dollar> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2010_FIFA_World_Cup_team_rankings> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1985–86_S.S.C._Napoli_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Camp_Nou> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/World_Team_of_the_20th_Century> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/clubs> <http://dbpedia.org/resource/Sevilla_FC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/position> <http://dbpedia.org/resource/Second_striker> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1990_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Supercoppa_Italiana> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1996–97_Club_Atlético_Boca_Juniors_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://fa.dbpedia.org/resource/دیگو_مارادونا> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/United_Press_International_Athlete_of_the_Year_Award> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hernán_López_(footballer)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/managerClub> <http://dbpedia.org/resource/Al-Wasl_F.C.> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/Person/height> "165.0"^^<http://dbpedia.org/datatype/centimetre> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/manageryears> "1995"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Sportspeople_from_Lanús> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_nationalists> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/bordercolor> "black"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Diego_Maradona_(film)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/CONMEBOL> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Association_football_forwards> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Argentina_v_belgica_1986.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:S-ach> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://nn.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Villa_miseria> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/image> "Maradona banco racing.jpg"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:ARG> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Johan_Cruyff> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/image> "Maradona at Karama-1.JPG"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_people_of_Italian_descent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageExternalLink> <https://web.archive.org/web/20211010164119/https:/worldnews24daily.com/2021/02/diego-maradona-was-addicted-alcohol-and-marijuana-cause-of-death.html> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/S.S.C._Napoli> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/El_País_(Uruguay)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Navboxes_top> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:S-aft> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_expatriate_sportspeople_in_Mexico> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sk.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Glenn_Hoddle> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Yugoslavia_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_y_Kirchner.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://be.dbpedia.org/resource/Дыега_Арманда_Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Metabolism> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Amy_(2015_film)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:UAE_Pro_League_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Diego_Maradona_at_Mexico_86_(Panini_Supersport).jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://el.dbpedia.org/resource/Ντιέγκο_Μαραντόνα> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Academy_Awards> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/source> "—Lionel Messi, the player most closely identified with the \"New Maradona\" label"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_people_of_Basque_descent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.wikidata.org/entity/Q215627> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__12> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:La_Liga_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Pope_Francis> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Corriere_dello_Sport_–_Stadio> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/height> "1.65 m"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Fidel_Castro> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Aló_Presidente> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ministry_of_Foreign_Affairs_(Iran)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Coppa_Italia_top_scorers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Coppa_Italia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Juan_Domingo_Cabrera> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mano_Negra_(band)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2020_AFC_Champions_League> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cardiac_arrest> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://sw.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/totalcaps> "491"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Expatriate_footballers_in_Italy> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_squad_1989_Copa_América> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentina_youth_international_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Diego_acompanado_al_antidoping.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_Soccer_Aid_2.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/quote> "\"I have lost a great friend and the world has lost a legend. There's still so much to be said, but for now, may God give strength to his relatives. One day I hope we can play football together in heaven.\""@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:World_Soccer_Magazine_World_Player_of_the_Year_winners> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Argentina_national_under-20_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ast.dbpedia.org/resource/Diego_Armando_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Al_Wasl_FC_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://hi.dbpedia.org/resource/डिएगो_माराडोना> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/deathPlace> <http://dbpedia.org/resource/Dique_Luján> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatLaLigaFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Species> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://zh.dbpedia.org/resource/迭戈·马拉多纳> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1997–98_Club_Atlético_Boca_Juniors_season> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Copa_América_Historcial_Dream_Team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Paolo_Rossi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Inter_Milan> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Association_football> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/La_Liga> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona Franco (Lanús, 30 de outubro de 1960 — Tigre, 25 de novembro de 2020) foi um treinador e futebolista argentino que atuava como meia-atacante. Considerado um dos maiores futebolistas de todos os tempos, liderou a conquista da Copa do Mundo de 1986, marcando, nas quartas-de-final, o Gol do Século. Ele ainda disputou mais três mundiais (1982, 1990 e 1994), tendo alcançado o vice-campeonato em 1990. A Copa de 1994 ficou marcada como o ponto final da vitoriosa trajetória de Maradona pela Seleção, após ele ser apanhado no exame antidoping na partida contra a Nigéria (a segunda da Argentina no Mundial). Por conta de sua notória participação nos mundiais, em 2002 ele foi escolhido para o Time dos Sonhos das Copas do Mundo FIFA. Amplamente considerado um dos maiores, mais famosos e mais polêmicos jogadores do século XX, diversas personalidades e organizações reconheceram-no como um dos melhores jogadores da história do futebol e dos mundiais. Na votação do Melhor Jogador do Século XX pela FIFA, realizada em dezembro de 2000, ele ficou na primeira posição da votação popular, e em terceiro na votação dos especialistas selecionados pela FIFA. Neste mesmo ano, ele foi eleito o quinto melhor jogador da história pelo IFFHS. Enquanto jogador, Maradona foi reverenciado como uma divindade em seu país natal, sendo criada inclusive uma igreja dedicada a ele. Seu maior momento foi na Copa do Mundo de 1986 que, na opinião popular, foi ganha sozinha por El Pibe de Oro, outra de suas muitas alcunhas. Nesta Copa, que ficou conhecida como \"A Copa do Maradona\", Dieguito teve influência direta em 71% dos 14 gols anotados pela Argentina na campanha do título (ele marcou cinco tentos e deu cinco assistências para gols), sendo a maior porcentagem individual da história das Copas. Internacionalmente, Maradona também consagrou-se como herói da equipe italiana do Napoli, um clube que, embora tradicional, esteve entre os pequenos do país. Com El Diez, o Napoli viveu momentos de glória no final da década de 1980, ganhando seus dois únicos títulos no Campeonato Italiano e lutando de igual para igual com as maiores equipes do país. Além disso, Maradona foi o primeiro jogador na história do futebol a estabelecer duas vezes o recorde mundial de transferência mais cara: primeiro, quando foi transferido para o Barcelona por um recorde mundial de 5 milhões de euros, e o segundo quando foi transferido para o Napoli pelo valor recorde de 6,9 milhões de euros. A carreira de Maradona, porém, foi cercada de controvérsias, que não se limitaram aos gramados. Algumas delas estão relacionadas ao seu abuso de drogas, vício que levou ao seu banimento dos gramados por duas ocasiões, em 1991 e 1994. Teve também dois filhos fora do casamento que não reconheceu como seus. E rotineiramente fazia declarações contra os bastidores da FIFA, principalmente aos dirigentes João Havelange, Joseph Blatter, Michel Platini, Franz Beckenbauer, além de Pelé, e também tem um histórico de atritos com imprensas, incluindo a de seu próprio país. Morreu aos sessenta anos de idade, na sua residência em Tigre, vítima de uma parada cardiorrespiratória."@pt .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://hu.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/birthPlace> <http://dbpedia.org/resource/Lanús> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__6> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/quote> "\"I asked myself, 'Who is this man? Who is this footballing magician, this Sex Pistol of international football, this cocaine victim who kicked the habit, looked like Falstaff and was as weak as spaghetti?' If Andy Warhol had still been alive, he would have definitely put Maradona alongside Marilyn Monroe and Mao Tse-tung. I'm convinced that if he hadn’t been a footballer, he'd've become a revolutionary.\""@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Evo_Morales> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1986_FIFA_World_Cup_Final> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://is.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Olimpia_Award> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hugo_Chávez> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Tartan_Army> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Olympique_de_Marseille> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/El_camino_de_San_Diego> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentine_Primera_División_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1976_Argentine_Primera_División> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Nicolás_Maduro> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/LivingThing100004258> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Louis_Vuitton> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Footballer_of_the_Year_of_Argentina> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Standard-Examiner> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona-Mundial_86_con_la_copa.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/goals> "28"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Live_Is_Life> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Fujairah_FC_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Wikiquote> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:MedalCompetition> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Vatican_City> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Air_rifle> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Deified_people> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Latin_Americans> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Spnd> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://tg.dbpedia.org/resource/Марадона> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://arz.dbpedia.org/resource/دييغو_مارادونا> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/manageryears> "2013"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Basque_Argentines> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:People_from_Lomas_de_Zamora_Partido> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Argentina_v_belgica_1986.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentinaYouthInternationalFootballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Diego Armando Maradona, född 30 oktober 1960, död 25 november 2020, var en argentinsk fotbollsspelare och tränare. Maradona anses som en av de bästa fotbollsspelarna genom tiderna och av vissa som den allra bästa. När det internationella fotbollsförbundet Fifa anordnade en webbaserad omröstning år 2000 med världens fotbollsfans om vem som har varit 1900-talets bästa fotbollsspelare så blev Maradona placerad på förstaplatsen. Maradonas främsta merit var hans VM-guld med Argentina i VM 1986 där han blev utnämnd till turneringens bästa spelare. Under sin landslagskarriär spelade han i fyra VM-slutspel, 91 landskamper och gjorde 34 mål. Största delen av hans klubblagskarriär tillbringades i Boca Juniors, Barcelona och Napoli. År 1987 och 1990 blev han italiensk mästare med Napoli. Under sin tid i klubben från 1984 till 1991 spelade han 259 matcher och gjorde 115 mål. Maradonas spelstil kännetecknades av en otrolig teknik och spelförståelse. Han var bara 1,66 m lång och med sin låga tyngdpunkt kunde han dribbla förbi spelare med bollen klistrad vid fötterna. Han var också känd för sin karisma och sin förmåga att höja sina medspelares prestationer. Efter den aktiva karriären blev han fotbollstränare. Han ledde bland annat Argentinas herrlandslag i VM 2010. Maradona avled i november 2020 efter en längre tids hälsoproblem. Efter hans död beslutade Argentinas president om att landet skulle ha tre dagars landssorg. Napolis hemmaarena bytte namn från San Paolo-stadion till Diego Armando Maradona-stadion efter hans död."@sv .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__17> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__4> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/years> "1976"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/caps> "166"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Guaraní_people> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_Roman_Catholics> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/manageryears> "1994"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Francisco_José_Carrasco> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1979_Copa_América> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Giuseppe_Bergomi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Ali_Bin_Nasser> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:S-ttl> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Lying_in_state> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_squad_1986_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://hy.dbpedia.org/resource/Դիեգո_Մարադոնա> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Raúl_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1990_Supercoppa_Italiana> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/List_of_Argentine_Primera_División_top_scorers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Boca_Juniors_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Claudio_Caniggia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1980_Argentine_Primera_División> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/The_Guardian> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Priest> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Cvt> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cuba> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Racing_Club_de_Avellaneda_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Sportspeople_from_Lanús> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Leader109623038> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/UAE_First_Division_League> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2010_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Careca> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/United_Arab_Emirates> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:1994_FIFA_World_Cup_players> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Діє́го Арма́ндо Марадо́на (ісп. Diego Armando Maradona; 30 жовтня 1960, Ланус, Буенос-Айрес, Аргентина — 25 листопада 2020, , Буенос-Айрес, Аргентина) — аргентинський футболіст, один з найвідоміших і найкращих гравців в історії футболу. По завершенні кар'єри гравця — футбольний тренер і функціонер, телекоментатор. Грав на позиціях атакувального півзахисника і нападника. Виступав за клуби «Архентінос Хуніорс», «Бока Хуніорс», «Барселона», «Наполі», «Севілья» і «Ньюеллс Олд Бойз». Провів 91 матч і забив 34 голи у складі збірної Аргентини. Чемпіон світу 1986 року. Віце-чемпіон світу 1990 року. Учасник чотирьох чемпіонатів світу. Чемпіон світу серед молодіжних команд 1979 року. Найкращий гравець чемпіонату світу 1986 року. Футболіст року в Південній Америці 1979 і 1980 років. Двічі входив до символічних збірних чемпіонатів світу. Чемпіон Аргентини у складі клубу «Бока Хуніорс». Дворазовий чемпіон Італії, а також володар Кубка УЄФА у складі клубу «Наполі». Найкращий бомбардир Чемпіонату Аргентини з футболу (1979, 1980 та 1981 роки) та Чемпіонату Італії з футболу (1989 рік). за результатами голосування на офіційному сайті ФІФА, де набрав 53,6 % голосів; за версією футбольної Комісії ФІФА, Марадона — 3-й футболіст у XX столітті. Серед найкращих футболістів світу XX століття: за опитуванням IFFHS посідає 5-те місце, за версією журналу World Soccer — 2-ге місце, за версією журналу France Football — 2-ге місце. Є найкращим футболістом в історії чемпіонатів світу за версією газети Таймс. Перший володар почесного «Золотого м'яча». Член Зали слави італійського футболу в номінації «найкращий іноземний гравець». Член символічної збірної найкращих гравців на всіх чемпіонатах світу за версією ФІФА. Член символічної збірної найкращих гравців в історії Південної Америки. 1999 року Марадону визнано найкращим спортсменом XX століття в Аргентині. Автор голу у ворота збірної Англії, який дістав назву «Гол століття», визнаного найкращим в історії чемпіонатів світу; в тій самій грі забив м'яч рукою, цей випадок відомий як «Рука Бога». Спортивна кар'єра Марадони виявилася короткою через наркотичну залежність, унаслідок якої він був змушений на деякий час покидати футбол через дискваліфікацію і лікування. Окрім цього Марадона був замішаний у декількох судових розглядах, включаючи арешт у квітні 1991 року за зберігання кокаїну і дворічний умовний строк, який він отримав 1999 року за стрілянину з пневматичної гвинтівки по журналістах улітку 1994 року. Працював телекоментатором на каналах Аргентини й Італії. Із червня 2005 по серпень 2006 року — віцепрезидент футбольної комісії клубу «Бока Хуніорс». Знявся в декількох фільмах. Від жовтня 2008 року до липня 2010 року Марадона працював головним тренером збірної Аргентини, з якою дійшов до чвертьфіналу чемпіонату світу 2010."@uk .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Murales_en_homenaje_a_Diego_Armando_Maradona_en_el_estadio_que_lleva_su_nombre,_sobre_la_calle_Boyacá..jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://viaf.org/viaf/34444144> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://mzn.dbpedia.org/resource/دیگو_مارادونا> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/ns/prov#wasDerivedFrom> <http://en.wikipedia.org/wiki/Diego_Maradona?oldid=1124729351&ns=0> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_torneos_evita.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cubans> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__18> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Gabriela_Sabatini> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/careerStation> <http://dbpedia.org/resource/Diego_Maradona__CareerStation__16> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://data.bibliotheken.nl/id/thes/p075100878> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/quote> "\"Maradona, turns like a little eel and comes away from trouble, little squat man... comes inside Butcher and leaves him for dead, outside Fenwick and leaves him for dead, and puts the ball away... and that is why Maradona is the greatest player in the world.\""@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Dorados_de_Sinaloa_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Textil_Mandiyú_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:Argentina_youth_international_footballers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Sevilla_FC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#label> "Марадона, Диего Армандо"@ru .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_torneos_evita.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Assist_(association_football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ro.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://mr.dbpedia.org/resource/दिएगो_मारादोना> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://umbel.org/umbel/rc/SoccerCoach> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Peter_Beardsley> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://br.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Direct_free_kick> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://oc.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Queen_maradona.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Rudi_Völler> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1978_FIFA_World_Cup> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Barcelona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatPeopleFromBuenosAires> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/caps> "30"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/manageryears> "2011"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Glasgow> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatArgentinePeopleOfIndigenousPeoplesDescent> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/World_Soccer_(magazine)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "Діє́го Арма́ндо Марадо́на (ісп. Diego Armando Maradona; 30 жовтня 1960, Ланус, Буенос-Айрес, Аргентина — 25 листопада 2020, , Буенос-Айрес, Аргентина) — аргентинський футболіст, один з найвідоміших і найкращих гравців в історії футболу. По завершенні кар'єри гравця — футбольний тренер і функціонер, телекоментатор. Грав на позиціях атакувального півзахисника і нападника. Виступав за клуби «Архентінос Хуніорс», «Бока Хуніорс», «Барселона», «Наполі», «Севілья» і «Ньюеллс Олд Бойз». Провів 91 матч і забив 34 голи у складі збірної Аргентини."@uk .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/SportsManager> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/managerClub> <http://dbpedia.org/resource/Argentina_national_football_team> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Dummy_(football)> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/footer> "Murals of Maradona in Buenos Aires, created following his death"@en .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Parody_religion> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Deportivo_Mandiyú> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/wikiPageUsesTemplate> <http://dbpedia.org/resource/Template:Argentina_Primera_Division_top_scorers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/title> <http://dbpedia.org/resource/L'Équipe_Champion_of_Champions> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/La_Plata> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/linguistics/gold/hypernym> <http://dbpedia.org/resource/Footballer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Cartagena_de_Indias> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Dorados_de_Sinaloa> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Caracas> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/WikicatExpatriateFootballManagersInTheUnitedArabEmirates> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://vo.dbpedia.org/resource/Diego_Maradona> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Mao_Tse-tung> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Catholic_Church_in_Argentina> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/class/yago/Wikicat1989CopaAméricaPlayers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Andrés_Calamaro> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/years> "1984"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Athletic_Bilbao> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1982–83_Copa_del_Rey> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Estadio_Olímpico_Universitario> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2000/01/rdf-schema#comment> "دييغو أرماندو مارادونا (تلفظ بالإسبانية: ‎/ˈdjeɣo maɾaˈðona/‏؛ 30 أكتوبر 1960 – 25 نوفمبر 2020) كان لاعب ومدرب كرة قدم أرجنتيني سابق. يُعتبر على نطاق واسع أحد أعظم اللاعبين في التاريخ، وكان أحد الفائزين بالمناصفة بجائزة لاعب القرن العشرين من الفيفا. تم الجمع بين رؤية مارادونا وتمريراته ومهاراته في التحكم بالكرة والمراوغة مع قصر قامته 1.65 متر (5 قدم 5 بوصة)، مما يسمح له بالمناورة بشكل أفضل من معظم لاعبي كرة القدم الآخرين؛ غالبًا ما كان يتخطى عدة لاعبين من الخصم أثناء الجري. كان لوجوده وقيادته في الميدان تأثير كبير على الأداء العام لفريقه، في حين أنه غالبًا ما كان يتم تمييزه من قبل الخصوم. بالإضافة إلى قدراته الإبداعية، كان يمتلك حس تهديفي وكان معروفًا بأنه متخصص في الركلات الحرة. كان مارادونا موهوبًا منذ الصغر، وقد حصل على لقب «El Pibe de Oro» («الطفل الذهبي»)، وهو الاسم الذي ظل ملازمه طوا"@ar .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hokey_Cokey> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/property/managerclubs> <http://dbpedia.org/resource/Fujairah_FC> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Second_striker> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Martín_Guzmán_con_Alberto_Fernández_y_Maradona.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Santos_Laciar> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/1981_Argentine_Primera_División> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/FIFA_18> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Muammar_Gaddafi> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/2014_Israel–Gaza_conflict> .
<http://dbpedia.org/resource/Diego_Maradona> <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:Argentine_football_managers> .
<http://dbpedia.org/resource/Diego_Maradona> <http://xmlns.com/foaf/0.1/depiction> <http://commons.wikimedia.org/wiki/Special:FilePath/Maradona_CRS.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/abstract> "Ο Ντιέγκο Αρμάντο Μαραντόνα (ισπανικά: Diego Armando Maradona, 30 Οκτωβρίου 1960 – 25 Νοεμβρίου 2020) ήταν Αργεντινός ποδοσφαιριστής και προπονητής ποδοσφαίρου. Θεωρείται ως ένας από τους κορυφαίους ποδοσφαιριστές όλων των εποχών, ενώ αρκετοί στο άθλημα και κυρίως φίλαθλοι θεωρούν το Μαραντόνα ως τον καλύτερο όλων. Στις εκλογές της IFFHS ψηφίστηκε 5ος καλύτερος ποδοσφαιριστής του 20ού αιώνα. Ακόμη, βραβεύτηκε από τη FIFA το 2000 ως ο κορυφαίος ποδοσφαιριστής του 20ού αιώνα μαζί με τον Πελέ. Υπήρξε ο πρώτος ποδοσφαιριστής στην ιστορία του αθλήματος που κατέρριψε το ρεκόρ της πιο ακριβής μεταγραφής δύο φορές, την πρώτη όταν έπαιξε στη Μπαρτσελόνα για τρία εκατομμύρια αγγλικές λίρες και τη δεύτερη, όταν αγωνίστηκε στη Νάπολι για πέντε εκατομμύρια λίρες. Είχε αγωνιστεί στους Αρχεντίνος Τζούνιορς, Μπόκα Τζούνιορς, Μπαρτσελόνα, Νάπολι, Σεβίλλη και στο τέλος της καριέρας του, στη Νιούελς Ολντ Μπόις και τελικά μετά από παύση ενός έτους από το ποδόσφαιρο έκλεισε την καριέρα του στην αγαπημένη του Μπόκα Τζούνιορς το 1997. Τα πιο ένδοξα ποδοσφαιρικά του χρόνια τα πέρασε στη Νάπολι, όπου κέρδισε τίτλους και διακρίσεις. Στην καριέρα του με την Εθνική Αργεντινής, σημείωσε 34 τέρματα σε 91 εμφανίσεις. Αν και ξεκίνησε την καριέρα του ως επιθετικός, καθιερώθηκε ως επιθετικός μέσος. Η διεισδυτικότητα του Μαραντόνα, η εφευρετικότητα, οι πάσες του, οι εντυπωσιακές τεχνικές του ικανότητες, η ταχύτητα, τα αντανακλαστικά και ο χρόνος αντίδρασης συνδυάστηκαν με το μικρό του ανάστημα (1,65 μέτρα). Το χαμηλό κέντρο βάρους τον βοηθούσε στην κατοχή και τον χειρισμό της μπάλας. Γοήτευσε τους οπαδούς σε όλο τον κόσμο σε μια καριέρα δύο δεκαετιών με ένα μαγευτικό τρόπο παιχνιδιού που ήταν καθαρά δικό του. Η παρουσία του στο γήπεδο είχε μεγάλη επίδραση στη γενική απόδοση της ομάδας του. Βάσει του απαράμιλλου ταλέντου του και των ηγετικών του ικανοτήτων, έλαβε το προσωνύμιο El Pibe de Oro (Το Χρυσό Αγόρι). Εξαιρετικά ιδιοφυής, ο αγώνας του Μαραντόνα με τον εθισμό στα ναρκωτικά και το αλκοόλ αμαύρωσε την καριέρα του, αλλά με όλες τις αδυναμίες του, γοήτευσε τους φίλους του αθλήματος για δύο δεκαετίες με τον τρόπο παιχνιδιού του και είναι ευρέως σεβαστός έχοντας προσφέρει στο άθλημα μερικές από τις πιο αξέχαστες στιγμές του. Έλαβε μέρος σε τέσσερα Παγκόσμια Κύπελλα, συμπεριλαμβανομένου του Παγκοσμίου Κυπέλλου του 1986 στο Μεξικό, όπου έλαμψε η χαρισματική προσωπικότητά του και οδήγησε την ομάδα του στην κατάκτηση του τροπαίου με νίκη επί της Δυτικής Γερμανίας στον τελικό. Επίσης κέρδισε τη Χρυσή Μπάλα ως ο καλύτερος παίκτης της διοργάνωσης. Στον προ-ημιτελικό απέναντι στην Αγγλία, πέτυχε δύο γκολ, στη νίκη της ομάδας του με 2–1 που γράφτηκε στην ιστορία για δύο διαφορετικούς, μοναδικούς λόγους. Το πρώτο γκολ επιτεύχθηκε με χέρι του Μαραντόνα, γνωστό ως «Χέρι του Θεού», ενώ το δεύτερο υπήρξε προϊόν εκπληκτικής ατομικής προσπάθειας που ξεκίνησε πίσω από το κέντρο του γηπέδου. Αυτό το γκολ, καταγράφηκε ως το «Γκολ του αιώνα» από τους ψηφοφόρους της FIFA το 2002. Το 1998 η FIFA τον εξέλεξε στην καλύτερη ενδεκάδα του 20ού αιώνα. Έγινε προπονητής της Εθνικής Αργεντινής τον Νοέμβριο του 2008, έχοντας την ευθύνη της ομάδας στο Παγκόσμιο Κύπελλο 2010, ενώ συνέχισε την προπονητική του σταδιοδρομία ως το τέλος της ζωής του, το οποίο ήρθε στις 25 Νοεμβρίου του 2020 σε ηλικία 60 ετών."@el .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Artful_Dodger> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Marseille_turn> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Alfio_Basile> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/File:Maradona_CRS.jpg> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Hernia> .
<http://dbpedia.org/resource/Diego_Maradona> <http://www.w3.org/2002/07/owl#sameAs> <http://ru.dbpedia.org/resource/Марадона,_Диего_Армандо> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/managerClub> <http://dbpedia.org/resource/Racing_Club_de_Avellaneda> .
<http://dbpedia.org/resource/Diego_Maradona> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/Category:1994_FIFA_World_Cup_players> .
```