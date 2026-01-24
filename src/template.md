<!-- このファイルは自動生成されています。直接編集しないでください。 -->
<!-- 変更する場合は profile-config.yaml を編集してください。 -->

```
██╗   ██╗██╗   ██╗██╗  ██╗██╗
╚██╗ ██╔╝██║   ██║██║ ██╔╝██║
 ╚████╔╝ ██║   ██║█████╔╝ ██║
  ╚██╔╝  ██║   ██║██╔═██╗ ██║
   ██║   ╚██████╔╝██║  ██╗██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝
```

```
+------------------------------------------+
|  SYSTEM://PROFILE                        |
|  ========================================|
|                                          |
|  > name     : {{ user.name }}
|  > location : {{ user.location }}
|  > role     : {{ user.title }}
|  > status   : online                     |
|                                          |
|  "{{ user.tagline }}"
|                                          |
+------------------------------------------+
```

---

### `> cat /etc/skills/languages.conf`

```
{{ skills.languages | join(' // ') }}
```

### `> cat /etc/skills/frontend.conf`

```
{{ skills.frontend | join(' // ') }}
```

### `> cat /etc/skills/backend.conf`

```
{{ skills.backend | join(' // ') }}
```

### `> cat /etc/skills/infrastructure.conf`

```
{{ skills.infrastructure | join(' // ') }}
```

### `> cat /etc/skills/tools.conf`

```
{{ skills.tools | join(' // ') }}
```

---

### `> neofetch --github`

```
       ◢███████◣          yuki-mtmr@github
      ◢█████████◣         -----------------
     ◢███████████◣        Repos: 49+
    ◢█████████████◣       Followers: 11
   ◢██████ ◼ █████◣       Status: Building the Wired
  ◢███████████████◣
 ◢█████████████████◣      "No matter where you go,
◢████████▀▀▀████████◣      everyone's connected."
```

<details>
<summary><code>> stats --verbose</code></summary>
<br>

![GitHub Stats](https://github-readme-stats.vercel.app/api?username={{ user.github_username }}&show_icons=true&theme=dark&hide_border=true&bg_color=0d1117&title_color=00ff00&text_color=c9d1d9&icon_color=00ff00&include_all_commits=true&count_private=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={{ user.github_username }}&layout=compact&theme=dark&hide_border=true&bg_color=0d1117&title_color=00ff00&text_color=c9d1d9)

</details>

---

{% if rss.qiita or rss.zenn %}
### `> tail -f /var/log/blog.log`

<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->

---

{% endif %}
```
+------------------------------------------+
|  CONNECTION://CLOSED                     |
|  ========================================|
|                                          |
|  Present day, Present time. HAHAHA!      |
|                                          |
|  Layer:07 - PROTOCOL                     |
|                                          |
+------------------------------------------+
```

<sub>{{ user.github_username }} © MMXXV - You don't seem to understand.</sub>
