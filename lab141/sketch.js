let ender;

function preload(){
    ender = loadModel("ender3v3_model.stl", true);
}

function setup(){
    createCanvas(window.innerWidth, window.innerHeight, WEBGL);
    let canvas = createCanvas(400, 600); // Exemplo com dimensões de 400x400
    canvas.parent('p5-container'); // Associa o canvas a um contêiner HTML
}

function draw(){
    camera(-500, -1000, 100, 0, 0, 0, 0, 0, -2);
    colorMode (HSL);
    background(0, 85.6, 53.7);
    scale (width * 0.007);
    orbitControl(7, 7, 7);
    noStroke();
    directionalLight (0, 0, 500, 0.5, 0.5, -0.5);
    specularMaterial (250);
    shininess (1);
    model(ender);
}