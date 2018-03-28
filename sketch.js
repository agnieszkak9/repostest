szerokosc = 640;
wysokosc = 480;

punktX0 = szerokosc/2;
punktY0 = wysokosc/2;

//ileKw = prompt("Podaj ilość losowanych punktów: ", 1000);
ileKw = 1000;
ileKw = parseInt(ileKw);
r = 100;
//r = prompt("Podaj promień:", 100);
ileKo = 0;

function getRnd(min, max) {
	return Math.random() * (max - min) + min;
}

lx = [];
ly = [];

for(i = 0; i < ileKw; i++) {
		x = Math.floor(getRnd(r, -r));
		y = Math.floor(getRnd(r, -r));
		//console.log(x);
		//console.log(y);
		lx[i] = x;
		ly[i] = y;
  	if(x * x + y * x <= r * r) {
    	ileKo ++;
  	}
}

pi = 4 * ileKo / ileKw;
alert("Przybliżona wartość Pi: " + pi);

function setup() {
	createCanvas(szerokosc, wysokosc);
	background('#ffffff');
}

function draw() {
	stroke('#666'); // ustalenie koloru konturu
	fill('#fff'); // kolor wypełnienia
	ellipse(szerokosc/2, wysokosc/2, 2*r, 2*r); // koło
	line(szerokosc/2, 0, szerokosc/2, wysokosc); // oś x
	line(0, wysokosc/2, szerokosc, wysokosc/2); // oś y

	for(i = 0; i < ileKw; i++){
		if(lx[i]*lx[i] + ly[i]*ly[i] < r*r) {
			stroke('#f00'); // kolor czerwony dla punktów w kole
		} else {
			stroke('#000'); // kolor czarny dla punktów pozostałych
		}
		point(lx[i] + punktX0, ly[i] + punktY0);
	}
}