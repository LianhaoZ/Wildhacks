import requests
from bs4 import BeautifulSoup

def GenerateCourses(url) -> dict:
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the paragraphs on the website
    paragraphs = soup.find_all("p")

    # Extract the text from each paragraph and print it
    courses = {}
    for p in paragraphs[1:]:
        words = p.get_text().split()
        if len(words) <= 2:
            continue
        name = words[0] + " " + words[1]
        
        prerequisites = []
        start = 0
        for i, word in enumerate(words):
            if "Prerequisite" in word or "Prerequisite" == word:
                # Start collecting them
                start = i + 1
        
        if start == 0:
            courses[name] = None
            continue

        for word in words[start:]:
            if "." in word:
                # this is the end
                removal = word.replace(".", "")
                if len(removal) > 0:
                    prerequisites.append(removal)
                break
            prerequisites.append(word)
        
        if len(prerequisites) == 0:
            courses[name] = None
        else:
            courses[name] = " ".join(prerequisites)
    return courses
