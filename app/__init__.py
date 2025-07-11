import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict 
import datetime

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(mydb)

class TimelinePost (Model) :
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = mydb
mydb. connect ()
mydb. create_tables([TimelinePost])

hero_info = {
    "name": "Jenny Cheng",
    "intro": "A passionate software engineer specializing in AI and full-stack development. I thrive on building innovative solutions and bringing ideas to life.",
}

about_info = {
    "name": "Jenny Cheng",
    "bio": "I'm a software engineer passionate about AI and full-stack development.",
    "location": "San Francisco, CA",
    "title": ["Software Engineer", "Software Developer"],
    "interests": ["AI", "Web Dev", "Hackathons", "Startups"],
    "photo_url": "/static/img/photo.JPG",
}

experiences_data = [
    {
        "job_title": "Data Operator",
        "date": "2022 - Present",
        "location": "San Francisco, CA",
        "company_name": "Google",
        "company_logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Google_%22G%22_logo.svg/800px-Google_%22G%22_logo.svg.png",
        "tech_stack": ["Python", "Docker", "AWS", "Kubernetes", "React", "Node.js"],
        "description": "Led a team to build scalable cloud-native applications. Improved CI/CD pipelines, mentored junior developers, and collaborated with cross-functional teams to deliver high-impact products.",
    },
    {
        "job_title": "Quantitative Researcher",
        "date": "2020 - 2022",
        "location": "New York, NY",
        "company_name": "Jane Street",
        "company_logo": "https://ocaml.janestreet.com/ocaml-core/v0.12/doc/logo.png",
        "tech_stack": ["Python", "OCaml", "Pandas"],
        "description": "Developed and backtested trading strategies, analyzed large datasets, and collaborated with traders to optimize performance.",
    },
    {
        "job_title": "Backend Developer",
        "date": "2018 - 2020",
        "location": "Bozeman, MT",
        "company_name": "Snowflake",
        "company_logo": "https://logos-world.net/wp-content/uploads/2022/11/Snowflake-Symbol.png",
        "tech_stack": ["Go", "PostgreSQL", "Docker"],
        "description": "Designed and implemented RESTful APIs, optimized database queries, and maintained microservices infrastructure.",
    },
]

education_data = [
    {
        "degree": "M.Sc. Computer Science",
        "date": "2016 - 2018",
        "location": "Stanford, CA",
        "institution_name": "Stanford University",
        "institution_logo": "https://identity.stanford.edu/wp-content/uploads/sites/3/2020/07/block-s-right.png",
        "description": "Specialized in Artificial Intelligence and Machine Learning. Graduated with honors.",
    },
    {
        "degree": "B.Sc. Computer Science",
        "date": "2012 - 2016",
        "location": "Cambridge, MA",
        "institution_name": "MIT",
        "institution_logo": "https://download.logo.wine/logo/Massachusetts_Institute_of_Technology/Massachusetts_Institute_of_Technology-Logo.wine.png",
        "description": "Focused on software engineering principles and data structures. Active member of the coding club.",
    },
]

hobbies = [
    {
        "name": "Foodie",
        "image": "/static/img/food.jpg",
        "color": "#B39DDB",
        "label": "Foodie",
    },
    {
        "name": "Driving",
        "image": "/static/img/drive.jpg",
        "color": "#9575CD",
        "label": "Driving",
    },
    {"name": "Tech", "image": "wifi.png", "color": "#7E57C2", "label": "Tech"},
    {"name": "Design", "color": "#673AB7", "label": "Design"},
    {
        "name": "Fitness",
        "image": "/static/img/gym.jpg",
        "color": "#5E35B1",
        "label": "Fitness",
    },
    {"name": "Cafe", "color": "#512DA8", "label": "Coffee Time"},
]

projects = [
    {
        "title": "Glance",
        "subtitle": "AI Social Cheat Sheet",
        "description": "An AI-powered tool that summarizes any X user's tweets into a snapshot of their interests, tone, and focus.",
        "image_url": "/img/projects/glance.webp",
        "link": "https://github.com/ericcxie/glance",
        "tags": ["Next.js", "OpenAI API", "X API", "Supabase", "Prisma"]
    },
    {
        "title": "Summailize",
        "subtitle": "Gmail Digest Generator",
        "description": "A Gmail extension that summarizes unread emails using AI and stores digest in Firestore, with support for both per-email and full summary views.",
        "image_url": "/img/projects/summailize.webp",
        "link": "https://github.com/jennyycheng/summailize",
        "tags": ["Python", "Flask", "OpenAI API", "Gmail API", "Firebase"]
    },
    {
        "title": "IntelliView",
        "subtitle": "Mock Interview Transcript Agent",
        "description": "Built with Google’s AI Agent Development Kit, this tool conducts real-time mock interviews, transcribes sessions, and summarizes answers using Gemini.",
        "image_url": "/static/img/Intelliview.png",
        "link": "https://github.com/lydia-yan/Intelliview",
        "tags": ["Gemini", "Google ADK", "FastAPI", "WebSocket", "Streaming"]
    },
    {
        "title": "Smart Bookmark",
        "subtitle": "AI Bookmark Organizer",
        "description": "A Chrome extension that classifies and tags your saved URLs using Gemini’s summarization and prompt APIs, and suggests folders based on content.",
        "image_url": "/img/projects/bookmark.webp",
        "link": "https://github.com/Jennyyyy0212/bookmark-organizer",
        "tags": ["Chrome Extension", "Gemini", "Prompt API", "JavaScript"]
    },
    {
        "title": "TeamCAST",
        "subtitle": "Team Contribution Tracking Tool",
        "description": "An AI-powered dashboard that auto-fetches GitHub PRs and visualizes team contributions for collaborative learning or grading use cases.",
        "image_url": "/img/projects/teamcast.webp",
        "link": "https://github.com/jennyycheng/teamcast",
        "tags": ["React", "Firebase", "GitHub API", "Tailwind CSS", "PR Viewer"]
    }
]

skills = [
    {"name": "Linux", "filename": "/static/img/icon/Linux.png"},
    {"name": "Docker", "filename": "/static/img/icon/Docker.png"},
    {"name": "Python", "filename": "/static/img/icon/Python.png"},
    {"name": "React", "filename": "/static/img/icon/React.png"},
    {"name": "JavaScript", "filename": "/static/img/icon/Javascript.png"},
    {"name": "Java", "filename": "/static/img/icon/Java.png"},
    {"name": "Google ADK", "filename": "/static/img/icon/Google-adk.png"},
    {"name": "MongoDB", "filename": "/static/img/icon/Mongodb.png"},
    {"name": "Markdown", "filename": "/static/img/icon/Markdown.png"},
    {"name": "Flutter", "filename": "/static/img/icon/Flutter.png"},
    {"name": "FastAPI", "filename": "/static/img/icon/Fastapi.png"},
    {"name": "Flask", "filename": "/static/img/icon/Flask.png"},
    {"name": "GitHub", "filename": "/static/img/icon/Github.png"},
    {"name": "Git", "filename": "/static/img/icon/Git.png"},
    {"name": "Firebase", "filename": "/static/img/icon/Firebase.png"},
    {"name": "Dart", "filename": "/static/img/icon/Dart.png"},
    {"name": "Azure", "filename": "/static/img/icon/Azure.png"},
    {"name": "Android", "filename": "/static/img/icon/Android.png"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="MLH Fellow",
        hero_info=hero_info,
        about_info=about_info,
        experiences=experiences_data,
        education=education_data,
        projects=projects,
        mapbox_token = "pk.eyJ1IjoiamVubnl5eXkwMjEyIiwiYSI6ImNtY3RvZTNkNDAwZzgyd3B5cmxvb2FzeTgifQ.OX0MjKAR_xr1lP8gAAYJKw",
        locations = [
            {"title": "Waterloo, ON", "coords": [-80.5167, 43.4668]},
            {"title": "Toronto, ON", "coords": [-79.3832, 43.6532]},
            {"title": "Vancouver, BC", "coords": [-123.1207, 49.2827]},
        ],
        url=os.getenv("URL"),
        skills=skills,
    )


@app.route("/hobbies")
def hobbies_route():
    return render_template(
        "hobbies.html",
        title="MLH Fellow",
        hobby_data=hobbies,
        url=os.getenv("URL"),
    )


@app. route('/api/timeline_post', methods=['POST' ])
def post_time_line_post():
    name = request. form[ 'name']
    email = request. form['email']
    content = request.form ['content']
    timeline_post = TimelinePost. create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post() :
    return {
        'timeline_posts': [ 
            model_to_dict(p)
            for p in
        TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }