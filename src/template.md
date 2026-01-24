<!-- このファイルは自動生成されています。直接編集しないでください。 -->
<!-- 変更する場合は profile-config.yaml を編集してください。 -->

## Hi there 👋

{{ user.bio }}

### About Me

- 🔭 **{{ user.title }}** based in {{ user.location }}
- 🌱 Currently focused on Web Development & AI Engineering
- 💬 Ask me about **{{ skills.languages[:3] | join(', ') }}**

---

### Tech Stack

<p>
  <img alt="Python" src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img alt="TypeScript" src="https://img.shields.io/badge/-TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white" />
  <img alt="Ruby" src="https://img.shields.io/badge/-Ruby-CC342D?style=flat-square&logo=ruby&logoColor=white" />
  <img alt="Java" src="https://img.shields.io/badge/-Java-007396?style=flat-square&logo=openjdk&logoColor=white" />
  <img alt="JavaScript" src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
</p>
<p>
  <img alt="React" src="https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black" />
  <img alt="Vue.js" src="https://img.shields.io/badge/-Vue.js-4FC08D?style=flat-square&logo=vue.js&logoColor=white" />
  <img alt="Rails" src="https://img.shields.io/badge/-Rails-CC0000?style=flat-square&logo=rubyonrails&logoColor=white" />
  <img alt="Django" src="https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white" />
  <img alt="Spring" src="https://img.shields.io/badge/-Spring-6DB33F?style=flat-square&logo=spring&logoColor=white" />
  <img alt="Node.js" src="https://img.shields.io/badge/-Node.js-339933?style=flat-square&logo=node.js&logoColor=white" />
</p>
<p>
  <img alt="Docker" src="https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img alt="AWS" src="https://img.shields.io/badge/-AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" />
  <img alt="GCP" src="https://img.shields.io/badge/-GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white" />
  <img alt="MySQL" src="https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" />
  <img alt="Git" src="https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white" />
  <img alt="Linux" src="https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
</p>

---

### GitHub Stats

<p>
  <img height="170" src="https://github-readme-stats.vercel.app/api?username={{ user.github_username }}&show_icons=true&theme=default&hide_border=true&include_all_commits=true&count_private=true" />
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username={{ user.github_username }}&layout=compact&theme=default&hide_border=true" />
</p>

---

{% if social.twitter or social.qiita or social.zenn %}
### Connect

<p>
{% if social.twitter %}  <a href="https://twitter.com/{{ social.twitter }}"><img alt="Twitter" src="https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white" /></a>
{% endif %}{% if social.qiita %}  <a href="https://qiita.com/{{ social.qiita }}"><img alt="Qiita" src="https://img.shields.io/badge/-Qiita-55C500?style=flat-square&logo=qiita&logoColor=white" /></a>
{% endif %}{% if social.zenn %}  <a href="https://zenn.dev/{{ social.zenn }}"><img alt="Zenn" src="https://img.shields.io/badge/-Zenn-3EA8FF?style=flat-square&logo=zenn&logoColor=white" /></a>
{% endif %}</p>

---

{% endif %}
![](https://komarev.com/ghpvc/?username={{ user.github_username }}&color=blue&style=flat)
