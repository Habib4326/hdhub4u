import json
import os

def generate_movie():
    filename = 'movies.json'
    
    # Load existing data if file exists
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                movies = json.load(f)
            except:
                movies = []
    else:
        movies = []

    print(f"--- Current Movie Count: {len(movies)} ---")

    while True:
        print("\nAdd New Movie (Type 'exit' to stop):")
        name = input("Movie Name: ")
        if name.lower() == 'exit': break
        
        url = input("Video URL: ")
        thumb = input("Thumbnail URL: ")
        fanart = input("Fanart URL: ")

        # Create new movie object
        new_movie = {
            "name": name,
            "url": url,
            "thumbnail": thumb,
            "fanart": fanart
        }

        # Append to the list
        movies.append(new_movie)
        
        cont = input("Add another movie? (y/n): ")
        if cont.lower() != 'y': break

    # Save with optimized spacing
    with open(filename, 'w', encoding='utf-8') as f:
        # indent=2 keeps it readable, while separators remove extra spaces
        json.dump(movies, f, indent=2, separators=(',', ': '))

    print(f"\nSuccessfully Saved! Total movies in list: {len(movies)}")

if __name__ == "__main__":
    generate_movie()