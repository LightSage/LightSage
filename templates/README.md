Hello there!

{% if pfp_link %}
- Github PFP Sauce: {{ pfp_link }}
{% endif %}

## 🖼️ Catpost!

<sub>
    <img src="{{ catpost['url'] }}" height="256">
</sub>

{% if catpost['breeds'] %}
<details>
<summary>More about the breed(s) shown:</summary>
{% for breed in catpost['breeds'] %}
Breed: {{ breed['name'] }}

Description: {{ breed['description'] }}

Links:
<ul>
  <li>CFA {{ breed.get('cfa_url', "None available") }}</li>
  <li>Wikipedia {{ breed['wikipedia_url'] }}</li>
</ul> 
{% endfor %}
</details>
{% endif %}
