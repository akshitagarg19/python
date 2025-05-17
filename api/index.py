import json

def handler(request, response):
    # Load the students data from the JSON file
    with open("students.json") as f:
        data = json.load(f)

    # Get the names from query parameters
    names = request.query.getlist("name")
    marks = [data.get(name, None) for name in names]

    # Enable CORS (Cross-Origin Resource Sharing)
    response.headers["Access-Control-Allow-Origin"] = "*"

    # Return the marks of the requested names as JSON
    return response.json({ "marks": marks })
