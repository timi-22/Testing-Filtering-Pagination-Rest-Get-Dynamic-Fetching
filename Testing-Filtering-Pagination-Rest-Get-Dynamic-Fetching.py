from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import datetime


app = Flask(__name__)
app.secret_key = "secret"  # To use sessions. change "secret" to a/random secret key.



POSTDATA = [
    {
        "title": "Holographic",
        "location_detail": ["AS", "AG", "AQ", "DZ"],
        "location": "Algeria, Antarctica, and more",
        "years_ranking": 6,
        "category": "CIS",
        "posted": "2024-01-01",
    },
    {
        "title": "Data Analysis 101",
        "location_detail": ["AD", "AL", "AS", "AI"],
        "location": "Albania, Antigua & Barbuda and more",
        "years_ranking": 7,
        "category": "PIM",
        "posted": "2023-11-12",
    },
    {
        "title": "Python for Beginners",
        "location_detail": ["AR", "AG"],
        "location": "Argentina and Andorra",
        "years_ranking": 0.3,
        "category": "BIL",
        "posted": "2023-08-15",
    },
    {
        "title": "Chemistry for Physicians",
        "location_detail": ["AL", "AG"],
        "location": "Argentina and Andorra",
        "years_ranking": 0.3,
        "category": "BIL",
        "posted": "2024-04-11",
    },
    {
        "title": "Farrowing in Forestry",
        "location_detail": ["AQ", "AG"],
        "location": "Antarctica and Andorra",
        "years_ranking": 4,
        "category": "BIL",
        "posted": "2023-12-12",
    },
    {
    "title": "Renaisansse",
        "location_detail": ["AS", "AG", "AQ", "DZ"],
        "location": "Algeria, Antarctica, and more",
        "years_ranking": 6,
        "category": "CIS",
        "posted": "2024-01-01",
    },
    {
        "title": "Punk Analysis 501",
        "location_detail": ["AD", "AL", "AS", "AI"],
        "location": "Argentina, Antigua & Barbuda and more",
        "years_ranking": 12,
        "category": "PIM",
        "posted": "2024-01-18",
    },
    {
        "title": "Melon for Beginners",
        "location_detail": ["AI", "AG"],
        "location": "Argentina and Andorra",
        "years_ranking": 6,
        "category": "BIL",
        "posted": "2023-09-25",
    },
     {
        "title": "Holographic",
        "location_detail": ["AS", "AG", "AQ", "DZ"],
        "location": "Algeria, Antarctica, and more",
        "years_ranking": 6,
        "category": "CIS",
        "posted": "2024-01-01",
    },
    {
        "title": "Data Analysis 101",
        "location_detail": ["AD", "AL", "AS", "AI"],
        "location": "Albania, Antigua & Barbuda and more",
        "years_ranking": 7,
        "category": "PIM",
        "posted": "2023-11-12",
    },
    {
        "title": "Python for Beginners",
        "location_detail": ["AR", "AG"],
        "location": "Argentina and Andorra",
        "years_ranking": 0.3,
        "category": "BIL",
        "posted": "2023-08-15",
    },
    {
        "title": "Chemistry for Physicians",
        "location_detail": ["AL", "AG"],
        "location": "Argentina and Andorra",
        "years_ranking": 0.3,
        "category": "BIL",
        "posted": "2024-04-11",
    },
    {
        "title": "Farrowing in Forestry",
        "location_detail": ["AQ", "AG"],
        "location": "Antarctica and Andorra",
        "years_ranking": 4,
        "category": "BIL",
        "posted": "2023-12-12",
    },
    {
    "title": "Renaisansse",
        "location_detail": ["AS", "AG", "AQ", "DZ"],
        "location": "Algeria, Antarctica, and more",
        "years_ranking": 6,
        "category": "CIS",
        "posted": "2024-01-01",
    },
    {
        "title": "Punk Analysis 501",
        "location_detail": ["AD", "AL", "AS", "AI"],
        "location": "Argentina, Antigua & Barbuda and more",
        "years_ranking": 12,
        "category": "PIM",
        "posted": "2024-01-18",
    },
    {
        "title": "Melon for Beginners",
        "location_detail": ["AI", "AG"],
        "location": "Argentina and Andorra",
        "years_ranking": 6,
        "category": "BIL",
        "posted": "2023-09-25",
    },
]

# Helper function to apply filters
def filter_data(data, filters):
    filtered = data

    # Category filter
    category = filters.get("category")
    if category and category != "All":
        filtered = [item for item in filtered if item["category"] == category]

    # Location filter
    locations = filters.get("location")
    if locations:
        filtered = [
            item
            for item in filtered
            if any(loc in item["location_detail"] for loc in locations.split(","))
        ]

    # Year ranking filter
    yearrank0 = filters.get("yearrank0")
    if yearrank0:
        filtered = [item for item in filtered if item["years_ranking"] >= float(yearrank0)]

    yearrank1 = filters.get("yearrank1")
    if yearrank1:
        filtered = [item for item in filtered if item["years_ranking"] <= float(yearrank1)]

    # Search filter
    search = filters.get("search")
    if search:
        filtered = [item for item in filtered if search.lower() in item["title"].lower()]

    return filtered





# re-routing, here.

@app.route('/all', methods=['GET'])
def cisonlyall():
    # Let's say you want to pre-set filters like category, location, and sort
    category = 'All'
    location = 'AG,DZ' # locations as a string
    sort = 'desc' # Default to 'desc' if not provided
    
    # Store them in session so they can be accessed on the next route
    session['category'] = category
    session['location'] = location
    session['sort'] = sort  # Store sort preference
    
    # Redirect to the root route "/"
    return redirect(url_for('index'))

@app.route('/cis', methods=['GET'])
def cisonly():
    category = 'CIS'
    location = 'DZ' # locations as a string
    sort = 'desc' # Default to 'desc' if not provided
    
    # Store them in session
    session['category'] = category
    session['location'] = location
    session['sort'] = sort
    
    # Redirect to the root route
    return redirect(url_for('index'))

@app.route('/pim', methods=['GET'])
def cisadvanced():
    category = 'PIM'
    location = '' # locations as a string
    sort = 'asc'
    
    # Store them in session
    session['category'] = category
    session['location'] = location
    session['sort'] = sort
    
    # Redirect to the root route
    return redirect(url_for('index'))

@app.route('/bil', methods=['GET'])
def cisbasic():
    category = 'BIL'
    location = 'AS,DZ' # locations as a string
    sort = 'asc'
    
    # Store them in session
    session['category'] = category
    session['location'] = location
    session['sort'] = sort
    
    # Redirect to the root route
    return redirect(url_for('index'))
    
  
##to clear session for user after clicking clear-filters.  
@app.route('/clear-session', methods=['POST'])
def clear_session():
    # Clear session data (if any)
    session.pop('category', None)
    session.pop('location', None)
    session.pop('sort', None)
    #session.pop('yearrank0', None)
    #session.pop('yearrank1', None)
    #session.pop('search', None)
    #session.pop('page', None)
    return jsonify({'status': 'Session cleared'}), 200
#return statement often required in any request to return back to the sender that it could move on or so, especially for such this type(s).
##to clear session for user after clicking clear-filters.

# re-routing, here, e.g. for /africajobs. up i.



@app.route('/')
def index():
    # Retrieve the filters from session (set by /...the above)
    HLPcategory = session.get('category', 'All')
    HLPlocation = session.get('location', '')
    HLPsort = session.get('sort', 'desc')  # Default to 'desc' if not set in session
  
  
    # if there was routing
    if HLPlocation or HLPcategory or HLPsort:  
    	return render_template('index.html', HLPcategory=HLPcategory, HLPlocation=HLPlocation, HLPsort=HLPsort)
    # otherwise, no filter routing?
    else:
    	return render_template("index.html")
    	



@app.route("/get-data", methods=["GET"])
def get_data():
    filters = {
        "category": request.args.get("category"),
        "location": request.args.get("location"),
        "yearrank0": request.args.get("yearrank0"),
        "yearrank1": request.args.get("yearrank1"),
        "search": request.args.get("search"),
    }
    sort_order = request.args.get("sort", "desc")
    page = int(request.args.get("page", 1))
    items_per_page = int(request.args.get("items_per_page", 2))

    # Filter and sort data
    filtered_data = filter_data(POSTDATA, filters)
    sorted_data = sorted(
        filtered_data,
        key=lambda x: datetime.datetime.strptime(x["posted"], "%Y-%m-%d"),
        reverse=(sort_order == "desc"),
    )

    # Paginate
    start = (page - 1) * items_per_page
    end = start + items_per_page
    paginated_data = sorted_data[start:end]

    return jsonify({
        "data": paginated_data,
        "total_items": len(sorted_data),
        "total_pages": (len(sorted_data) + items_per_page - 1) // items_per_page,
    })

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
# Jinja template, the {{}} are resolved in the backend before getting to client side javascript or html intepreter, hence, commenting empty {{}} in html in html/js/cs or .net or so is invalid and throws error, among other example cases of non-valid use of {{}}.