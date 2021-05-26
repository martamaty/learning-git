
# blog/templates/homepage.html

{% extends "base.html" %}

{% block content %}

{% for post in all_posts %}

<div>
   <div>
       <h2 class="d-inline-block">{{ post.title }}</h2>
       <a href="{{ url_for('edit_entry', entry_id=post.id) }}">

       <svg class="bi bi-pencil float-right" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
           <path fill-rule="evenodd" d="M11.293 1.293a1 1 0 0 1 1.414 0l2 2a1 1 0 0 1 0 1.414l-9 9a1 1 0 0 1-.39.242l-3 1a1 1 0 0 1-1.266-1.265l1-3a1 1 0 0 1 .242-.391l9-9zM12 2l2 2-9 9-3 1 1-3 9-9z"/>
           <path fill-rule="evenodd" d="M12.146 6.354l-2.5-2.5.708-.708 2.5 2.5-.707.708zM3 10v.5a.5.5 0 0 0 .5.5H4v.5a.5.5 0 0 0 .5.5H5v.5a.5.5 0 0 0 .5.5H6v-1.5a.5.5 0 0 0-.5-.5H5v-.5a.5.5 0 0 0-.5-.5H3z"/>
         </svg>
       </a>
   </div>
   <p>{{ post.pub_date.strftime('%Y-%m-%d') }} </p>
   <p>
       {{ post.body}}
   </p>
</div>

{% endfor %}
{% endblock %}
{% extends "base.html" %}

{% block content %}
<h3>
   Dodaj nowy wpis
</h3>

<form action="" method="POST">
  {{form.hidden_tag()}}
   <div class="form-group">
       <label for="title">Tytuł wpisu</label>
       {{ form.title(class_="form-control") }}
   </div>
   <div class="form-group">
       <label for="body">Treść</label>
       {{ form.body(class_="form-control", cols="100", rows="20") }}
   </div>
   <div class="form-check">
       {{ form.is_published(class_="form-check-input") }}
       <label class="form-check-label" for="is_published">Wpis opublikowany</label>
   </div>
   <button type="submit" class="btn btn-primary mt-5">Zapisz</button>
</form>

{% endblock %}