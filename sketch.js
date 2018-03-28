szerokosc = 640;
wysokosc = 480;

ileKw = prompt("Podaj ilość losowanych punktów: ", 1000);
ileKw = parseInt(ileKw);
r = prompt("Podaj promień:", 100);
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
	createCanvas(640, 480);
	background(255, 204, 100);
}

function draw() {
	stroke('#000')
	ellipse(szerokosc/2, wysokosc/2, 2*r, 2*r);
	line(0, 240, 640, 240);
	line(320, 0, 320, 480);

	line(220,140,220,340);
	line(220,140,420,140);
	line(220,340,420,340);
	line(420,140,420,340);
}