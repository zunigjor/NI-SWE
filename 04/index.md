# HW4 - Linked Data

## Task 1
* Filled Fuseki with:
    * [Chile.ttl](src/Chile.ttl) on `\Chile` endpoint
    * [Santiago.ttl](src/Santiago.ttl) on `\Santiago` endpoint
    * [Bratislava.ttl](src/Bratislava.ttl) on `\Bratislava` endpoint
## Task 2
* Created a Flask server that provides results on paths:
  * `\cities`
  * `\countries`
* The `\cities` path provides:
  * `\cities\Bratislava.json` 
  * `\cities\Bratislava.xml`
  * `\cities\Bratislava.ttl`
  * `\cities\Santiago.json` 
  * `\cities\Santiago.xml`
  * `\cities\Santiago.ttl`
* The `\countries` path provides:
  * `\countries\Chile.json` 
  * `\countries\Chile.xml`
  * `\countries\Chile.ttl`
* JSON and XML are results of this query:
```
PREFIX dbpedia: <http://dbpedia.org/resource/>
SELECT ?subject ?predicate ?object
WHERE {
    dbpedia:<item> ?predicate ?object
}
LIMIT 20
```
* TTL returns the entire TTL dataset in turtle format

* Server provides the 303 Linked Data URI dereferencing strategy where it provides a location link when the suffix isn't provided.
```
curl -H 'Accept: application/json' -i http://localhost:8080/cities/Santiago
```
```
HTTP/1.1 303 SEE OTHER
Server: Werkzeug/3.0.1 Python/3.10.12
Date: Tue, 28 Nov 2023 12:41:00 GMT
Content-Type: text/html; charset=utf-8
Location: http://localhost:8080/cities/Santiago.json
Content-Length: 0
Connection: close
```
### Example curl requests:
```
curl -H 'Accept: application/json' -i http://localhost:8080/cities/Santiago.json
```
#### [curl_1_result.txt](results/curl_1_result.txt)
```
curl -H 'Accept: application/xml' -i http://localhost:8080/cities/Bratislava.xml
```
#### [curl_2_result.txt](results/curl_2_result.txt)
```
curl -H 'Accept: text/turtle' -i http://localhost:8080/countries/Chile.ttl
```
#### [curl_3_result.txt](results/curl_3_result.txt)