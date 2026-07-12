"""Seed the database with initial data matching the 2K Solutions frontend content."""

from datetime import datetime, timezone
import bcrypt
from app.extensions import db
from app.models.user import User
from app.models.course import Course
from app.models.module import Module
from app.models.service import Service
from app.models.testimonial import Testimonial
from app.models.faq import FAQ
from app.models.technology import Technology
from app.models.milestone import Milestone
from app.models.step import Step
from app.models.differentiator import Differentiator
from app.models.site_setting import SiteSetting


def seed_database() -> None:
    if User.query.first():
        return

    admin_password = bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode("utf-8")
    admin = User(
        first_name="Admin",
        last_name="User",
        email="admin@2ksolutions.com",
        phone="+91 98765 43210",
        password_hash=admin_password,
        role="admin",
        terms_accepted=True,
        is_active=True,
        email_verified=True,
    )
    db.session.add(admin)

    # Courses
    courses_data = [
        {
            "slug": "software-development",
            "title": "Software Development",
            "subtitle": "Master Python, Java, C++, and modern software engineering practices.",
            "description": "This comprehensive software development program takes you from fundamentals to advanced concepts...",
            "definition": "Software development is the process of designing, programming, testing, and maintaining applications...",
            "quote": "Software development is not just about writing code — it's about solving problems and building solutions that make a difference.",
            "duration_months": 6,
            "num_projects": 5,
            "badge": "Popular",
            "icon_class": "fab fa-python",
            "curriculum": [
                {"title": "Python Programming", "description": "Data structures, OOP, NumPy, Pandas"},
                {"title": "Java Development", "description": "OOP, multithreading, collections"},
                {"title": "C++ Programming", "description": "Pointers, STL, algorithms"},
                {"title": "Software Engineering", "description": "Git, Agile, design patterns, CI/CD"},
                {"title": "Database Management", "description": "SQL, MySQL, PostgreSQL"},
                {"title": "Deployment & DevOps", "description": "AWS/Azure, Docker, CI/CD pipelines"},
            ],
            "career_outcomes": [
                "Build scalable backend systems and APIs",
                "Develop cross-platform desktop applications",
                "Design and manage complex databases",
                "Implement CI/CD pipelines and DevOps workflows",
                "Lead software development teams",
                "Architect enterprise-level software solutions",
            ],
            "history": "Software development has evolved significantly over the past few decades...",
            "display_order": 1,
            "modules": [
                {"title": "Python Programming", "description": "Master Python from basics to advanced. Learn data structures, object-oriented programming, and popular libraries like NumPy and Pandas.", "icon_class": "fab fa-python", "display_order": 1},
                {"title": "Java Development", "description": "Deep dive into Java with OOP concepts, multithreading, collections framework, and enterprise applications.", "icon_class": "fab fa-java", "display_order": 2},
                {"title": "C++ Programming", "description": "Learn C++ with pointers, STL, memory management, and algorithm implementation.", "icon_class": "fas fa-code", "display_order": 3},
                {"title": "Software Engineering", "description": "Master Git, Agile methodologies, design patterns, and CI/CD pipelines.", "icon_class": "fas fa-code-branch", "display_order": 4},
                {"title": "Database Management", "description": "Work with SQL, MySQL, and PostgreSQL for robust data management.", "icon_class": "fas fa-database", "display_order": 5},
                {"title": "Deployment & DevOps", "description": "Deploy applications using AWS, Azure, Docker, and CI/CD tools.", "icon_class": "fas fa-cloud", "display_order": 6},
            ],
        },
        {
            "slug": "web-development",
            "title": "Web Development",
            "subtitle": "Full-stack web development with HTML, CSS, JavaScript, React, Node.js, and more.",
            "description": "Become a full-stack web developer with this comprehensive program covering frontend and backend technologies...",
            "definition": "Web development encompasses building websites and web applications that run on the internet...",
            "quote": "The web is the most powerful platform ever created. Learning to build for it is a superpower.",
            "duration_months": 5,
            "num_projects": 4,
            "badge": None,
            "icon_class": "fab fa-react",
            "curriculum": [
                {"title": "HTML & CSS", "description": "HTML5, CSS3, Flexbox, Grid"},
                {"title": "JavaScript", "description": "ES6+, DOM, async, promises"},
                {"title": "React.js", "description": "Components, hooks, state management"},
                {"title": "Node.js & Express", "description": "REST APIs, middleware, auth"},
                {"title": "Databases", "description": "MongoDB, PostgreSQL, ORMs"},
                {"title": "Deployment", "description": "Vercel, Netlify, AWS, CI/CD"},
            ],
            "career_outcomes": [
                "Build responsive, accessible websites",
                "Develop single-page applications with React",
                "Create RESTful APIs with Node.js",
                "Work with both SQL and NoSQL databases",
                "Deploy and maintain production web applications",
                "Implement authentication and authorization",
            ],
            "history": "The World Wide Web has transformed from static HTML pages to dynamic, interactive applications...",
            "display_order": 2,
            "modules": [
                {"title": "HTML & CSS", "description": "Build responsive layouts with HTML5, CSS3, Flexbox, Grid, and modern styling techniques.", "icon_class": "fab fa-html5", "display_order": 1},
                {"title": "JavaScript", "description": "Master ES6+ features, DOM manipulation, async programming, and promises.", "icon_class": "fab fa-js", "display_order": 2},
                {"title": "React.js", "description": "Build dynamic UIs with React components, hooks, context, and state management.", "icon_class": "fab fa-react", "display_order": 3},
                {"title": "Node.js & Express", "description": "Create powerful backends with Node.js, Express, middleware, and authentication.", "icon_class": "fab fa-node", "display_order": 4},
                {"title": "Databases", "description": "Work with MongoDB, PostgreSQL, and Prisma ORM for data persistence.", "icon_class": "fas fa-database", "display_order": 5},
                {"title": "Deployment", "description": "Deploy to Vercel, Netlify, AWS, and implement CI/CD pipelines.", "icon_class": "fas fa-rocket", "display_order": 6},
            ],
        },
        {
            "slug": "data-analytics",
            "title": "Data Analytics",
            "subtitle": "Learn SQL, Excel, Tableau, Power BI, and Python for data analysis and visualization.",
            "description": "Transform raw data into actionable insights with our data analytics program...",
            "definition": "Data analytics is the science of analyzing raw data to draw meaningful conclusions and support decision-making...",
            "quote": "Data is the new oil. It's valuable, but if unrefined it cannot really be used.",
            "duration_months": 4,
            "num_projects": 3,
            "badge": None,
            "icon_class": "fas fa-chart-bar",
            "curriculum": [
                {"title": "Excel & Spreadsheets", "description": "Pivot tables, VLOOKUP, macros"},
                {"title": "SQL & Databases", "description": "Joins, subqueries, window functions"},
                {"title": "Python for Data", "description": "Pandas, NumPy, Matplotlib"},
                {"title": "Tableau & Power BI", "description": "Dashboards, visualizations"},
                {"title": "Statistics", "description": "Hypothesis testing, regression"},
                {"title": "Reporting", "description": "KPI dashboards, data storytelling"},
            ],
            "career_outcomes": [
                "Analyze large datasets to extract insights",
                "Create interactive dashboards and reports",
                "Work with SQL databases efficiently",
                "Apply statistical methods to real-world problems",
                "Present data-driven recommendations",
                "Automate data processing workflows",
            ],
            "history": "Data analytics has become one of the most sought-after skills in the modern business landscape...",
            "display_order": 3,
            "modules": [
                {"title": "Excel & Spreadsheets", "description": "Master pivot tables, VLOOKUP, macros, and advanced Excel functions.", "icon_class": "fas fa-file-excel", "display_order": 1},
                {"title": "SQL & Databases", "description": "Learn joins, subqueries, window functions, and query optimization.", "icon_class": "fas fa-database", "display_order": 2},
                {"title": "Python for Data", "description": "Use Pandas, NumPy, and Matplotlib for data analysis and visualization.", "icon_class": "fab fa-python", "display_order": 3},
                {"title": "Tableau & Power BI", "description": "Create stunning dashboards and interactive visualizations.", "icon_class": "fas fa-chart-pie", "display_order": 4},
                {"title": "Statistics", "description": "Apply hypothesis testing, regression analysis, and statistical methods.", "icon_class": "fas fa-calculator", "display_order": 5},
                {"title": "Reporting", "description": "Build KPI dashboards and master data storytelling techniques.", "icon_class": "fas fa-file-alt", "display_order": 6},
            ],
        },
        {
            "slug": "cloud-computing",
            "title": "Cloud Computing",
            "subtitle": "AWS, Azure, and Google Cloud platforms with hands-on deployment experience.",
            "description": "Master cloud computing platforms and infrastructure management...",
            "definition": "Cloud computing delivers computing services over the internet, including storage, processing, and software...",
            "quote": "The cloud is not a place — it's a new way of thinking about infrastructure and scalability.",
            "duration_months": 5,
            "num_projects": 4,
            "badge": "New",
            "icon_class": "fas fa-cloud",
            "curriculum": [
                {"title": "AWS Fundamentals", "description": "EC2, S3, Lambda, RDS, VPC, IAM"},
                {"title": "Microsoft Azure", "description": "VMs, App Services, Functions, Blob"},
                {"title": "Google Cloud", "description": "GCP Compute, BigQuery, Kubernetes"},
                {"title": "Containers & K8s", "description": "Docker, Helm, microservices"},
                {"title": "Cloud Security", "description": "IAM, encryption, compliance"},
                {"title": "DevOps & CI/CD", "description": "Jenkins, GitHub Actions, Terraform"},
            ],
            "career_outcomes": [
                "Design and deploy cloud infrastructure",
                "Manage multi-cloud environments",
                "Implement containerized applications",
                "Automate infrastructure with IaC",
                "Ensure cloud security and compliance",
                "Optimize cloud costs and performance",
            ],
            "history": "Cloud computing has revolutionized how businesses deploy and scale their applications...",
            "display_order": 4,
            "modules": [
                {"title": "AWS Fundamentals", "description": "Learn EC2, S3, Lambda, RDS, VPC, IAM, and core AWS services.", "icon_class": "fab fa-aws", "display_order": 1},
                {"title": "Microsoft Azure", "description": "Work with Azure VMs, App Services, Functions, and Blob Storage.", "icon_class": "fab fa-microsoft", "display_order": 2},
                {"title": "Google Cloud", "description": "Explore GCP Compute, BigQuery, and Kubernetes Engine.", "icon_class": "fab fa-google", "display_order": 3},
                {"title": "Containers & Kubernetes", "description": "Master Docker, Kubernetes, Helm charts, and microservices architecture.", "icon_class": "fab fa-docker", "display_order": 4},
                {"title": "Cloud Security", "description": "Implement IAM policies, encryption, and compliance frameworks.", "icon_class": "fas fa-shield-alt", "display_order": 5},
                {"title": "DevOps & CI/CD", "description": "Automate with Jenkins, GitHub Actions, and Terraform.", "icon_class": "fas fa-sync-alt", "display_order": 6},
            ],
        },
        {
            "slug": "ai-machine-learning",
            "title": "AI & Machine Learning",
            "subtitle": "Deep dive into ML algorithms, neural networks, NLP, and computer vision with TensorFlow.",
            "description": "Explore the cutting edge of artificial intelligence and machine learning...",
            "definition": "Artificial Intelligence and Machine Learning are transforming every industry by enabling computers to learn from data...",
            "quote": "AI is the new electricity. Just as electricity transformed industry, AI will transform everything.",
            "duration_months": 6,
            "num_projects": 5,
            "badge": None,
            "icon_class": "fas fa-brain",
            "curriculum": [
                {"title": "Mathematics for ML", "description": "Linear algebra, calculus, statistics"},
                {"title": "ML Algorithms", "description": "Regression, classification, clustering"},
                {"title": "Neural Networks", "description": "CNN, RNN, backpropagation"},
                {"title": "TensorFlow & Keras", "description": "Building, training, deploying models"},
                {"title": "NLP & Transformers", "description": "BERT, GPT, sentiment analysis"},
                {"title": "Computer Vision", "description": "OpenCV, object detection, image segmentation"},
            ],
            "career_outcomes": [
                "Build and deploy machine learning models",
                "Work with neural networks and deep learning",
                "Implement natural language processing solutions",
                "Develop computer vision applications",
                "Deploy ML models to production",
                "Solve real-world problems with AI",
            ],
            "history": "Artificial Intelligence has evolved from theoretical concepts to practical applications that impact daily life...",
            "display_order": 5,
            "modules": [
                {"title": "Mathematics for ML", "description": "Build foundations with linear algebra, calculus, probability, and statistics.", "icon_class": "fas fa-square-root-alt", "display_order": 1},
                {"title": "ML Algorithms", "description": "Master regression, classification, clustering, and ensemble methods.", "icon_class": "fas fa-project-diagram", "display_order": 2},
                {"title": "Neural Networks", "description": "Understand CNN, RNN, LSTM, and backpropagation in depth.", "icon_class": "fas fa-network-wired", "display_order": 3},
                {"title": "TensorFlow & Keras", "description": "Build, train, and deploy deep learning models with TensorFlow.", "icon_class": "fas fa-cogs", "display_order": 4},
                {"title": "NLP & Transformers", "description": "Explore BERT, GPT, sentiment analysis, and language models.", "icon_class": "fas fa-language", "display_order": 5},
                {"title": "Computer Vision", "description": "Work with OpenCV, object detection, and image segmentation.", "icon_class": "fas fa-eye", "display_order": 6},
            ],
        },
        {
            "slug": "app-development",
            "title": "App Development",
            "subtitle": "Build cross-platform mobile apps with Flutter, React Native, and Kotlin.",
            "description": "Create stunning mobile applications for iOS and Android...",
            "definition": "Mobile app development is the process of creating software applications that run on mobile devices...",
            "quote": "Mobile is not just a channel — it's the primary way people interact with technology.",
            "duration_months": 5,
            "num_projects": 4,
            "badge": None,
            "icon_class": "fas fa-mobile-alt",
            "curriculum": [
                {"title": "Flutter & Dart", "description": "Cross-platform native apps"},
                {"title": "React Native", "description": "Cross-platform, native features"},
                {"title": "Kotlin / Android", "description": "Jetpack Compose, Material Design"},
                {"title": "UI/UX Design", "description": "Figma, wireframing, prototyping"},
                {"title": "Firebase & Backend", "description": "Auth, DB, push notifications"},
                {"title": "App Store Deployment", "description": "Google Play, Apple App Store"},
            ],
            "career_outcomes": [
                "Build cross-platform mobile applications",
                "Design intuitive user interfaces",
                "Implement push notifications and real-time features",
                "Deploy apps to App Store and Google Play",
                "Integrate backend services with mobile apps",
                "Create engaging user experiences",
            ],
            "history": "Mobile app development has grown from simple utilities to sophisticated platforms that power modern business...",
            "display_order": 6,
            "modules": [
                {"title": "Flutter & Dart", "description": "Build beautiful cross-platform apps with Flutter and Dart programming.", "icon_class": "fab fa-flutter", "display_order": 1},
                {"title": "React Native", "description": "Create native mobile apps using React Native framework.", "icon_class": "fab fa-react", "display_order": 2},
                {"title": "Kotlin / Android", "description": "Develop Android apps with Kotlin and Jetpack Compose.", "icon_class": "fab fa-android", "display_order": 3},
                {"title": "UI/UX Design", "description": "Design stunning interfaces with Figma, wireframing, and prototyping.", "icon_class": "fab fa-figma", "display_order": 4},
                {"title": "Firebase & Backend", "description": "Integrate auth, databases, and push notifications with Firebase.", "icon_class": "fas fa-fire", "display_order": 5},
                {"title": "App Store Deployment", "description": "Deploy to Google Play and Apple App Store with confidence.", "icon_class": "fab fa-apple", "display_order": 6},
            ],
        },
    ]

    for course_data in courses_data:
        modules_list = course_data.pop("modules", [])
        course = Course(**course_data)
        db.session.add(course)
        db.session.flush()

        for mod_data in modules_list:
            module = Module(course_id=course.id, **mod_data)
            db.session.add(module)

    # Services
    services_data = [
        {"title": "Software Training", "description": "Hands-on training in programming languages, frameworks, and tools used by top tech companies worldwide.", "icon_class": "fas fa-chalkboard-teacher", "display_order": 1},
        {"title": "Placement Assistance", "description": "Job-ready support with resume building, mock interviews, and direct connections to our hiring partner network.", "icon_class": "fas fa-briefcase", "display_order": 2},
        {"title": "Online Courses", "description": "Flexible, self-paced online courses that let you learn from anywhere, anytime with expert mentor support.", "icon_class": "fas fa-globe", "display_order": 3},
        {"title": "Corporate Training", "description": "Tailored training programs for organizations to upskill their teams in the latest technologies and best practices.", "icon_class": "fas fa-building", "display_order": 4},
        {"title": "Internships", "description": "Real-world internship opportunities with live projects to build your portfolio and gain practical experience.", "icon_class": "fas fa-user-graduate", "display_order": 5},
        {"title": "Certifications", "description": "Industry-recognized certifications that validate your skills and boost your credibility in the job market.", "icon_class": "fas fa-certificate", "display_order": 6},
    ]
    for s in services_data:
        db.session.add(Service(**s))

    # Testimonials
    testimonials_data = [
        {"student_name": "Rahul Sharma", "initials": "RS", "role": "Software Engineer at TechCorp", "quote": "2K Solutions completely changed my career trajectory. The hands-on projects and mentor guidance helped me land my dream job at a top tech company.", "rating": 5, "display_order": 1},
        {"student_name": "Priya Verma", "initials": "PV", "role": "Data Analyst at DataWorks", "quote": "The data analytics course was incredibly well-structured. I went from knowing nothing to working as a Data Analyst in just 5 months.", "rating": 5, "display_order": 2},
        {"student_name": "Arjun Kumar", "initials": "AK", "role": "Full-Stack Developer at WebStudio", "quote": "What sets 2K apart is the placement support. They didn't just teach me — they prepared me for interviews, reviewed my resume, and connected me with employers.", "rating": 5, "display_order": 3},
    ]
    for t in testimonials_data:
        db.session.add(Testimonial(**t))

    # FAQs
    faqs_data = [
        {"question": "Who can enroll in 2K Solutions courses?", "answer": "Anyone with a passion for technology can enroll! Whether you're a student, graduate, or working professional looking to upskill, our courses are designed for all levels — from complete beginners to advanced learners.", "display_order": 1},
        {"question": "Do you provide placement assistance?", "answer": "Yes! We have a dedicated placement cell that provides resume building, mock interviews, aptitude training, and direct referrals to our network of 50+ hiring partner companies. Our placement rate is 95%.", "display_order": 2},
        {"question": "Are the courses online or classroom-based?", "answer": "We offer both options! You can choose from fully online, in-person classroom, or hybrid modes based on your preference and convenience.", "display_order": 3},
        {"question": "What is the duration of the courses?", "answer": "Course durations range from 3 to 6 months depending on the program. Each course includes theory, hands-on labs, projects, and placement preparation.", "display_order": 4},
        {"question": "Do I get a certificate after completion?", "answer": "Absolutely! Upon successful completion, you will receive an industry-recognized certificate from 2K Solutions that validates your skills and knowledge.", "display_order": 5},
    ]
    for f in faqs_data:
        db.session.add(FAQ(**f))

    # Technologies
    technologies_data = [
        {"name": "Python", "icon_class": "fab fa-python", "display_order": 1},
        {"name": "Java", "icon_class": "fab fa-java", "display_order": 2},
        {"name": "JavaScript", "icon_class": "fab fa-js", "display_order": 3},
        {"name": "React", "icon_class": "fab fa-react", "display_order": 4},
        {"name": "Node.js", "icon_class": "fab fa-node", "display_order": 5},
        {"name": "AWS", "icon_class": "fab fa-aws", "display_order": 6},
        {"name": "Docker", "icon_class": "fab fa-docker", "display_order": 7},
        {"name": "SQL", "icon_class": "fas fa-database", "display_order": 8},
        {"name": "Angular", "icon_class": "fab fa-angular", "display_order": 9},
        {"name": "Vue.js", "icon_class": "fab fa-vuejs", "display_order": 10},
        {"name": "Git", "icon_class": "fab fa-git-alt", "display_order": 11},
        {"name": "Azure", "icon_class": "fab fa-microsoft", "display_order": 12},
        {"name": "Figma", "icon_class": "fab fa-figma", "display_order": 13},
        {"name": "ML/AI", "icon_class": "fas fa-brain", "display_order": 14},
        {"name": "Android", "icon_class": "fab fa-android", "display_order": 15},
        {"name": "iOS", "icon_class": "fab fa-apple", "display_order": 16},
    ]
    for tech in technologies_data:
        db.session.add(Technology(**tech))

    # Milestones (Hero section)
    hero_milestones = [
        {"label": "Students Trained", "value": 500, "icon_class": "fas fa-user-graduate", "section": "hero", "display_order": 1},
        {"label": "Placement Rate %", "value": 95, "icon_class": "fas fa-briefcase", "section": "hero", "display_order": 2},
        {"label": "Expert Mentors", "value": 50, "icon_class": "fas fa-chalkboard-teacher", "section": "hero", "display_order": 3},
        {"label": "Hiring Partners", "value": 30, "icon_class": "fas fa-handshake", "section": "hero", "display_order": 4},
    ]
    for m in hero_milestones:
        db.session.add(Milestone(**m))

    # Milestones (Achievements section)
    achievement_milestones = [
        {"label": "Students Trained", "value": 500, "icon_class": "fas fa-user-graduate", "section": "milestones", "display_order": 1},
        {"label": "Placement Rate %", "value": 95, "icon_class": "fas fa-briefcase", "section": "milestones", "display_order": 2},
        {"label": "Expert Mentors", "value": 50, "icon_class": "fas fa-chalkboard-teacher", "section": "milestones", "display_order": 3},
        {"label": "Hiring Partners", "value": 30, "icon_class": "fas fa-handshake", "section": "milestones", "display_order": 4},
        {"label": "Awards Won", "value": 15, "icon_class": "fas fa-award", "section": "milestones", "display_order": 5},
        {"label": "Live Projects", "value": 200, "icon_class": "fas fa-laptop", "section": "milestones", "display_order": 6},
    ]
    for m in achievement_milestones:
        db.session.add(Milestone(**m))

    # Steps
    steps_data = [
        {"step_number": 1, "title": "Assessment & Goal Setting", "description": "We evaluate your current skills, understand your career goals, and create a personalized learning roadmap.", "icon_class": "fas fa-clipboard-list"},
        {"step_number": 2, "title": "Foundations Training", "description": "Build strong fundamentals with structured courses, hands-on labs, and guided practice sessions.", "icon_class": "fas fa-book-open"},
        {"step_number": 3, "title": "Live Projects", "description": "Apply your skills to real-world projects that simulate actual industry scenarios and challenges.", "icon_class": "fas fa-project-diagram"},
        {"step_number": 4, "title": "Certification", "description": "Earn industry-recognized certifications that validate your expertise and boost your resume.", "icon_class": "fas fa-certificate"},
        {"step_number": 5, "title": "Placement Support", "description": "Get interview training, resume reviews, and direct referrals to our network of hiring partners.", "icon_class": "fas fa-briefcase"},
    ]
    for s in steps_data:
        db.session.add(Step(**s))

    # Differentiators
    differentiators_data = [
        {"number": 1, "title": "Expert Mentors", "description": "Learn from industry professionals with 8+ years of experience at top tech companies.", "icon_class": "fas fa-users", "display_order": 1},
        {"number": 2, "title": "Live Projects", "description": "Work on real-world projects that build your portfolio and demonstrate your skills.", "icon_class": "fas fa-code-branch", "display_order": 2},
        {"number": 3, "title": "Placement Guarantee", "description": "95% placement rate with our extensive network of 50+ hiring partner companies.", "icon_class": "fas fa-handshake", "display_order": 3},
        {"number": 4, "title": "Updated Curriculum", "description": "Courses constantly updated to match the latest industry trends and technology demands.", "icon_class": "fas fa-sync-alt", "display_order": 4},
        {"number": 5, "title": "Flexible Learning", "description": "Choose between classroom, online, or hybrid modes to fit your schedule.", "icon_class": "fas fa-clock", "display_order": 5},
        {"number": 6, "title": "Certification", "description": "Earn industry-recognized certificates that add value to your resume and career.", "icon_class": "fas fa-award", "display_order": 6},
    ]
    for d in differentiators_data:
        db.session.add(Differentiator(**d))

    # Site Settings
    site_settings = SiteSetting(
        brand_name="2K Solutions",
        tagline="Empowering Tech Careers",
        address="123 Tech Park, Cyber City\nHyderabad, Telangana 500081",
        phone="+91 98765 43210",
        email="info@2ksolutions.com",
        working_hours="Mon-Sat: 9AM - 7PM",
        social_links={
            "facebook": "#",
            "instagram": "#",
            "linkedin": "#",
            "youtube": "#",
            "twitter": "#",
        },
        copyright_year=2026,
    )
    db.session.add(site_settings)

    db.session.commit()
    print("Database seeded successfully!")


def run_seed() -> None:
    from app import create_app
    app = create_app()
    with app.app_context():
        seed_database()


if __name__ == "__main__":
    run_seed()
