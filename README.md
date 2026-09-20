Pasted markdown.md
File
why it shows only the few months , i wnat that the streak should be shows form the januaray 2026 to till the date and next uposmog added on it , 




Yes — the issue is in your custom SVG generation, not the GitHub contribution data.

Your README currently embeds this custom file:

<img width="98%" src="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-contrib-6mo.svg" />

and the SVG itself is explicitly configured as 6 months, which is why it starts around March 2026 instead of January. Your README also labels it as 6 months.

What you want

You want the graph to:

Start: January 1, 2026
End: today's date — September 20, 2026
Show every month: Jan → Feb → Mar → Apr → May → Jun → Jul → Aug → Sep
Automatically extend as new contributions are made.
On October 1, October should appear automatically.
On January 1, 2027, the graph should continue into 2027.
Keep your current green/black design.
Keep the graph clean and not overcrowded.

GitHub's contribution calendar itself is based on contribution activity and is updated as contributions occur.

Important change

Instead of hardcoding:

6mo

make your generator calculate:

January 1, 2026 → current date

and dynamically generate the month labels.

For example, the graph should currently look conceptually like:

Contribution Graph

2026
Jan   Feb   Mar   Apr   May   Jun   Jul   Aug   Sep
│     │     │     │     │     │     │     │     │
●─────●─────●─────●─────●─────●─────●─────●─────●
                                              ↑
                                           TODAY

Then tomorrow/new contributions simply extend/update the graph.

Your README does NOT need a major change

Keep:

<img width="98%" src="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-contrib-6mo.svg" alt="6-month contribution graph" />

but I'd rename the generated file to something like:

<img width="98%" src="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-contrib-2026.svg" alt="2026 contribution graph" />

The real fix needs to happen in the GitHub Action/script that generates github-contrib-6mo.svg.

If you send me your .github/workflows/...yml and the script that generates github-contrib-6mo.svg, I can give you the exact code changes so it automatically runs Jan 1 → today → keeps extending every day.

so give em the upaded readme .md whole code with new update

Yes. I’ve updated the README so the contribution section is intended to show January 2026 → current date, rather than labeling it as a 6-month graph.

One important point: README alone cannot change the actual dates inside github-contrib-6mo.svg. The SVG generator/workflow must also generate the Jan-2026-to-current graph. I’ve updated the README naming/labels so it is ready for that.

Here is the complete updated README.md:

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:006D32,100:00FF41&height=200&section=header&text=Keshav%20Jha&fontSize=62&fontColor=FFFFFF&animation=fadeIn&fontAlignY=32&desc=Full-Stack%20Developer%20%20%E2%80%A2%20%20AI%20Enthusiast%20%20%E2%80%A2%20%20Automation%20Builder&descAlignY=53&descSize=16" width="100%" alt="header" />
</div>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=700&color=00FF41&center=true&vCenter=true&width=720&height=48&lines=root%40keshav%3A~%24+whoami;%3E+Full-Stack+Developer+%7C+MERN+%2B+Next.js+%2B+Django;%3E+AI+%26+Automation+Enthusiast;%3E+Open+Source+Contributor;%3E+Always+learning.+Always+shipping." alt="typing" />
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/keshavjha005" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>

  <a href="https://portfolio-keshav-eight.vercel.app/" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-00FF41?style=for-the-badge&logo=vercel&logoColor=0D1117" />
  </a>

  <a href="https://hashnode.com/@keshavBlog" target="_blank">
    <img src="https://img.shields.io/badge/Hashnode-2962FF?style=for-the-badge&logo=hashnode&logoColor=white" />
  </a>

  <a href="https://topmate.io/keshavjha005" target="_blank">
    <img src="https://img.shields.io/badge/Topmate-FF6F61?style=for-the-badge&logo=topmate&logoColor=white" />
  </a>

  <a href="https://author.envato.com/profile/onboarding" target="_blank">
    <img src="https://img.shields.io/badge/Envato-82B541?style=for-the-badge&logo=envato&logoColor=white" />
  </a>

  <a href="https://www.buymeacoffee.com/jharajiv92n" target="_blank">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FF813F?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white" />
  </a>
</div>

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=keshavjha005&label=PROFILE+VIEWS&color=00FF41&style=for-the-badge&abbreviated=true" />
  <img src="https://img.shields.io/github/followers/keshavjha005?label=FOLLOWERS&style=for-the-badge&color=00FF41&labelColor=0D1117&logo=github" />
  <img src="https://img.shields.io/badge/STATUS-BUILDING-00FF41?style=for-the-badge&labelColor=0D1117" />
</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />

## `$ cat about-me.txt`

<img align="right" width="380" src="https://user-images.githubusercontent.com/112645121/213100923-5b225bd3-b2eb-4e9f-b486-a5f2e7ea1ae9.png" alt="coding" />

```js
const keshav = {
  location:  "India 🇮🇳",
  role:      "Full-Stack Developer",
  obsession: "Clean architecture + AI automation",

  stack: {
    frontend: ["React", "Next.js", "Redux", "TailwindCSS"],
    backend:  ["Node.js", "Express", "Django"],
    database: ["MongoDB", "PostgreSQL", "MySQL"],
    cloud:    ["AWS", "GCP", "Vercel", "CI/CD"],
    ai:       ["OpenAI API", "LangChain", "n8n", "Prompt Eng."]
  },

  currentlyBuilding: "AI-powered products & workflow automations",
  currentlyLearning: "System Design · LLM Agents · Scalable Backends",
  openTo:            ["Collaboration", "Freelance", "Open Source"],

  motto: () => "Break it. Fix it. Ship it. Repeat."
};
┌──(keshav㉿github)-[~]
└─$ sudo ./launch.sh --mode=build --coffee=∞
[✔] Frontend  ......... online
[✔] Backend   ......... online
[✔] AI Agents ......... online
[✔] Bugs      ......... "features", actually
<br clear="right" /> <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />
$ ls -la ./tech-stack
<div align="center">

📘 CS FUNDAMENTALS

DSA • OS • CN • RESTful API • HLD • LLD • SDLC • Agile • A/B Testing • SEO

<br/>

💻 LANGUAGES

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" /> <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" /> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" /> <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" /> <br/>

🎨 FRONTEND

<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /> <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" /> <img src="https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=redux&logoColor=white" /> <img src="https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" /> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" /> <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" /> <img src="https://img.shields.io/badge/Webpack-8DD6F9?style=for-the-badge&logo=webpack&logoColor=black" /> <br/>

⚙️ BACKEND

<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" /> <img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white" /> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" /> <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" /> <br/>

🤖 AI · ML · AUTOMATION

<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" /> <img src="https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" /> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" /> <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" /> <img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" /> <img src="https://img.shields.io/badge/Prompt%20Engineering-00FF41?style=for-the-badge&logo=probot&logoColor=0D1117" /> <br/>

🗄️ DATABASE

<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" /> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" /> <br/>

🧪 TESTING

<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" /> <img src="https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" /> <img src="https://img.shields.io/badge/Jest-C21325?style=for-the-badge&logo=jest&logoColor=white" /> <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" /> <br/>

🛠️ TOOLS & CLOUD

<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" /> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /> <img src="https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white" /> <img src="https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" /> <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" /> <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white" /> <img src="https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white" /> <img src="https://img.shields.io/badge/Google%20Analytics-E37400?style=for-the-badge&logo=googleanalytics&logoColor=white" /> </div> <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />
$ git log --stat --graph
<div align="center"> <img height="170" src="https://streak-stats.demolab.com?user=keshavjha005&hide_border=false&background=0D1117&stroke=00FF41&ring=00FF41&fire=00FF41&currStreakLabel=00FF41&sideLabels=C9D1D9&currStreakNum=FFFFFF&sideNums=FFFFFF&dates=8B949E&border=00FF41" />

<br/><br/>

<!-- CONTRIBUTION GRAPH Range: January 1, 2026 → Current Date The SVG is generated automatically by the repository workflow. -->

<img width="98%" src="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-contrib-2026.svg" alt="GitHub contribution graph from January 2026 to current date" />

</div>
📅 Contribution Activity
<div align="center">

January 2026 → Present

<br/> <sub> Contribution activity starts from January 2026 and continues to update as new contributions are added. </sub> </div> <br/> <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />
🐍 Contribution Snake
<div align="center">

<code>📅 January 2026 → Present</code>

  

<img src="https://img.shields.io/github/last-commit/keshavjha005/keshavjha005/output?label=LAST%20SYNCED&style=flat-square&color=00FF41&labelColor=0D1117&logo=github" />

<br/><br/>

<picture> <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-snake-dark.svg" />

<source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-snake.svg" />

<img alt="GitHub contribution snake" src="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-snake.svg" />
</picture>

</div> <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />
$ curl -X GET /connect
<div align="center">
> Open to: Freelance · Collaboration · Open Source · Mentorship
> Response time: usually < 24h
<a href="https://www.linkedin.com/in/keshavjha005" target="_blank"> <img src="https://img.shields.io/badge/Let's%20Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /> </a> <a href="https://topmate.io/keshavjha005" target="_blank"> <img src="https://img.shields.io/badge/Book%20a%20Call-FF6F61?style=for-the-badge&logo=topmate&logoColor=white" /> </a> <a href="https://portfolio-keshav-eight.vercel.app/" target="_blank"> <img src="https://img.shields.io/badge/See%20My%20Work-00FF41?style=for-the-badge&logo=vercel&logoColor=0D1117" /> </a> </div> <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />
$ sudo apt install coffee
<div align="center"> <table> <tr> <td align="center" width="50%"> <h3>☕ Fuel the Build</h3> <a href="https://buymeacoffee.com/jharajiv92n" target="_blank"> <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="48" alt="Buy Me A Coffee" /> </a>

<br/><br/>

<img src="https://drive.google.com/uc?export=view&id=1kp4gjn7uDDq3OKDwz8A94bWATDb5wRpV" alt="Scan to support" width="180" />

</td> <td align="center" width="50%"> <h3>💥 Keep exploring, keep building 💥</h3>

<img src="https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif" width="280" />

</td> </tr> </table> </div> <div align="center">
"Code with purpose. Learn continuously. Ship confidently."
"Ek din code yahi reh jayega... aur main push ho jaunga. 🚀"

⭐ If any of my repos helped you, drop a star — it genuinely helps.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FF41,50:006D32,100:0D1117&height=120&section=footer" width="100%" alt="footer" />

</div> ```
⚠️ One thing you must change outside README

Your old README points to:

github-contrib-6mo.svg

I changed it to:

github-contrib-2026.svg

So your repository must actually generate:

output/
└── github-contrib-2026.svg

with the range:

2026-01-01 → today

Otherwise the new image will show as broken.

The next thing I recommend is updating your GitHub Action/script that generates the SVG. That's what will make the graph automatically go:

Jan → Feb → Mar → Apr → May → Jun → Jul → Aug → Sep → Oct → Nov → Dec → 2027...

without you manually changing the README every month.

Meet Codex in the desktop app
A coding agent that helps you build and ship with AI, included for free in your ChatGPT plan.
Download the app
Learn more

<div align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:006D32,100:00FF41&height=200&section=header&text=Keshav%20Jha&fontSize=62&fontColor=FFFFFF&animation=fadeIn&fontAlignY=32&desc=Full-Stack%20Developer%20%20%E2%80%A2%20%20AI%20Enthusiast%20%20%E2%80%A2%20%20Automation%20Builder&descAlignY=53&descSize=16" width="100%" alt="header" /> </div>

<div align="center"> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=700&color=00FF41&center=true&vCenter=true&width=720&height=48&lines=root%40keshav%3A~%24+whoami;%3E+Full-Stack+Developer+%7C+MERN+%2B+Next.js+%2B+Django;%3E+AI+%26+Automation+Enthusiast;%3E+Open+Source+Contributor;%3E+Always+learning.+Always+shipping." alt="typing" /> </div>

<div align="center"> <a href="https://www.linkedin.com/in/keshavjha005" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a> <a href="https://portfolio-keshav-eight.vercel.app/" target="_blank"><img src="https://img.shields.io/badge/Portfolio-00FF41?style=for-the-badge&logo=vercel&logoColor=0D1117" /></a> <a href="https://hashnode.com/@keshavBlog" target="_blank"><img src="https://img.shields.io/badge/Hashnode-2962FF?style=for-the-badge&logo=hashnode&logoColor=white" /></a> <a href="https://topmate.io/keshavjha005" target="_blank"><img src="https://img.shields.io/badge/Topmate-FF6F61?style=for-the-badge&logo=topmate&logoColor=white" /></a> <a href="https://author.envato.com/profile/onboarding" target="_blank"><img src="https://img.shields.io/badge/Envato-82B541?style=for-the-badge&logo=envato&logoColor=white" /></a> <a href="https://www.buymeacoffee.com/jharajiv92n" target="_blank"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FF813F?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white" /></a> </div>

<div align="center"> <img src="https://komarev.com/ghpvc/?username=keshavjha005&label=PROFILE+VIEWS&color=00FF41&style=for-the-badge&abbreviated=true" /> <img src="https://img.shields.io/github/followers/keshavjha005?label=FOLLOWERS&style=for-the-badge&color=00FF41&labelColor=0D1117&logo=github" /> <img src="https://img.shields.io/badge/STATUS-BUILDING-00FF41?style=for-the-badge&labelColor=0D1117" /> </div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />

$ cat about-me.txt

<img align="right" width="380" src="https://user-images.githubusercontent.com/112645121/213100923-5b225bd3-b2eb-4e9f-b486-a5f2e7ea1ae9.png" alt="coding" />

const keshav = {
  location:  "India 🇮🇳",
  role:      "Full-Stack Developer",
  obsession: "Clean architecture + AI automation",

  stack: {
    frontend: ["React", "Next.js", "Redux", "TailwindCSS"],
    backend:  ["Node.js", "Express", "Django"],
    database: ["MongoDB", "PostgreSQL", "MySQL"],
    cloud:    ["AWS", "GCP", "Vercel", "CI/CD"],
    ai:       ["OpenAI API", "LangChain", "n8n", "Prompt Eng."]
  },

  currentlyBuilding: "AI-powered products & workflow automations",
  currentlyLearning: "System Design · LLM Agents · Scalable Backends",
  openTo:            ["Collaboration", "Freelance", "Open Source"],

  motto: () => "Break it. Fix it. Ship it. Repeat."
};
┌──(keshav㉿github)-[~]
└─$ sudo ./launch.sh --mode=build --coffee=∞
[✔] Frontend  ......... online
[✔] Backend   ......... online
[✔] AI Agents ......... online
[✔] Bugs      ......... "features", actually

<br clear="right" />

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />

$ ls -la ./tech-stack

<div align="center">

📘 CS FUNDAMENTALS

DSA • OS • CN • RESTful API • HLD • LLD • SDLC • Agile • A/B Testing • SEO

<br/>

💻 LANGUAGES
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
<br/>

🎨 FRONTEND

<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /> <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" /> <img src="https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=redux&logoColor=white" /> <img src="https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" /> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" /> <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" /> <img src="https://img.shields.io/badge/Webpack-8DD6F9?style=for-the-badge&logo=webpack&logoColor=black" />

<br/>

⚙️ BACKEND

<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" /> <img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white" /> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" /> <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" />

<br/>

🤖 AI · ML · AUTOMATION

<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" /> <img src="https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" /> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" /> <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" /> <img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" /> <img src="https://img.shields.io/badge/Prompt%20Engineering-00FF41?style=for-the-badge&logo=probot&logoColor=0D1117" />

<br/>

🗄️ DATABASE

<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" /> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" />

<br/>

🧪 TESTING

<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" /> <img src="https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" /> <img src="https://img.shields.io/badge/Jest-C21325?style=for-the-badge&logo=jest&logoColor=white" /> <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" />

<br/>

🛠️ TOOLS & CLOUD

<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" /> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /> <img src="https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white" /> <img src="https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" /> <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" /> <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white" /> <img src="https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white" /> <img src="https://img.shields.io/badge/Google%20Analytics-E37400?style=for-the-badge&logo=googleanalytics&logoColor=white" />

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />

$ git log --stat --graph

<div align="center">

<img height="170" src="https://streak-stats.demolab.com?user=keshavjha005&hide_border=false&background=0D1117&stroke=00FF41&ring=00FF41&fire=00FF41&currStreakLabel=00FF41&sideLabels=C9D1D9&currStreakNum=FFFFFF&sideNums=FFFFFF&dates=8B949E&border=00FF41" />

<br/><br/>




<!-- ✅ NEW — self-generated, 6 months, month labels -->

<img width="98%" src="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-contrib-6mo.svg" alt="6-month contribution graph" />

</div>

🐍 Contribution Snake

<div align="center">

<code>📅 <!--SNAKE_RANGE-->21 Sep 2025 → 20 Sep 2026<!--/SNAKE_RANGE--></code>
  
<img src="https://img.shields.io/github/last-commit/keshavjha005/keshavjha005/output?label=LAST%20SYNCED&style=flat-square&color=00FF41&labelColor=0D1117&logo=github" />

<br/><br/>

<picture> <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-snake-dark.svg" /> <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-snake.svg" /> <img alt="github-snake" src="https://raw.githubusercontent.com/keshavjha005/keshavjha005/output/github-snake.svg" /> </picture>

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />

$ curl -X GET /connect

<div align="center">

> Open to: Freelance · Collaboration · Open Source · Mentorship
> Response time: usually < 24h

<a href="https://www.linkedin.com/in/keshavjha005" target="_blank"><img src="https://img.shields.io/badge/Let's%20Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="https://topmate.io/keshavjha005" target="_blank"><img src="https://img.shields.io/badge/Book%20a%20Call-FF6F61?style=for-the-badge&logo=topmate&logoColor=white" /></a>
<a href="https://portfolio-keshav-eight.vercel.app/" target="_blank"><img src="https://img.shields.io/badge/See%20My%20Work-00FF41?style=for-the-badge&logo=vercel&logoColor=0D1117" /></a>

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" />

$ sudo apt install coffee

<div align="center"> <table> <tr> <td align="center" width="50%"> <h3>☕ Fuel the Build</h3> <a href="https://buymeacoffee.com/jharajiv92n" target="_blank"> <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="48" alt="Buy Me A Coffee" /> </a> <br/><br/> <img src="https://drive.google.com/uc?export=view&id=1kp4gjn7uDDq3OKDwz8A94bWATDb5wRpV" alt="Scan to support" width="180"/> </td> <td align="center" width="50%"> <h3>💥 Keep exploring, keep building 💥</h3> <img src="https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif" width="280"> </td> </tr> </table> </div>

<div align="center">

""Code with purpose. Learn continuously. Ship confidently.""  
""Ek din code yahi reh jayega... aur main  push ho jaunga. 🚀""

⭐ If any of my repos helped you, drop a star — it genuinely helps.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FF41,50:006D32,100:0D1117&height=120&section=footer" width="100%" alt="footer" />

</div>

Close
