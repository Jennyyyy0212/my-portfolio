import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict 
import datetime

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


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
        "job_title": "Production Engineer Intern",
        "date": "2025 - Present",
        "location": "Remote, CA",
        "company_name": "Meta x MLH Fellowship",
        "company_logo": "/static/img/facebook-logo.jpeg",
        "company_link": "https://opensource.fb.com/partnerships/major-league-hacking/",
        "tech_stack": ["Python", "Flask", "Docker", "Linux", "Bash", "React"],
        "description": "Focused on improving system reliability and developer workflows through production engineering practices.",
        "details": {
            "bullets": [
                "Designed and implemented logging, monitoring, and alerting for Flask-based backend services using open-source tooling.",
                "Containerized full-stack applications with Docker and managed multi-service environments via Docker Compose.",
                "Wrote shell scripts to automate testing, deployment, and log analysis on Linux-based environments.",
                "Improved CI/CD pipelines and reduced production deployment time by over 30%.",
                "Collaborated with fellows and mentors from Meta to debug performance issues and conduct incident response simulations.",
            ]
        },
    },
    {
        "job_title": "Data Operator",
        "date": "2024 - 2024",
        "location": "Mountain View, CA",
        "company_name": "Athelas / Commure",
        "company_logo": "/static/img/commure-logo.jpeg",
        "company_link": "https://www.athelas.com/",
        "tech_stack": ["Python", "SQL", "Data Analytics"],
        "description": "Supported backend workflows and helped improve the accuracy and efficiency of patient data processing systems.",
        "details": {
            "bullets": [
                "Reviewed and validated large volumes of healthcare data across multiple hospital systems.",
                "Automated the inconsistency checking process using Python and solved around 80% of repetive tasks, reducing manual review effort",
                "Worked closely with engineers to debug data pipeline issues and propose improvements.",
            ]
        },
    },
    {
        "job_title": "Marketing Engineer",
        "date": "2023 - 2024",
        "location": "San Jose, CA",
        "company_name": "ABConvert",
        "company_logo": "/static/img/abconvert-logo.jpeg",
        "company_link": "https://www.abconvert.io/",
        "tech_stack": ["Python", "LLM", "OpenAI", "Pandas"],
        "description": "Built AI tools to optimize marketing campaigns through data analysis, automation, and content generation.",
        "details": {
            "bullets": [
                "Developed Python pipelines to analyze and segment marketing performance data using Pandas.",
                "Built prompt-based GPT tools that generated headlines, CTAs, and ad copy tailored to different user segments.",
                "Fine-tuned content generation using A/B testing results to improve engagement metrics.",
                "Collaborated with the marketing and engineering teams to launch LLM-based internal tools.",
                "Reduced manual campaign iteration time by over 50% through automation and insight generation.",
            ]
        },
    },
]

education_data = [
    {
        "degree": "M.Sc. Software Engineering",
        "date": "2014 - Present",
        "location": "Irvine, CA",
        "institution_name": "University of California, Irvine",
        "institution_logo": "/static/img/uci-logo.jpeg",
        "institution_link": "https://uci.edu/",
        "description": "Graduate program focused on scalable systems, backend development, and engineering best practices. Collaborating on real-world projects with a strong emphasis on infrastructure and testing.",
    },
    {
        "degree": "B.Sc. Business Analytics",
        "date": "2019 - 2023",
        "location": "San Jose, CA",
        "institution_name": "San Jose State University",
        "institution_logo": "/static/img/sjsu-logo.png",
        "institution_link": "https://www.sjsu.edu/",
        "description": "Studied data analytics, statistics, and business strategy with hands-on projects in machine learning and data visualization. Minor in CS. Graduated with honors.",
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
        "title": "Summailize",
        "subtitle": "Gmail Digest Generator",
        "description": "A Gmail extension that summarizes unread emails using AI and stores digest in Firestore, with support for both per-email and full summary views.",
        "image_url": "/static/img/summailize-screen.png",
        "link": "https://github.com/lydia-yan/Summailize",
        "tags": ["Python", "Flask", "OpenAI API", "Gmail API", "Firebase"]
    },
    {
        "title": "IntelliView",
        "subtitle": "Mock Interview Transcript Agent",
        "description": "Built with Google’s AI Agent Development Kit, this tool conducts real-time mock interviews, transcribes sessions, and summarizes answers using Gemini.",
        "image_url": "/static/img/intelliview-screen.png",
        "link": "https://github.com/lydia-yan/Intelliview",
        "tags": ["Gemini", "Google ADK", "FastAPI", "WebSocket", "Streaming"]
    },
    {
        "title": "Smart Bookmark",
        "subtitle": "AI Bookmark Organizer",
        "description": "A Chrome extension that classifies and tags your saved URLs using Gemini’s summarization and prompt APIs, and suggests folders based on content.",
        "image_url": "/static/img/bookmark-screen.png",
        "link": "https://github.com/Jennyyyy0212/bookmark-organizer",
        "tags": ["Chrome Extension", "Gemini", "Prompt API", "JavaScript"]
    },
    {
        "title": "TeamCAST",
        "subtitle": "Team Contribution Tracking Tool",
        "description": "An AI-powered dashboard that auto-fetches GitHub PRs and visualizes team contributions for collaborative learning or grading use cases.",
        "image_url": "/static/img/Intelliview.png",
        "link": "https://github.com/jennyycheng/teamcast",
        "tags": ["React", "Firebase", "GitHub API", "Tailwind CSS", "PR Viewer"]
    }
]

skills = [
    {"name": "Linux", "filename": "/static/img/icon/Linux.png"},
    {"name": "Docker", "filename": "/static/img/icon/Docker.png"},
    {"name": "Python", "filename": "/static/img/icon/Python.png"},
    {"name": "React", "filename": "/static/img/icon/React.png"},
    {"name": "JavaScript", "filename": "/static/img/icon/JavaScript.png"},
    {"name": "Java", "filename": "/static/img/icon/Java.png"},
    {"name": "MongoDB", "filename": "/static/img/icon/MongoDB.png"},
    {"name": "Markdown", "filename": "/static/img/icon/Markdown.png"},
    {"name": "Flutter", "filename": "/static/img/icon/Flutter.png"},
    {"name": "FastAPI", "filename": "/static/img/icon/FastAPI.png"},
    {"name": "Flask", "filename": "/static/img/icon/Flask.png"},
    {"name": "GitHub", "filename": "/static/img/icon/GitHub.png"},
    {"name": "Git", "filename": "/static/img/icon/Git.png"},
    {"name": "Firebase", "filename": "/static/img/icon/Firebase.png"},
    {"name": "Dart", "filename": "/static/img/icon/Dart.png"},
    {"name": "Azure", "filename": "/static/img/icon/Azure.png"},
    {"name": "Android", "filename": "/static/img/icon/Android.png"},
]

mydb.connect()
mydb.create_tables([TimelinePost])

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

@app.route("/timeline")
def timeline():
    return render_template(
        "timeline.html",
        title="Timeline"
    )


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    error = validateTimelineForm(request.form)

    if len(error) != 0:
        return error, 400
    else:
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']
        timeline_post = TimelinePost.create(name=name, email=email, content=content)
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
                                                                                        
@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def get_single_post(post_id):
    post = TimelinePost.get_or_none(TimelinePost.id == post_id)
    if post:
        post.delete_instance()
        return {"message": f"Deleted timeline post {post_id}"}, 200
    return {"error": "Post not found"}, 404


def validateTimelineForm(form) -> str:
    if 'name' not in form or len(form['name']) == 0:
        return "Invalid name"
    
    if 'content' not in form or len(form['content']) == 0:
        return "Invalid content"
    
    if 'email' not in form or '@' not in form['email'] == 0 or '.' not in form['email']:
        return "Invalid email"
    
    return ""
