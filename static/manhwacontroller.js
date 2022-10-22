var eng_div = getElementById('eng');
var kor_div = getElementById('kor');

function show_eng()
{
	eng_div.style.display = 'block';
	kor_div.style.display = 'none';
}

function show_kor()
{
	eng_div.style.display = 'none';
	kor_div.style.display = 'block';
}

eng_div.addEventListener('click', show_kor)
kor_div.addEventListener('click', show_eng)

show_eng()