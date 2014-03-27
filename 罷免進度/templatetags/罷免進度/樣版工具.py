from django.template import Library

register = Library()

@register.filter
def 轉置( 矩陣 ):
	"""
		Filter - returns a list containing range made from given value
		Usage (in template):

		<ul>{% for i in [[ 1, 2, 3],[ 4, 5, 6]]|轉置 %}
				{% for j in i %}
					<li>{{ j }}. Do something</li>
			{% endfor %}
		{% endfor %}</ul>

		Results with the HTML:
		<ul>
			<li>1. Do something</li>
			<li>4. Do something</li>
			<li>2. Do something</li>
			<li>5. Do something</li>
			<li>3. Do something</li>
			<li>6. Do something</li>
		</ul>
	"""
	return zip(*矩陣)
	
@register.filter
def 變字串(物件):
	if isinstance(物件, float):
		return str(round(物件,1))+'%'
	return 物件
		