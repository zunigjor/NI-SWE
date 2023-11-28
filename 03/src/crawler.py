import requests


def run_sparql_query(results_per_page, offset):
    # Specify your SPARQL query here
    sparql_query = f"""
        SELECT ?subject ?predicate ?object
        WHERE {{
          ?subject ?predicate ?object
        }}
        LIMIT {results_per_page}
        OFFSET {offset}
    """

    # DBpedia SPARQL endpoint
    endpoint_url = "http://dbpedia.org/sparql"

    # Send the SPARQL query
    response = requests.get(endpoint_url, params={'query': sparql_query, 'format': 'json'})

    # Check for successful response
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def main():
    total_results = 100
    results_per_page = 10
    offset = 0

    while offset < total_results:
        # Run the SPARQL query with pagination
        result_json = run_sparql_query(results_per_page, offset)

        # Process the results (you can customize this based on your needs)
        if result_json:
            results = result_json.get('results', {}).get('bindings', [])
            for result in results:
                print(result)

        # Update offset for the next page
        offset += results_per_page


if __name__ == "__main__":
    main()
