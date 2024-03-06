# HW3 - SPARQL

---
## Task 1
### Task 1.1 + 1.2
1) Downloaded apache jena fuseki 4.10.0.zip from: https://jena.apache.org/download/
2) Ran using java
3) Grabbed `curl https://dbpedia.org/data/Diego_Maradona.ttl > data.ttl` and uploaded `data.ttl` to the server

### Task 1.3
#### SELECT 1 

Retrieves 10 distinct ordered subjects, skipping the first 5.
```
SELECT DISTINCT ?subject
WHERE {
  ?subject ?predicate ?object
}
LIMIT 10
OFFSET 5
```
```
curl -X POST -H \
"Content-Type: application/x-www-form-urlencoded" \
--data "query=SELECT DISTINCT ?subject WHERE { ?subject ?predicate ?object } ORDER BY ?subject LIMIT 10 OFFSET 5" \
http://localhost:3030/DiegoMaradona/
```
#### SELECT 2 
Retrieves the birthplace and birth date of Diego Maradona, including optional birth date information
```
PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT ?birthPlace ?birthDate
WHERE {
  <http://dbpedia.org/resource/Diego_Maradona> dbo:birthPlace ?birthPlace .
  OPTIONAL { <http://dbpedia.org/resource/Diego_Maradona> dbo:birthDate ?birthDate }
}
```
```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" \
--data "query=PREFIX dbo: <http://dbpedia.org/ontology/> SELECT ?birthPlace ?birthDate WHERE { <http://dbpedia.org/resource/Diego_Maradona> dbo:birthPlace ?birthPlace . OPTIONAL { <http://dbpedia.org/resource/Diego_Maradona> dbo:birthDate ?birthDate } } ORDER BY ?birthDate" \
http://localhost:3030/DiegoMaradona/
```
#### CONSTRUCT 1
Constructs a new graph with triples containing subjects, predicates, and objects
```
CONSTRUCT {
  ?subject ?predicate ?object
}
WHERE {
  ?subject ?predicate ?object
}
LIMIT 10
```
```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" \
--data "query=CONSTRUCT { ?subject ?predicate ?object } WHERE { ?subject ?predicate ?object } LIMIT 10" \
http://localhost:3030/DiegoMaradona/
```
#### CONSTRUCT 2
Constructs a new graph with triples containing Diego Maradona's height and positions he played.
```
PREFIX dbo: <http://dbpedia.org/ontology/>

CONSTRUCT {
  <http://dbpedia.org/resource/Diego_Maradona> dbo:height ?height .
  <http://dbpedia.org/resource/Diego_Maradona> dbo:position ?position .
}
WHERE {
  <http://dbpedia.org/resource/Diego_Maradona> dbo:height ?height .
  <http://dbpedia.org/resource/Diego_Maradona> dbo:position ?position .
}
```
```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" \
--data "query=PREFIX dbo: <http://dbpedia.org/ontology/> CONSTRUCT { <http://dbpedia.org/resource/Diego_Maradona> dbo:height ?height . <http://dbpedia.org/resource/Diego_Maradona> dbo:position ?position . } WHERE { <http://dbpedia.org/resource/Diego_Maradona> dbo:height ?height . <http://dbpedia.org/resource/Diego_Maradona> dbo:position ?position . }" \
http://localhost:3030/DiegoMaradona/
```
#### ASK
Checks if Diego Maradona is associated with any DBpedia ontogoly team.
```
PREFIX dbo: <http://dbpedia.org/ontology/>
ASK
WHERE {
  <http://dbpedia.org/resource/Diego_Maradona> ?property ?object
  FILTER (?property = dbo:team)
}
```
```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" \
--data "query=PREFIX dbo: <http://dbpedia.org/ontology/> ASK WHERE { <http://dbpedia.org/resource/Diego_Maradona> ?property ?object FILTER (?property = dbo:team) }" \
http://localhost:3030/DiegoMaradona/
```
#### DESCRIBE
Retrieves information about <http://dbpedia.org/resource/Diego_Maradona>.
```
DESCRIBE <http://dbpedia.org/resource/Diego_Maradona>
```
```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" \
--data "query=DESCRIBE <http://dbpedia.org/resource/Diego_Maradona>" \
http://localhost:3030/DiegoMaradona/
```
### [Task 1.3 RESULTS](results/results.md)

---
# Task 2
### [Task 2 code](src/crawler.py)
### [Task 2 result](results/crawler_results.txt)
