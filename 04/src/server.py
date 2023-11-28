from flask import Flask, make_response, request
import rdflib

########################################################################################################################
# FLASK SETUP
app = Flask(__name__)
port = 8080
host = 'localhost'
########################################################################################################################
# FUSEKI HOST
fusekiHost = 'http://localhost:3030/'
##################################################################
# PATHS
paths = {"cities", "countries"}
##################################################################
# ITEMS
cities = {"Santiago", 'Bratislava'}
countries = {"Chile"}
all_items = set().union(cities, countries)
##################################################################
# ACCEPTED FORMATS
application_json = "application/json"
application_xml = "application/xml"
text_turtle = "text/turtle"
accepted = {application_json, application_xml, text_turtle}
########################################################################################################################


@app.route("/<path>/<item>")
def get_path_item(path, item):
    accept = request.headers.get("Accept")

    # Do not accept anything other than json, xml or n-triples
    if accept not in accepted:
        return get_404()

    # Return not found if not in paths
    if path not in paths:
        return get_404()

    # Item not between database items
    just_item = item.split(".")[0]
    if just_item not in all_items:
        return get_404()

    # JSON -> application/json
    if item.endswith(".json") and accept == application_json:
        return query_fuseki(just_item, accept)

    # XML -> application/xml
    if item.endswith(".xml") and accept == application_xml:
        return query_fuseki(just_item, accept)

    # TTF -> text/turtle
    if item.endswith(".ttl") and accept == text_turtle:
        return query_fuseki(just_item, accept)

    return get_303_location(path, just_item, accept)


def get_303_location(path, item, accept):
    response = make_response()
    response.status_code = 303
    if accept == application_json:
        response.location = f"http://{host}:{port}/{path}/{item}.json"
    elif accept == application_xml:
        response.location = f"http://{host}:{port}/{path}/{item}.xml"
    elif accept == text_turtle:
        response.location = f"http://{host}:{port}/{path}/{item}.ttl"
    return response


def query_fuseki(item, accept):
    graph = rdflib.Graph()
    graph.parse(f"{fusekiHost}{item}")
    # SPARQL query about the item
    query = f"""
        PREFIX dbpedia: <http://dbpedia.org/resource/>
        SELECT ?subject ?predicate ?object
        WHERE {{
            dbpedia:{item} ?predicate ?object
        }}
        LIMIT 20
        """
    query_result = graph.query(query)

    if accept == application_json:
        response = make_response(query_result.serialize(format="json"), 200)
        response.content_type = "application/json"
        return response
    elif accept == application_xml:
        response = make_response(query_result.serialize(format="xml"), 200)
        response.content_type = "application/xml"
        return response
    elif accept == text_turtle:
        response = make_response(graph.serialize(format="turtle"), 200)
        response.content_type = "text/turtle"
        return response


def get_404():
    return make_response("", 404)


########################################################################################################################
if __name__ == '__main__':
    print(f"Server running at http://{host}:{port}/")
    app.run(host=host, port=port)
