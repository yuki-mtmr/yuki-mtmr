<!-- このファイルは自動生成されています。直接編集しないでください。 -->
<!-- 変更する場合は profile-config.yaml を編集してください。 -->

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color={{ theme.accent_color|upper }}&center=true&vCenter=true&random=false&width=600&lines={{ user.title|urlencode }};{{ user.location|urlencode }})](https://git.io/typing-svg)

</div>

## 👋 About Me

<table>
<tr>
<td width="50%" valign="top">

```yaml
name: {{ user.name }}
location: {{ user.location }}
role: {{ user.title }}

current_focus:
  - Building modern web applications
  - Learning new technologies
  - Contributing to open source

interests:
  - Clean code & architecture
  - Developer experience
  - Performance optimization
```

</td>
<td width="50%" valign="top">

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username={{ user.github_username }}&show_icons=true&theme={{ theme.stats_theme }}&hide_border={{ theme.hide_border|lower }}&include_all_commits=true&count_private=true&bg_color=00000000)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={{ user.github_username }}&layout=compact&theme={{ theme.stats_theme }}&hide_border={{ theme.hide_border|lower }}&bg_color=00000000)

</div>

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

### Languages
[![Languages](https://skillicons.dev/icons?i={{ skills.languages|join(',') }})](https://skillicons.dev)

### Frontend
[![Frontend](https://skillicons.dev/icons?i={{ skills.frontend|join(',') }})](https://skillicons.dev)

### Backend
[![Backend](https://skillicons.dev/icons?i={{ skills.backend|join(',') }})](https://skillicons.dev)

### Infrastructure
[![Infrastructure](https://skillicons.dev/icons?i={{ skills.infrastructure|join(',') }})](https://skillicons.dev)

### Tools
[![Tools](https://skillicons.dev/icons?i={{ skills.tools|join(',') }})](https://skillicons.dev)

</div>

---

{% if rss.qiita or rss.zenn %}
## 📝 Latest Blog Posts

<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->

{% endif %}
---

## 🐍 Contribution Graph

<div align="center">

![Snake animation](https://raw.githubusercontent.com/{{ user.github_username }}/{{ user.github_username }}/output/github-contribution-grid-snake-dark.svg)

</div>

---

<div align="center">

{% if social.twitter %}[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/{{ social.twitter }}) {% endif %}{% if social.qiita %}[![Qiita](https://img.shields.io/badge/-Qiita-55C500?style=flat-square&logo=qiita&logoColor=white)](https://qiita.com/{{ social.qiita }}) {% endif %}{% if social.zenn %}[![Zenn](https://img.shields.io/badge/-Zenn-3EA8FF?style=flat-square&logo=zenn&logoColor=white)](https://zenn.dev/{{ social.zenn }}){% endif %}

![Profile Views](https://komarev.com/ghpvc/?username={{ user.github_username }}&color={{ theme.accent_color }}&style=flat-square)

</div>
