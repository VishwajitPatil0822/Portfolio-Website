# The Personal Portfolio Website
The Personal Portfolio Website is a professionally designed, web-based platform designed to showcase my projects, skills, academic achievements, and certifications in a clean and engaging format. Built with Django as the backend and a responsive frontend using HTML, CSS, JavaScript, and Bootstrap, this site offers visitors an intuitive and seamless browsing experience across all devices.

Whether potential employers, collaborators, or clients are exploring my technical expertise or looking to connect, the website provides a centralized and distraction-free environment. Highlighting live projects, detailed project galleries, academic qualifications, and certifications, it creates a strong and authentic digital presence. The site is supported by a PostgreSQL database to securely handle form submissions like contact queries, ensuring both efficiency and privacy without storing any unnecessary user data.

Designed with a modern aesthetic and user-friendly navigation, the portfolio features sections like About Me, Technologies & Skills, Live Projects, Academic Details, and Contact Me, allowing visitors to discover my professional journey effortlessly. Developed using PyCharm following clean, modular coding practices, the project is easy to maintain, scale, and update as new achievements are added.

Deployed globally using Vercel, the website ensures fast loading speeds, high availability, and smooth performance across devices. Designed with a focus on scalability, security, and user-centric design, it establishes a strong and credible online presence. The goal of this project is to create a professional digital platform that not only highlights my technical skills and achievements but also serves as a bridge to connect with potential employers, collaborators, and clients, opening doors to new career and growth opportunities.

<br>

## ✨ Features Of Personal Portfolio Website

- **Professional Introduction** - A clean and engaging hero section introducing the developer, including name, role, location, and a personal tagline to immediately establish connection.

- **Call-to-Action Buttons** -  Strategically placed "Hire Me" and "Download CV" buttons enabling visitors to initiate contact or access the most recent resume effortlessly.

- **Key Professional Metrics** - A summary of achievements highlighting the number of projects developed, live projects hosted, positive feedback percentage, and certifications earned.

- **About Me Section**  - A detailed narrative outlining the developer’s background, career journey, technical approach, and professional philosophy, crafted to leave a strong personal impression.

- **Technologies and Skills Overview** - A visually organized display of technical proficiencies across programming languages, frameworks, databases, tools, and platforms.

- **Live Projects Showcase** - Featured live projects with direct links to deployed applications, allowing visitors to experience working demos firsthand.

- **Comprehensive Projects Gallery** - A structured listing of all completed projects with descriptions and repository access, demonstrating a diverse range of development capabilities.

- **Academic Credentials** - A concise presentation of educational qualifications, institutions attended, and academic performance details to validate technical expertise.

- **Certifications Display** - A dedicated section listing professional certifications, including course providers, issue dates, and certificate IDs, reinforcing continuous learning and development.

- **Contact Information Panel** - Multiple channels provided for direct communication, including email, LinkedIn, GitHub, and WhatsApp, ensuring easy accessibility.

- **Secure Contact Form** - An integrated contact form backed by PostgreSQL for secure message submissions, facilitating seamless visitor inquiries while ensuring data privacy.

- **Django-Powered Backend** - Robust server-side management ensuring efficient handling of dynamic content and form submissions, with an emphasis on security and performance.

- **Responsive and Modern User Interface** - Designed with Bootstrap to ensure seamless navigation, mobile responsiveness, and compatibility across all major browsers.

- **Global Deployment via Vercel** - Hosted on Vercel to guarantee optimized performance, rapid loading times, and reliable global accessibility.

- **Clean, Modular Architecture** - Developed with a scalable, maintainable codebase using PyCharm, enabling easy future enhancements and customizations.

- **Goal-Driven Design Philosophy** - Purposefully built to establish a professional digital identity, showcase technical strengths, and open pathways to career opportunities, collaborations, and client engagements.

<br>

  ## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap  

- **Backend**: Python, Django  

- **Database**: PostgreSQL

- **IDE Used**: PyCharm

- **Deployment**: Vercel

<br>

## Screenshots

![Home Page](screenshots/home.png)

<br>

##  🧰  Installation & Setup

**1. Clone the Repository**

   ```
git clone https://github.com/VishwajitPatil0822/Portfolio-Website.git

   cd Portfolio-Website
   ```

**2. Create & Activate a Virtual Environment**

    python -m venv myvenv
    myvenv\Scripts\activate

**3. Install dependencies**

    pip install -r requirements.txt

**4. Configure PostgreSQL**

- Go to https://neon.tech
- Sign up for a free account using your email or GitHub
- After signing in, click “New Project”.
- Enter a project name, select your region, and click “Create Project”.
- Once your project is created, you will see your Database URL in the Connection Details tab. It will look something like this:

        postgres://username:password@your-db-host.neon.tech/dbname?sslmode=require

- Paste your PostgreSQL database URL like in ```.env``` file like this:

        DATABASE_URL=postgres://username:password@your-db-host.neon.tech/dbname?sslmode=require

**5. Run Migrations**

        python manage.py migrate

**6. Start the Development Server**

        python manage.py runserver

<br>

## 📬 Contact

If you have any questions, suggestions, or want to collaborate, feel free to reach out:

- 💌 Email: [vishwajit22patil@gmail.com](mailto:vishwajit22patil@gmail.com)

- 🐙 GitHub: [github.com/VishwajitPatil0822](https://github.com/VishwajitPatil0822)

- 💼 LinkedIn: [linkedin.com/in/vishwajitpatil-pythondev](https://www.linkedin.com/in/vishwajitpatil-pythondev/)

- 🌐 Portfolio: [vishwajit-patil-portfolio.vercel.app](https://vishwajit-patil-portfolio.vercel.app/)
 
<br>

## ❤️ Support

If you like this project, give it a ⭐ on [GitHub](https://github.com/VishwajitPatil0822/Portfolio-Website)!  
You can also share it with your friends.

Thank you for checking it out! 🚀


### Created with ❤️ by Vishwajit Patil
