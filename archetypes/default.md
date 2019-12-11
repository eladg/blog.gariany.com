---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
categories: [""]
tags: ["", ""]
discussionId: "{{ replace .Name " " "-" }}"
dont_show_comments: true
---