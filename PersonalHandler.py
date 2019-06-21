 {% if prf.image %}

            <div class="profile-img">
                <img src="{{ prf.image.url }}" id="prf_img" alt=""/>

            </div>
            {% else %}
            <div class="profile-img">
                <img src="{% static 'img/empty-profile-picture.png' %}" id="prf_img" alt=""/>

            </div>
            {% endif %}

            <a href="{% url 'upload_picture' %}">  <div class="file btn btn-lg " >
                Change Photo
                   <input type="file" name="file"/>
               </div></a>
            <form method="post" action="{% url 'profile' %}" enctype="multipart/form-data">
                {% csrf_token %}
                {{ form.as_p }}
                <input type="submit" class="btn btn-outline-success" value="upload">

            </form>
        </div>
